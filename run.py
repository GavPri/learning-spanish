# python code goes here
# import pyttsx3
import googletrans
from googletrans import Translator
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('new_phrases')


en_es = SHEET.worksheet('english_to_spanish')
en_es_data = en_es.get_all_values()


def lang_choice():
    choice = input('Please choose what language you would like to translate FROM ("es" or "en"):')
    if choice == "en":
        trans_english_to_spanish()
    elif choice == 'es':
        trans_spanish_to_english()    
    else:
        print('Oops, please choose "es" or "en"\n')
        return lang_choice()    


def trans_english_to_spanish():
    """
    Function to translate user inout from English To Spanish. 
    """
    while True:
        global phrase
        translator = Translator()
        phrase = input(
            'Please enter the phrase that you would like to be translated: '
        )
        if phrase.isdigit():
            print('Please enter words and phrases, not digits!\n')
            continue
        else:
            break

    language_en = translator.detect(phrase).lang

    if language_en != 'en':
        print('Oops, no language was detected. Please try again')
        return trans_english_to_spanish()
    else:
        translation = translator.translate(phrase, src='en', dest='es')
        print(f' {phrase} is being translated to Spanish...\n')
        print(f'"{phrase}" translates to "{translation.text}" in Spanish\n')
        update_worksheet_en(phrase, translation)
        return lang_choice()


def trans_spanish_to_english():
    """
    Function to translate user input from Spanish to English.
    """
    global phrase
    while True:
        translator = Translator()
        phrase = input(
            'Please enter the phrase that you would like to be translated: '
        )

        if phrase.isdigit():
            print('Please enter words and phrases, not digits!\n')
            continue
        else:
            break

    language = translator.detect(phrase).lang

    if language != 'es':
        print('Oops, Spanish was not detected, please try again!')
        return trans_spanish_to_english()
    else:
        translation = translator.translate(phrase, src='es', dest='en')
        print(f'\n {phrase} is being translated to English..\n')
        print(f'"{phrase}" translates to "{translation.text}" in English\n')
        update_worksheet_es(phrase, translation)
        return lang_choice()


def update_worksheet_en(phrase, translation):
    """
    Function to update the "english_to_spanish" 
    worksheet with the input phrase and its translation.
    """
    print('Updating phrase worksheet...\n')
    en_worksheet = SHEET.worksheet('english_to_spanish')
    en_worksheet.append_row([phrase, translation.text])
    print('New phrase added to worksheet!')


def update_worksheet_es(phrase, translation):
    """
    Function to update the "english_to_spanish" worksheet with the input
    phrase and its translation.
    """
    print('Updating phrase worksheet...\n')
    es_worksheet = SHEET.worksheet('spanish_to_english')
    es_worksheet.append_row([phrase, translation.text])
    print('New phrase added to worksheet!\n')


lang_choice()