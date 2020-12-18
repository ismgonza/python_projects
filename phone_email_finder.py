import pyperclip
import re

# regex for phones
regPhone = re.compile(
    r'\+?\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}')

# regex for emails
regEmail = re.compile(r'''
    [\w\-\.\_\+]+          # username
    \@                      # @ symbol
    [\w\-\_]+             # domain
    \.[A-Za-z]{2,3}         # dot TLD
    ''', re.VERBOSE)

listPhones = regPhone.findall(pyperclip.paste())
listEmail = regEmail.findall(pyperclip.paste())

if (len(listPhones) != 0 or len(listEmail) != 0):
    print('\n***** List of Phones:')
    for phone in listPhones:
        print(phone)
    print('\n***** List of Emails:')
    for email in listEmail:
        print(email)
    print()
else:
    print('***** No info was captured *****')

# Other Method

# text = str(pyperclip.paste())

# matches = []

# for groups in phone_reg.findall(text):
#     matches.append(groups)
# for groups in email_reg.findall(text):
#     matches.append(groups)

# # Paste them into clipboard
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('Following is the list of copied emails and phones from your clipboard:\n')
#     print('\n'.join(matches), '\n')
# else:
#     print('nothing copied')
