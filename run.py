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


def student_choice():
    """
    This function asks the user whether they want to translate a phrase or learn a new random phrase. 
    If they choose to translate a phrase, it calls the lang_choice_beta function. 
    If they choose to learn a new random phrase, it calls the learn_spanish_saying function. 
    If they enter an invalid option, it prompts them to enter a valid option.
    """
    trans_or_learn = input(
        'Press 1 to translate a phrase, press 2 to learn a new random phrase.'
        )
    if trans_or_learn == '1':
        lang_choice_beta()
    elif trans_or_learn == '2':
        learn_spanish_saying()
    else:
        print('Oops, please enter 1 or 2.')
        student_choice()


def lang_choice_beta():
    """
    This function prompts the user to choose which language they would like to translate from, 
    either "en" for English or "es" for Spanish. If the user enters an invalid option, it prompts them to 
    enter a valid option. If the user enters a valid option, it calls the translate_phrase function.
    """
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
        translate_phrase(src_lang, dest_lang)
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
    save_location = SHEET.worksheet('es_to_en')
    cool_phrase_data = cool_phrase.get_all_values()[1:]
    random_saying = random.choice(cool_phrase_data)
    spanish_phrase = random_saying[0]
    english_translation = random_saying[1]
    print('Generating new phrase...\n')
    print(
        f'Phrase of the day is: {spanish_phrase} - {english_translation}\n'
        )
    
    def save_phrases():
        storage = input(
            'Would you like to save this phrase to your worksheet? yes or no? '
            )
        if storage == 'yes':
            print('Updating Spanish to English worksheet...\n')
            save_location.append_row([spanish_phrase, english_translation])
            print('Worksheet has been updated!')
            new_phrase_reset()
        elif storage == 'no':
            print('New phrase NOT added to worksheet.')
            new_phrase_reset()
        else:
            print('Oops, please enter "yes" or "no"')
            save_phrases()
    save_phrases()


def new_phrase_reset():
    reset = input(
            'Continue learning? yes or no?\n'
        )
    if reset == 'yes':
        student_choice()
    elif reset == 'no':
        print("Thank you, see you soon!")
        exit()
    else:
        print('Oops, please enter yes or no')
        new_phrase_reset()


student_choice()
