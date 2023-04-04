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

## Usage.  
To use this project, follow the steps listed bellow: 

- In the terminal enter "python3 run.py"
- When the program first runs, you will be able to choose:
    - If you would like to translate a phrase by pressing 1 or
    - Learn a new phrase that is randomly selected from a google sheet by pressing 2. 

### Choosing Tranlation. 
- If you choose to translate a phrase, it will ask you if you to
choose which language you would like to translate from. (English or Spanish)
- The user is then prompted to input the phrase that they would like to translate. 
    - The user is prevented from entering integers as they do not require translation. 
    - Googletrans API also has a language detect feature, It is used in this project to prevent inputs
    that are not detected as the language choosen. If invalid inputs are provided
    the function prompts the user to re-enter their input. 

### Updating the spreadsheet after translation. 
- Once the users input has been validated, the corresponding spreadsheets are updated. 
with this project, I created three spreadsheets in Google sheets. 
    - The first is to store the phrases that the user translates from English to Spanish. (en_to_es)
    - The second is to store the phrases that the user translates from Spanish to English. (es_to_en)
    - The third is to house the phrases that a user can learn.
- If, in the first step, I chose to input the phrase in English, it will update the en_to_es spreadsheet. 
If I chose to translate from Spanish to English, It would update the es_to_en spreadsheet. 
- Once the spreadsheet is updated, you have the option to continue learning, inputting 'yes' will bring you back to the lang_choice function. 
- If you enter 'no' the program ends. 

### Choosing to learn a new phrase. 
- If you choose to learn a new phrase by inputting 2 at the first prompt:
    The phrase is pulled at randome from the 'cool_phrase' spreadsheet and displayed in the terminal. 

### Updating the spreadsheet after new phrase generation. 
    - You then have the choice to save the input to your the es_to_en spreadsheet or not. 
        - If you choose the the update the spreadsheet, the terminal will display when it is done. 
        - If you choose not to, the spreadsheet is not updated. 
    - After both of these outputs you are asked if you would like to continue learning. 
    - Entering 'yes' to this will return you to student_choice() function. 
    - Entering 'no' here will lead to the exiting the program. 
