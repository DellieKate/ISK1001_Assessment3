from entities import Patient, LabTest, BiochemTest, HemaTest, CytoTest, GenericTest
import create_pdf

def doctor_main_menu(patient_list = []):
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

def recommend_labtest(patient):
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
    for patient in patient_list:
        if patient.id == patient_id:
            return patient
        
    
    
