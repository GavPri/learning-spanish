# Love Spanish 
Love Spanish is a project that translates a phrase from English to Spanish and Vice Versa using the Google translate API. When the phrase is translated, the phrase inputted and the translation provided are added to a google sheet for storage using the gspread. 

I built this prpject as I always enjoyed learning Spanish. I currently work with a lot of Spanish speaking people. I made this as a place to keep the new phrases that I learn.  

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
![translation-process](/assets/images/translation-function.png)

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

## Testing 
I have tested the code in this project by:
    Passing the code into the PEP8 linter and this detected no issues in the code 
    I tested all input ares to test how they handle in valid inputs such as:
        - entering symbols, integers, blank spaces and various other characters when strings are required. 
    These tests took place in my local terminal. 
![input handling](/assets/images/input-handling.png)

## Bugs 
With some one one entries, the detect function will not detect the language you wish to translate from. 
    - For example, entering the word 'cunning' to be translated from english to spanish will not work. 
    - To fix this, more context is needed in the sentence you provide, for example: 
        'Cunning as a fox' will return a translation containing the translation for 'cunning'. 
To fix this bug, I entered a try except block to catch TypeErrors. 

## Remaining Bugs 
- No remianing bugs. 

## Validator Testing
- PEP8:
    Running my code in the PEP8 validator returned no errors. 

## Deployment

This app was deployed on Heroku. 
    Steps for deployment:
    Create a new app from the Heroku dashboard.
    Named the app and select the region, then click "Create app".
    Set up my app settings, including config vars to store sensitive data.
    Add buildpacks to install further dependencies outside of the requirements.txt file.
    Choose manual deployment method.
    Connected Heroku app to my GitHub repository code.
    Choose to manually or automatically deploy the app.
    Wait for the app to build and check the logs for any errors.
    Tested program to see if it works properly.  
