"""
reception.py - This is the reception module of the application

This module contains the functions for new patient registration and patient data export to a CSV file.

Imports
-------
- Patient (entities): The Class representing a patient.
- numpy as np: It is used to generate random patient IDs.
- parse (dateutil.parser): It is a powerful function that converts strings into datetime objects, automatically detecting the format.
- csv: It is used to write patient data into a .csv file.

Functions
---------
- reception_main_menu(patient_list = []):
    Main menu or interface where user (receptionist) can add new patients or export patient records.

- add_patient(patient_list):
    A function that allows the user to create a new Patient object by entering validated input data. It also generates a unique ID for each patient.

- master_list (patient_list = []):
    It adds new patient object to the current master list.
"""

from entities import Patient
import numpy as np
from dateutil.parser import parse
import csv

# Call function(options) to main menu  
def reception_main_menu(patient_list = []):
    """
    Launches the main menu for reception staff.
    
    Parameters
    ----------
    patient_list : list
        The list of Patient objects shared with the main system.
        
    Options 
    -------
    1 = Add a new patient
    2 = Export patient list to CSV file
    3 = Exit menu
    """
    
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
    """
    Prompts the user (receptionist) to input new patient's details and adds them to the patient_list.
    
    Features
    --------
    - validates first and last names
    - checks and parses birth date format
    - generates unique patient ID
    - confirms sex of patient (Male or Female)
    
    Parameters
    ----------
    patient_list : list
        The list where the new Patient will be added. 
    """

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
    """
    Current patient list will be exported to a CSV file and named patient_master_list.csv.
    
    Parameters
    ----------
    - patient_list : list
        The list of Patient objects to be written to the file.
    """
    
    with open('patient_master_list.csv', 'w') as f: # w means write into the file
        writer = csv.writer(f)
        writer.writerow(['ID', 'Full Name', 'Birthday', 'Sex'])
        writer.writerows(map(lambda patient: [patient.id, patient.full_name, patient.birthday, patient.sex], patient_list))
      
            
  
    
    
            

        

