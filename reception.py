from entities import Patient
import numpy as np
from dateutil.parser import parse
import csv

# Call function(options) to main menu  
def reception_main_menu(patient_list = []):
    """Main menu where user can input the necessary details of the patient"""
    print(f'\n--Welcome to Reception: Main Files--\n')
    option = 0
    while (option <= 4):
        print(f'Please choose an option:\n 1 = Add new patient \n 2 = Export patient details \n 3 = Exit\n')
        option = int(input('Option: '))
        match option:
            case 1:
                while True:
                    add_patient(patient_list)
                    add = input('Add another patient? (y/n): ').strip().lower()
                    if add != 'y':
                        break
            case 2:
                master_list(patient_list)
                print(f'Patient files exported to Patients Master List.\n')
                
            case 3:
                print(f'\nThank you! Exiting system.\n')
                break
            case _:
                print(f'\nInvalid option. Please try again.\n')
 
 
# Add new patient
def add_patient(patient_list):
    correct_input = False
    while correct_input != True:
        # First name
        while True:
            first_name = input('Enter first name: ').strip().capitalize()
            if first_name: 
                break
        # Last name
        while True:
            last_name = input('Enter last name: ').strip().capitalize()
            if last_name: 
                break
            
        full_name = (f'{first_name} {last_name}')
        
        # Birthday
        while True:
            try:
                birthday_str = input("Enter birthdate DD/MM/YYYY: ").strip()
                birthday = parse(birthday_str, dayfirst=True).date()
                break
            except (ValueError, OverflowError):
                print("Invalid date. Please enter date of birth.\n")
        
        # Sex / Gender
        while True:
            sex = input("Enter sex (M/F): ").strip().upper()
            if sex in ['M','F']:
                break
            print("Sex must be 'M' or 'F'.\n")
        
        # existing patient
        if full_name in patient_list:
                    print(f'{full_name} is already an existing patient.\n')
        else:
            # Generate random ID
            initials = f"{first_name[0].upper()}{last_name[0].upper()}"
            random_part = np.random.randint(100000, 999999)
            patient_id = f'{initials}-{random_part}'
            
            # Add new patient to patient list
            new_patient = Patient(patient_id,full_name,birthday,sex)
            patient_list.append(new_patient)
            
            print(f'{full_name} has been added to Patient records.\n')
            print(f'{new_patient.getDetails()}')
            
        correct_input = True
                
 #Write CSV file   
def master_list (patient_list = []):
    with open('patient_master_list.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Full Name', 'Birthday', 'Sex'])
        writer.writerows(map(lambda patient: [patient.id, patient.full_name, patient.birthday, patient.sex], patient_list))
      
            
  
    
    
            

        

