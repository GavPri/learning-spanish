# python code goes here
# import pyttsx3
# import googletrans
import random
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


def lang_choice_beta():
    pick = input(
        'Choose which language you would like to translate from es or en: '
        )
    if pick == 'en':
        translate_phrase('en', 'es')
    elif pick == 'es':
        translate_phrase('es', 'en')
    else:
        print('Oops, please enter "en" for English or "es" for Spanish')
        return lang_choice_beta()


def translate_phrase(src_lang, dest_lang):
    while True:
        translator = Translator()
        phrase = input(
            'Please enter the phrase you would like to have translated: '
            )

        if phrase.isdigit():
            print('Please only enter words and phrases, not digits!')
            continue
        else:
            break

    language = translator.detect(phrase).lang

    if language != src_lang:
        print(f'Oops! {src_lang} was not detected, please try again.')
    else:
        translation = translator.translate(
            phrase, src=src_lang, dest=dest_lang
            )
        print(f'\n {phrase} is being translated to {dest_lang}..\n')
        print(
            f'"{phrase}" translates to "{translation.text}" in {dest_lang}\n'
            )
        worksheet_name = f'{src_lang}_to_{dest_lang}'
        update_worksheet(phrase, translation, worksheet_name)
        lang_choice_beta()


def update_worksheet(phrase, translation, worksheet_name):
    print('Updating worksheet')
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row([phrase, translation.text])
    print('Worksheet has been updated!')
    return leave_translation()


def leave_translation():
    leave_option = input(
        'Is there another phrase you would like to translate? "yes" or "no": '
        )
    if leave_option == "no":
        print('Thank you, goodbye!')
        exit()
    elif leave_option == "yes":
        lang_choice_beta()
    else:
        print('Oops, please choose yes or no')
        return leave_translation()


def learn_spanish_saying():
    cool_phrase = SHEET.worksheet('cool_phrase')
    cool_phrase_data = cool_phrase.get_all_values()
    random_saying = random.choice(cool_phrase_data)
    spanish_phrase = random_saying[0]
    english_translation = random_saying[1]
    print(f'{spanish_phrase} - {english_translation}')


learn_spanish_saying()


lang_choice_beta()
