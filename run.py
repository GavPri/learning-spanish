# python code goes here
# H
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


def trans_english_to_spanish():
    """
    Function to translate user inout from English To Spanish. 
    """
    translator = Translator()
    phrase = input('Please enter the phrase that you would like to be translated: ')
    translation = translator.translate(phrase, src='en', dest='es')
    print(f'\n {phrase} is being translated to Spanish...\n')
    print(f'"{phrase}" translates to "{translation.text}" in Spanish')


trans_english_to_spanish()