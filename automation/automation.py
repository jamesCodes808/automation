import shutil
import re
import os

existing_phones = []
existing_emails = []
# grab all phone numbers from existing contacts
with open('./assets/existing-contacts.txt', 'r') as existing_f:
    existing_contacts = existing_f.readlines()

existing_contacts = [line.replace('\n', '') for line in existing_contacts]
# print(existing_contacts)

for line in existing_contacts:
    existing_phones = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
    existing_emails = re.findall(r'\S+@\S+', line)
#


# put potential contacts into a variable
with open('./assets/potential-contacts.txt', 'r') as potential_f:
    potential_contacts = potential_f.readlines()

# grab possible phone numbers in potential contacts
phone_found = []
for line in potential_contacts:
    # create regex for phone numbers
    # load phone numbers into a list from a 2D list
    phone_found.append(re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line))
    phone_content = [phone_num for sublist in phone_found for phone_num in sublist]

phone_txt = ''
# compare if phone number already exists
for i, phone_num in enumerate(phone_content):
    for existing_num in existing_phones:
        # if it is then bypass and take out of the list
        if phone_num == existing_num:
            phone_content.pop(i)
        # if not, write to txt file
        else:
            phone_txt += phone_num + '\n'

with open('./assets/phone_numbers.txt', 'w') as f:
    f.write(phone_txt)

#
# # grab possible emails from potential contacts
email_found = []
for line in potential_contacts:
    # insert regex to find emails
    # load emails to a variable from a 2D list
    email_found.append(re.findall(r'\S+@\S+', line))
    email_content = [email for sublist in email_found for email in sublist]

email_txt = ''
# compare if phone number already exists
# for i, email in enumerate(email_content):
#     for existing_email in existing_emails:
#         # if it is then bypass and take out of the list
#         if email == existing_email:
#             email_content.pop(i)
#         # if not, write to txt file
#         else:
#             print(email)
#             email_txt += email + '\n'

for email in email_content:
    email_txt += email + '\n'

with open('./assets/emails.txt', 'w') as f:
    f.write(email_txt)

# shutil.copy('phone_numbers.txt', './assets')
# shutil.copy('emails.txt', './assets')

