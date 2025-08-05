"""
clinic.py - This is the main entry point for the application.

It launches the application and directs user to the appropriate module once they have selected their role.

Imported Modules
----------------
- Reception (reception.py)
    Manages patient registration and other reception-related tasks.
- Doctor (doctor.py)
    Accesses patients' records, lab test results and generates appropriate PDF reports.

Variables
---------
patient_list : list
    It contains the list of Patient objects that is shared by both reception and doctor modules.
    
Errors
------
- The script also raises ValueError if the user provided a wrong input (input should be an integer value between 1 and 3 only).
"""


from reception import reception_main_menu
from doctor import doctor_main_menu

#Main page
patient_list = []

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
                
    
                
    


