#Assignment 6 WebScraping
import re
import sys
import pandas as pandas_library
import requests
from bs4 import BeautifulSoup

REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0 Safari/537.36"
    )
}

def fetch_html_content(website_url: str, connection_timeout: int = 20) -> str:
    website_response = requests.get(website_url, headers = REQUEST_HEADERS, timeout = connection_timeout)
    website_response.raise_for_status()
    return website_response.text


def flatten_table_headers(data_frame_table: pandas_library.DataFrame) -> pandas_library.DataFrame:
    if isinstance(data_frame_table.columns, pandas_library.MultiIndex):
        data_frame_table.columns = [
            " ".join([str(header_part) for header_part in header_tuple if str(header_part) != "nan"]).strip()
            for header_tuple in data_frame_table.columns.values
        ]
    else:
        data_frame_table.columns = [str(header_name).strip() for header_name in data_frame_table.columns]
    return data_frame_table

#QUESTION 1 - IBAN Country Codes
def read_iban_table_from_html(html_text_content: str) -> pandas_library.DataFrame:
    all_html_tables = pandas_library.read_html(pandas_library.io.common.StringIO(html_text_content))
    for single_html_table in all_html_tables:
        if single_html_table.shape[1] >= 3:
            iban_country_code_table = single_html_table
            break
    iban_country_code_table = flatten_table_headers(iban_country_code_table)
    return iban_country_code_table


def clean_iban_country_code_table(raw_iban_table: pandas_library.DataFrame) -> pandas_library.DataFrame:
    raw_iban_table.columns = [column_name.strip() for column_name in raw_iban_table.columns]

    column_rename_mapping = {}
    for column_name in raw_iban_table.columns:
        if "country" in column_name.lower():
            column_rename_mapping[column_name] = "Country"
        elif "alpha-2" in column_name.lower():
            column_rename_mapping[column_name] = "Alpha_2_Code"
        elif "alpha-3" in column_name.lower():
            column_rename_mapping[column_name] = "Alpha_3_Code"
        elif "numeric" in column_name.lower():
            column_rename_mapping[column_name] = "Numeric_Code"

    cleaned_iban_table = raw_iban_table.rename(columns = column_rename_mapping)

    important_columns = ["Country", "Alpha_2_Code", "Alpha_3_Code", "Numeric_Code"]
    cleaned_iban_table = cleaned_iban_table[[col for col in important_columns if col in cleaned_iban_table.columns]]

    cleaned_iban_table["Country"] = cleaned_iban_table["Country"].str.strip()
    cleaned_iban_table["Alpha_2_Code"] = cleaned_iban_table["Alpha_2_Code"].str.strip().str.upper()
    cleaned_iban_table["Alpha_3_Code"] = cleaned_iban_table["Alpha_3_Code"].str.strip().str.upper()

    if "Numeric_Code" in cleaned_iban_table.columns:
        cleaned_iban_table["Numeric_Code"] = pandas_library.to_numeric(
            cleaned_iban_table["Numeric_Code"], errors="coerce"
        ).astype("Int64")
    else:
        cleaned_iban_table["Numeric_Code"] = pandas_library.NA

    cleaned_iban_table = cleaned_iban_table.dropna(subset = ["Country", "Alpha_2_Code", "Alpha_3_Code"])

    return cleaned_iban_table


def sort_and_show_top_iban_countries(cleaned_iban_table: pandas_library.DataFrame, number_of_rows: int = 15) -> pandas_library.DataFrame:
    """Sort the IBAN data by numeric code descending and return the top results."""
    sorted_iban_table = cleaned_iban_table.sort_values(by = "Numeric_Code", ascending = False)
    return sorted_iban_table.head(number_of_rows)

print("QUESTION 1: IBAN Country Codes")

iban_country_codes_url = "https://www.iban.com/country-codes"
iban_html_content = fetch_html_content(iban_country_codes_url)
iban_raw_table = read_iban_table_from_html(iban_html_content)
iban_cleaned_table = clean_iban_country_code_table(iban_raw_table)
iban_top_15_countries = sort_and_show_top_iban_countries(iban_cleaned_table)

print("\nTop 15 Countries by Numeric Code:\n")
print(iban_top_15_countries)

iban_cleaned_table.to_csv("data_q1.csv", index = False)

#QUESTION 2 - Hacker News Front Page
def parse_hacker_news_items_from_html(html_text_content: str) -> pandas_library.DataFrame:
    html_soup = BeautifulSoup(html_text_content, "lxml")
    all_story_rows = html_soup.select("tr.athing")

    hacker_news_data_list = []

    for single_story_row in all_story_rows:
        story_rank_element = single_story_row.select_one(".rank")
        story_title_element = single_story_row.select_one(".titleline a")

        story_rank_text = story_rank_element.get_text(strip=True).replace(".", "") if story_rank_element else ""
        story_title_text = story_title_element.get_text(strip=True) if story_title_element else ""
        story_link_url = story_title_element["href"] if story_title_element else ""

        subtext_row = single_story_row.find_next_sibling("tr")
        story_points_element = subtext_row.select_one(".score") if subtext_row else None
        story_comments_element = subtext_row.find("a", string=re.compile("comment")) if subtext_row else None

        story_points_text = story_points_element.get_text(strip=True).replace(" points", "") if story_points_element else "0"
        story_comments_text = story_comments_element.get_text(strip=True).replace(" comments", "") if story_comments_element else "0"

        hacker_news_data_list.append({
            "Story_Rank": story_rank_text,
            "Story_Title": story_title_text,
            "Story_Link": story_link_url,
            "Story_Points": story_points_text,
            "Story_Comments": story_comments_text
        })

    hacker_news_data_frame = pandas_library.DataFrame(hacker_news_data_list)
    return hacker_news_data_frame


def clean_hacker_news_data(hacker_news_raw_data: pandas_library.DataFrame) -> pandas_library.DataFrame:
    hacker_news_cleaned_data = hacker_news_raw_data.fillna("")

    for numeric_column_name in ["Story_Rank", "Story_Points", "Story_Comments"]:
        hacker_news_cleaned_data[numeric_column_name] = (
            hacker_news_cleaned_data[numeric_column_name]
            .astype(str)
            .str.extract(r"(\d+)")
            .fillna(0)
            .astype(int)
        )

    hacker_news_cleaned_data["Story_Title"] = hacker_news_cleaned_data["Story_Title"].replace("", "N/A")
    hacker_news_cleaned_data["Story_Link"] = hacker_news_cleaned_data["Story_Link"].replace("", "N/A")

    return hacker_news_cleaned_data


def sort_and_show_top_hacker_news_stories(cleaned_hacker_news_data: pandas_library.DataFrame, number_of_rows: int = 15) -> pandas_library.DataFrame:
    """Sort by story points and return top stories."""
    sorted_hacker_news_data = cleaned_hacker_news_data.sort_values(by="Story_Points", ascending = False)
    return sorted_hacker_news_data.head(number_of_rows)

print("QUESTION 2: Hacker News Stories")

hacker_news_url = "https://news.ycombinator.com/"
hacker_news_html_content = fetch_html_content(hacker_news_url)
hacker_news_raw_data = parse_hacker_news_items_from_html(hacker_news_html_content)
hacker_news_cleaned_data = clean_hacker_news_data(hacker_news_raw_data)
hacker_news_top_15_stories = sort_and_show_top_hacker_news_stories(hacker_news_cleaned_data)

print("\nTop 15 Hacker News Stories by Points:\n")
print(hacker_news_top_15_stories)

hacker_news_cleaned_data.to_csv("data_q2.csv", index=False)
