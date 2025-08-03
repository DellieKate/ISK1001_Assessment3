from datetime import datetime
    
class Patient:
    """
    A class used to represent a Patient
    
    ...
    Attributes
    ----------
    id : int
        the id generated randomly from the reception module using numpy
    full_name : str
        the full name of the patient
    birthday : date
        the birthday extracted from parse
    age : int
        the age computed from birthday
    sex : str
        the sex of the patient
    
    """
        
    def __init__(self, id, full_name, birthday, sex):
        self.id = id
        self.full_name = full_name
        self.birthday = birthday
        self.age = self.calculate_age(birthday)
        self.sex = sex
        self.labtest_list = []

    def calculate_age(self, birthday):
       return datetime.today().date().year - birthday.year
    """
    Calculates the current age of the patient.

    Uses:
        datetime.now() from the datetime module.
    
    Returns:
        datetime: Current local date and time.
    """

    def getDetails(self):
        return (f'Patient ID: {self.id} | Full name: {self.full_name} | Age: {self.age} | Sex: {self.sex}')
        """Returns all the details of patient in the self object."""
    
    def confirm_labtests(self, labtest_list):
        self.labtests = labtest_list
        """Defines the list of labtests specifically for the patient."""

class LabTest:
    """
    A class used to represent a Labtest
    
    ...
    Attributes
    ----------
    name : str
        name of the labtest
    description : str
        description of the labtest including some results
    
    """
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
class BiochemTest(LabTest):
    """
    A class used to represent a BiochemTest that inherits the attributes of LabTest (argument)
    
    ...
    Attributes
    ----------
    upper_limit : float
        includes the upper limit value of the test
    __init__ 
        inherits the attribute of the parent class
    
    """
    
    def __init__(self):
        self.upper_limit = 2.5
        super().__init__('PSA', f'Normal PSA < {self.upper_limit} ng/mL')
            
class HemaTest(LabTest):
    def __init__(self):
        self.lower_limit = 3.9
        self.upper_limit = 5.6
        super().__init__('BSL', f'Normal fasting blood glucose level is between {self.lower_limit} mmol/L and {self.upper_limit} mmol/l.')
               
class CytoTest(LabTest):
    def __init__(self):
        super().__init__('Papsmear', 'Normal papsmear: No abnormal cells or HPV detected.')
    
class GenericTest(LabTest):
    def __init__(self, test_name):
        super().__init__(test_name, f"{test_name} - General tests")