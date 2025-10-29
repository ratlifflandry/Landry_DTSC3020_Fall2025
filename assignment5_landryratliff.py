with open("contacts_raw.txt", "w", encoding="utf-8") as f:
    f.write('Alice Johnson <alice@example.com> , +1 (469) 555-1234\nBob Roberts <bob[at]example.com> , 972-555-777\nSara M. , sara@mail.co , 214 555 8888\n"Mehdi A." <mehdi.ay@example.org> , (469)555-9999\nDelaram <delaram@example.io>, +1-972-777-2121\nNima <NIMA@example.io> , 972.777.2121\nduplicate <Alice@Example.com> , 469 555 1234')

print("sample contacts_raw.txt created")

def read_file(file_name):
    try:
        file = open(file_name, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("File not found! Check file path.")
        return []

def valid_email(email_address):
    email_address = email_address.strip()
    if "@" not in email_address or "." not in email_address:
        return False
    if email_address.startswith("@") or email_address.endswith("@"):
        return False
    return True

def normalize_phone(phone_number):
    digits_only = "".join(c for c in phone_number if c.isdigit())
    if len(digits_only) >= 10:
        return digits_only[-10:]
    else:
        return ""

def parse_contact_line(line_text):
    parts = [p.strip() for p in line_text.strip().split(",")]
    first_name = ""
    email_address = ""
    phone_number = ""
    email_candidate = ""

    if len(parts) == 2:
        name_email_part, phone_part = parts
        phone_number = normalize_phone(phone_part)
    elif len(parts) == 3:
        name_email_part, email_part, phone_part = parts
        phone_number = normalize_phone(phone_part)
        email_candidate = email_part
    else:
        name_email_part = parts[0]

    if "<" in name_email_part and ">" in name_email_part:
        start = name_email_part.find("<")+1
        end = name_email_part.find(">")
        email_candidate = name_email_part[start:end]
        first_name = (name_email_part[:start-1] + name_email_part[end+1:]).strip('" ')
    else:
        first_name = name_email_part.strip('" ')

    email_address = email_candidate.strip() if valid_email(email_candidate) else None

    return {"name": first_name, "email": email_address, "phone": phone_number}

def remove_duplicates(list_of_contacts):
    seen_emails = set()
    last_cleaned_contacts = []
    for contact in list_of_contacts:
        if contact["email"] and contact["email"].lower() not in seen_emails:
            last_cleaned_contacts.append(contact)
            seen_emails.add(contact["email"].lower())
    return last_cleaned_contacts

def write_csv(list_of_contacts, file_name):
    file = open(file_name, "w", encoding="utf-8")
    file.write("name,email,phone\n")
    for contact in list_of_contacts:
        file.write(f"{contact['name']},{contact['email']},{contact['phone']}\n")
    file.close()

all_lines = read_file("contacts_raw.txt")
parsed_contacts = [parse_contact_line(l) for l in all_lines]
valid_contacts = [c for c in parsed_contacts if c["email"]]
deduplicated_contacts = remove_duplicates(valid_contacts)
write_csv(deduplicated_contacts, "contacts_clean.csv")
print("Cleaned contacts saved to contacts_clean.csv")