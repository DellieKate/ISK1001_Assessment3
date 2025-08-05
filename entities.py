from datetime import datetime
    
class Patient:
    """
    A class used to represent a Patient.

    ...
    Attributes
    ----------
    id : int
        The ID generated randomly from the reception module using numpy.
    full_name : str
        The full name of the patient.
    birthday : date
        The birth date of the patient.
    age : int
        The age calculated from the birthday.
    sex : str
        The sex of the patient.
    labtest_list : list
        The lists of labtests generated for the patient.
    """
        
    def __init__(self, id, full_name, birthday, sex):
        """Generates all the necessary attributes for the object Patient.

        Parameters:
        ----------
            id : int
                Patient ID.
            full_name : str
                Full Name of Patient.
            birthday : date
                Date of birth of Patient.
            sex : str
                Sex of Patient.    
        """
        
        self.id = id
        self.full_name = full_name
        self.birthday = birthday
        self.age = self.calculate_age(birthday)
        self.sex = sex
        self.labtest_list = []

    def calculate_age(self, birthday):
        """Calculates the current age of the patient from their birthday.

        Parameters: 
        -----------
        birthday : date
            The date of the patient.
    
        Returns:
        -------
        int 
            Age of the patient.  
        """
        
        return datetime.today().date().year - birthday.year
    
    def getDetails(self):
        """Returns a string of all details of the patient.
        
        Returns:
        -------
        str
            A string including the patient's ID, full name, age and sex.
        """
        
        return (f'Patient ID: {self.id} | Full name: {self.full_name} | Age: {self.age} | Sex: {self.sex}')
         
    def confirm_labtests(self, labtest_list):
        """Assigns a list of lab tests specific to the patient.
        
        Parameters
        ----------
        labtest_list : list
            A list of labtests allocated to the patient.
        """
        
        self.labtests = labtest_list
        

class LabTest:
    """
    A class used to represent a Labtest.
    
    Attributes
    ----------
    name : str
        Name of the lab test.
    description : str
        Description of the lab test, which can include normal ranges and results.

    """
    
    def __init__(self, name, description):
        """Generates a Labtest with a given name and description.

        Parameters
        ----------
        name : str
            Name of the lab test.
        
        description : str
            A brief description of the lab test.
        """
        
        self.name = name
        self.description = description
    
class BiochemTest(LabTest):
    """
    A class used to represent a BiochemTest (PSA) that inherits from LabTest.
    
    Attributes
    ----------
    upper_limit : float
        The upper limit value for the PSA test.
    """
    
    def __init__(self):
        """Initializes the Biochem Test with a predefined test name and description."""
        self.upper_limit = 2.5
        super().__init__('PSA', f'Normal PSA < {self.upper_limit} ng/mL')
            
class HemaTest(LabTest):
    """
    A class that represents a Hema (hematology) lab test, specifically blood sugar level (BSL). 
    It also inherits for Labtest.

    Attributes
    ----------
    lower_limit : float
        The lower limit value for the BSL test.
    upper_limit : float
        The upper limit value for the BSL test.
    """
    
    def __init__(self):
        """
        Initializes the Hema Test with a predefined test name and description.
        """
        self.lower_limit = 3.9
        self.upper_limit = 5.6
        super().__init__('BSL', f'Normal fasting blood glucose level is between {self.lower_limit} mmol/L and {self.upper_limit} mmol/l.')
               
class CytoTest(LabTest):
    """
    A class that represents a Cyto (Cytology) Test, specifically Papsmear.
    Also inherits from LabTest.
    """
    
    def __init__(self):
        """Initializes the CytoTest with a predefined test name and description."""
        super().__init__('Papsmear', 'Normal papsmear: No abnormal cells or HPV detected.')
    
class GenericTest(LabTest):
    """
    A class that represents a Generic Test.
    Also inherits from LabTest.
    
    Parameters
    ----------
    test_name : str
        The name of the generic test.
    """
    
    def __init__(self, test_name):
        """Initializes the Generic test with a test name."""
        super().__init__(test_name, f"{test_name} - General tests")