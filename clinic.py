# Main page
from reception import reception_main_menu
from doctor import doctor_main_menu

# Define an empty patient list to start with
patient_list = []

# Starting with a user = 0 since no input yet from the user
user = 0

while True:
    print(f'\n*** KLM MEDICAL CENTRE ***')
    print(f'-- Melbourne, Victoria --')
    print("-" * 25)
    print(f'\nWELCOME!')

    print(f'\nPlease choose user:\n 1 = Reception \n 2 = Doctor \n 3 = Exit\n')
        # 1 = "Reception: Main Files"
        # 2 = "Doctor\'s Files"
        # 3 = "Exit" 
  
    try:
        user = int(input('User:  '))  
                       
        match user:
            case 1:
                reception_main_menu(patient_list)
                # opens to patients' files
            case 2:
                doctor_main_menu(patient_list)
                # opens Doctor's Files
            case 3:
                print(f'\nThank you!\n')
                break
            case _:
                print(f'\nInvalid user. Please choose from option 1 to 3.\n')

    except ValueError:
        print(f'\nInvalid input. Please enter a valid number between 1 and 3.')
                
    
                
    


