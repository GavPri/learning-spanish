# Love Spanish 
Love Spanish is a project that translates a phrase from English to Spanish and Vice Versa using the Google translate API. When the phrase is translated, the phrase inputted and the translation provided are added to a google sheet for storage using the gspread. 

I built this prpject as I always enjoyed learning Spanish and I wanted a program to translate and save the new phrases that I have learned. 

## Dependencies 
In order to make this project, I relied upon some libraries and modules. 
    - gspread: This library allows the project to access the necessary google sheet
    - google-auth: A library that allows autorisation for Google API's. 
    - googletrans: A libray that provides translations from one language to another. 

    These libraries were installed using this entry in the projects terminal: 
        ` pip install googletrans gspread google-auth `

## Usage 
To use this project, follow the steps listed bellow: 

- In the terminal enter "python3 run.py"
- When prompted to choose your language of choice, enter 'en' for English and 'es' for Spanish, once choosen, hit enter key. Be sure not to have any whitespace on either side of the letters. 
- You will then be promted to enter the phrase you would like to be translated from yuor selected language. Enter the phrase. 
- The translated text as well as the original input will be displayed in the terminal. They will also be allocated to the correct google sheet. 
