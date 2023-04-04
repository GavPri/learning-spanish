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


en_es = SHEET.worksheet('en_to_es')
en_es_data = en_es.get_all_values()


def lang_choice():
    choice = input(
        'Please choose what language you would like to translate FROM "es" or "en": '
        )
    if choice == "en":
        worksheet = 'en_to_es'
        trans_english_to_spanish()
    elif choice == 'es':
        worksheet = 'es_to_en'
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
        worksheet = 'english_to_spanish'
        update_worksheet(phrase, translation, worksheet)
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
        worksheet = 'spanish_to_english'
        update_worksheet(phrase, translation, worksheet)
        return lang_choice()


def update_worksheet(phrase, translation, worksheet):
    print('Updating worksheet')
    worksheet = SHEET.worksheet(f'{src_lang}_to_{dest_lang}')
    worksheet.append_row([phrase, translation.text])
    print('Worksheet has been updated!')


lang_choice()