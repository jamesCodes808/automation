import shutil
import re

existing_phones = []
existing_emails = []
# grab all phone numbers from existing contacts
with open('../assets/existing-contacts.txt', 'r') as existing_f:
    existing_contact = existing_f.readlines()

for line in existing_contact:
    existing_phones = re.findall(r'', line)
    existing_emails = re.findall(r'', line)
# grab possible phone numbers in potential contacts
with open('../assets/potential-contacts.txt', 'r') as potential_f:
    potential_contacts = potential_f.readlines()

# grab possible emails from potential contacts
phone_content = []
for line in potential_contacts:
    # create regex for phone numbers
    # load phone numbers into a variable
    phone_content = re.findall(r'', line)

    # compare if phone number already exists
    for i,phone_num in enumerate(phone_content):
        for existing_num in existing_phones:
            # if it is then bypass
            if phone_num == existing_num:
                phone_content.pop(i)
            # if not, write to txt file
            else:
                with open('../assets/phone_numbers.txt', 'r') as f:
                    f.write(phone_num)



email_content = []
for _ in range(100):
    # insert regex to find emails
    email_content = re.findall(r'', line)

    # compare if phone number already exists
    for i, email in enumerate(email_content):
        for existing_email in existing_emails:
            # if it is then bypass
            if email == existing_email:
                email_content.pop(i)
            # if not, write to txt file
            else:
                with open('../assets/emails.txt', 'r') as f:
                    f.write(email)


shutil.copy('phone_numbers.txt', '../assets')
shutil.copy('emails.txt', '../assets')