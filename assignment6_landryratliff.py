#Assignment 6 — Web Scraping

import re
import pandas as pandas_library
import requests
from bs4 import BeautifulSoup

request_headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0 Safari/537.36"
    )
}

#QUESTION 1 — IBAN Country Codes
print("QUESTION 1: IBAN Country Codes")

iban_website_url = "https://www.iban.com/country-codes"
iban_response = requests.get(iban_website_url, headers=request_headers)
iban_html_content = iban_response.text

all_html_tables = pandas_library.read_html(pandas_library.io.common.StringIO(iban_html_content))

for single_html_table in all_html_tables:
    if single_html_table.shape[1] >= 3:
        iban_country_table = single_html_table
        break

iban_country_table.columns = [column_name.strip() for column_name in iban_country_table.columns]

column_name_mapping = {}
for column_name in iban_country_table.columns:
    if "country" in column_name.lower():
        column_name_mapping[column_name] = "Country"
    elif "alpha-2" in column_name.lower():
        column_name_mapping[column_name] = "Alpha_2_Code"
    elif "alpha-3" in column_name.lower():
        column_name_mapping[column_name] = "Alpha_3_Code"
    elif "numeric" in column_name.lower():
        column_name_mapping[column_name] = "Numeric_Code"

iban_country_table = iban_country_table.rename(columns=column_name_mapping)

important_columns = ["Country", "Alpha_2_Code", "Alpha_3_Code", "Numeric_Code"]
iban_country_table = iban_country_table[[col for col in important_columns if col in iban_country_table.columns]]

iban_country_table["Country"] = iban_country_table["Country"].str.strip()
iban_country_table["Alpha_2_Code"] = iban_country_table["Alpha_2_Code"].str.strip().str.upper()
iban_country_table["Alpha_3_Code"] = iban_country_table["Alpha_3_Code"].str.strip().str.upper()

iban_country_table["Numeric_Code"] = pandas_library.to_numeric(
    iban_country_table["Numeric_Code"], errors="coerce"
).astype("Int64")

iban_country_table = iban_country_table.dropna(subset=["Country", "Alpha_2_Code", "Alpha_3_Code"])

iban_country_table_sorted = iban_country_table.sort_values(by="Numeric_Code", ascending=False)
iban_country_top_15 = iban_country_table_sorted.head(15)

print("\nTop 15 Countries by Numeric Code:\n")
print(iban_country_top_15)

iban_country_table.to_csv("data_q1.csv", index=False)

#QUESTION 2 — Hacker News Front Page
print("QUESTION 2: Hacker News Stories")

hacker_news_url = "https://news.ycombinator.com/"
hacker_news_response = requests.get(hacker_news_url, headers=request_headers)
hacker_news_html_content = hacker_news_response.text

hacker_news_soup = BeautifulSoup(hacker_news_html_content, "lxml")
all_story_rows = hacker_news_soup.select("tr.athing")

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

hacker_news_table = pandas_library.DataFrame(hacker_news_data_list)

hacker_news_table = hacker_news_table.fillna("")
for numeric_column_name in ["Story_Rank", "Story_Points", "Story_Comments"]:
    hacker_news_table[numeric_column_name] = (
        hacker_news_table[numeric_column_name]
        .astype(str)
        .str.extract(r"(\d+)")
        .fillna(0)
        .astype(int)
    )

hacker_news_table["Story_Title"] = hacker_news_table["Story_Title"].replace("", "N/A")
hacker_news_table["Story_Link"] = hacker_news_table["Story_Link"].replace("", "N/A")

hacker_news_table_sorted = hacker_news_table.sort_values(by="Story_Points", ascending=False)
hacker_news_top_15 = hacker_news_table_sorted.head(15)

print("\nTop 15 Hacker News Stories by Points:\n")
print(hacker_news_top_15)

hacker_news_table.to_csv("data_q2.csv", index=False)

print("\nBoth datasets have been saved successfully.")
