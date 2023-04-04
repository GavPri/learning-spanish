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
    This function asks the user whether they want to translate a phrase or
    learn a new random phrase. If they choose to translate a phrase, it calls
    the lang_choice_beta function. If they choose to learn a new random phrase,
    it calls thelearn_spanish_saying function. If they enter an invalid option,
    it prompts them to enter a valid option.
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
    This function prompts the user to choose which language they would like to
    translate from, either "en" for English or "es" for Spanish.
    If the user enters an invalid option, it prompts them to
    enter a valid option. If the user enters a valid option,
    it calls the translate_phrase function.
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
    """ This function prompts user to enter a phrase for translation.
    If phrase contains digits, user is prompted to only enter words or phrases.
    If entered phrase language is not the selected source language, user is
    prompted to enter a valid phrase.If entered phrase language is
    source language,it translates phrase to destination language,
    prints translation and calls update_worksheet() to
     update worksheet."""
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
    
    try:
        language = translator.detect(phrase).lang
    except TypeError:
        print('Oops, please add more context!')
        return translate_phrase(src_lang, dest_lang)

    if language is None or language != src_lang:
        print(f'Oops! {src_lang} was not detected, please try again.')
        translate_phrase(src_lang, dest_lang)
    else:
        try:
            translation = translator.translate(phrase, src=src_lang, dest=dest_lang)
        except TypeError:
            print('Oops, please add more context!')
            return translate_phrase(src_lang, dest_lang)
        print(f'{phrase} is being translated to {dest_lang}..\n')
        print(
            f'"{phrase}" translates to "{translation.text}" in {dest_lang}\n'
            )
        worksheet_name = f'{src_lang}_to_{dest_lang}'
        update_worksheet(phrase, translation, worksheet_name)


def update_worksheet(phrase, translation, worksheet_name):
    print('Updating worksheet')
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row([phrase, translation.text])
    print('Worksheet has been updated!')
    return leave_translation()


def leave_translation():
    """
    This function gives the user the option to leave the program,
    if they choose yes, the function will return them to lang_choice.
    If they choose no, it will say goodbye and exit the program.
    if the entry is invalid, it will return to the beginning of the
    leave_translation function.
    """
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
    """
    This function generates a random Spanish phrase and its English
    translation from the "cool_phrase" worksheet.
    It prompts the user to indicate whether they would like to
    save the phrase and its translation to the
    "es_to_en" worksheet.
    If the user indicates that they would like to save the phrase and its
    translation,
    it updates the "es_to_en" worksheet with the phrase and its translation
    and calls the new_phrase_reset
    function. If the user indicates that they do not want to save the phrase
    and its translation, it calls the new_phrase_reset function.
    If the user enters an invalid option, it prompts the user to enter
    a valid option and calls itself.
    """

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
    """
    Ask the user if they want to save the current phrase to their worksheet.
    Prompts the user to enter "yes" or "no" to indicate whether they want to
    save the current phrase to their worksheet or not,
    respectively. If the user enters an invalid input,
    the function prompts the user to re-enter their
    choice.
    """
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
