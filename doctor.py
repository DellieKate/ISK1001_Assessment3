"""
doctor.py - Doctor module of the application

This module contains the functions to search and view details of a patient, then the app will be able to recommend specific lab tests based on the patient's age and sex. Finally, the user (doctor) has an option to generate a PDF report.

Imports
-------
- All classes from entities module (Patient, LabTest, BiochemTest, HemaTest, CytoTest and Generic Test):
    These classes are integral to manage patient data and lab tests. 
- create_pdf (create_pdf.py)
    This is the module used to print patient reports as PDF file.
    
Functions
---------
- doctor_main_menu(patient_list = []):
    This is the main menu where user (doctor) can search for patients using their IDs, attach recommended lab tests and print a PDF report.
    
- recommend_labtest(patient):
    It defines the recommended lab tests based on the patient's age and sex, then adds these tests to the patient's labtest_list.

- find_patient_by_id(patient_list, patient_id):
    It searches a particular patient using the unique ID in the patient list.
"""

from entities import Patient, LabTest, BiochemTest, HemaTest, CytoTest, GenericTest
import create_pdf


def doctor_main_menu(patient_list = []):
    """
    Main interface in the doctor's module.
    
    Usage 
    -----
    User needs to input the patient's ID to retrieve the corresponding details from the patient_list. If patient details are retrieved, the app will recommend the necessary lab tests along with its description. There is an option at the end either to print the report as a PDF or not.
    """
    
    print(f'\nWelcome to Doctor\'s Files.')
    option = 0
    while (option <= 4):
        print(f'\nPlease choose an option:\n 1 = Search patient \n 2 = Exit\n')
        option = int(input('Option: '))
        match option:
            case 1:
                pID = input('Input patient ID: ' ).strip()
                patient = find_patient_by_id(patient_list, pID)
                if patient:
                    recommend_labtest(patient)
                    print(f'Recommended tests for {patient.full_name}')
                    for test in patient.labtest_list:
                        print(f'\t {test.description}')                        
                    print_report = input('\nPrint patient\'s report? Y/N  \n').strip().capitalize()
                    if print_report == 'Y':
                        print("Printing patient details...")
                        create_pdf.print(patient)
                else:
                    print(f'Patient with {pID} is not found.')
            case 2:
                print(f'\nThank you!\n')
                break
            case _:
                print(f'\nInvalid option. Please try again.\n')
                

generic_test = [GenericTest("FBC"), GenericTest("EUC"), GenericTest("LFT"), GenericTest("lipids")]
""" A list of generic tests including FBC, EUC, LFT, lipids. """
    
def recommend_labtest(patient):
    """
    This function recommends or assigns appropriate lab tests based on the patient's age and sex.
    
    Recommendations
    ---------------
    - age <= 15 : Observation only.
    - age 15 - 18 : Generic tests.
    - age >= 18: Generic + HemaTest.
    - age >= 18 and female : + CytoTest.
    - age >= 45 and not female : + Biochem Test.
    """
    
    if patient.age <= 15:
        print(f'Observation recommended.')
    if 15 <= patient.age <= 18:
        patient.labtest_list.extend(generic_test)
    if patient.age >= 18 :
        patient.labtest_list.extend(generic_test)
        patient.labtest_list.append(HemaTest())
    if patient.age >= 25 and patient.sex == 'F':
        patient.labtest_list.append(CytoTest())
    if patient.age >= 45 and patient.sex != 'F':
        patient.labtest_list.append(BiochemTest())        
  
    
def find_patient_by_id(patient_list, patient_id):
    """
    Patient is searched by their unique ID in the patient_list.
    
    Parameters
    ----------
    - patient_list : list
        List of Patient objects
    - patient_id : int
        The ID generated unique to the patient.

    Returns
    -------
        If id is found, returns the patient details.
        If not found, returns NONE. 
    """
    for patient in patient_list:
        if patient.id == patient_id:
            return patient
        
    
    
