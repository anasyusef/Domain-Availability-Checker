from string import ascii_lowercase
import os.path

USERNAME = "anasyusef"
API_KEY = "393a2dc4ecd74a1e881cae01f3c727c0"
IP_ADDRESS = "81.136.30.106"
SANDBOX = False
HOME_URL = 'https://www.domaining.com/'
URL_VALUATE = 'https://www.domaining.com/valuate/'
URL_LOGIN = 'https://www.domaining.com/login/'
FOLDER_TO_SAVE_FILENAME_DOMAINS = 'letters_dictionary/'
LOG_FILE = 'logs/'
# COOKIE_ID = "9760aeef4f259a70d0efd138fbe6d967"


print("How would you like to get your domains.\nType 'generate' to generate them or 'file' to retrieve them from file.")
while True:
    domain_get_method = str(input('> '))
    if domain_get_method.lower() == 'generate':
        domain_get_method = 'generate'
        break
    elif domain_get_method.lower() == 'file':
        domain_get_method = 'file'
        break
    else:
        print('Make sure you have typed the word correctly')
        continue
print("Please type the TLD desired to search for (without the dot), i.e. 'com'")
with open('TLDS/tlds-alpha-by-domain.txt', 'r') as tlds_file:
    tlds_accepted = [tld.replace('\n', '').lower() for tld in tlds_file]
while True:

    tld = str(input('> '))
    if not bool(tld.strip()):
        print('Please enter something')
        continue
    if tld.lower()[0] not in ascii_lowercase or tld.lower() not in tlds_accepted:
        print('Make sure you have typed the word correctly and that the TLD is accepted')
        continue
    else:
        tld = '.' + str(tld.lower())
        break
if domain_get_method == 'generate':
    print('Enter how many letters you would like to generate all the permutations')
    while True:
        user_input_letters = str(input('> '))
        if user_input_letters.isdigit():
            if int(user_input_letters) <= 10:
                user_input_letters = int(user_input_letters)
                break
        else:
            print("Make sure that you have typed a correct number and that you have not typed a large one.")
            continue

else:
    print("Please type the name of the file you want this program to use without the extension name.\n"
          "It must be 'txt'")
    while True:
        user_filename_domains = str(input('> '))
        filename_domains = FOLDER_TO_SAVE_FILENAME_DOMAINS + user_filename_domains + '.txt'
        if os.path.isfile(filename_domains) is False:
            print('This file does not exist. Please make sure that you have correctly typed the name of the file.')
            continue
        else:
            break


filename = 'domain_' + \
           user_filename_domains.replace('/', '_') + '_' + tld[1:]\
           + '_' + domain_get_method if domain_get_method == 'file' else \
           'domain_' + domain_get_method + '_' + tld[1:] + '_' + str(user_input_letters)

filename += '.csv'

log_filename = LOG_FILE + 'domain_' + tld[1:] + '_' + domain_get_method + '.log'

