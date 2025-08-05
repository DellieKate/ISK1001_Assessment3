from entities import Patient, LabTest, BiochemTest, HemaTest, CytoTest, GenericTest
import doctor
from dateutil.parser import parse

def test_true_patient():
    birthday = parse('08/01/1981', dayfirst=True).date()
    patient = Patient ('1234','Kate',birthday,'F')
    doctor.recommend_labtest(patient)
    assert len(patient.labtest_list) == 6    
    print(patient.labtest_list)
      

