## __*Python Assessment*__

# **Project Title**
KLM LabTest Advisor

## **Description**
An app that recommends clinical laboratory tests. For this version, only the following tests are supported: blood count, electrolytes, liver function test, cholesterol (lipids), sugar level, prostate antigen and papsmear.

### **Features**
1. Input basic patient details (reception interface). 
2. Look up patient’s file and recommends laboratory tests based on age and sex (doctor interface). 
3. Export patient’s record as PDF. 
4. Export list of patients into a CSV file. 

## **Installation**

*Prerequisite:*
- Python version 3.13

*Create a virtual environment (in bash terminal):*
``` 
python -m venv venv
source venv/bin/activate
```

*Install dependencies:*
```
pip install -r requirements.txt
```

## **Usage:**

1. Run project in terminal. 
```
python3 clinic.py
```
2. Select option in main menu.
3. In reception interface, select option to enter patient's details. (Note: A patient ID will be generated that will be used for patient look up.) Another option is to create a CSV file containing the lists of patients.
4. In doctor interface, patient is searched using ID. The system will display a report with an option to print as a PDF.

## **Project Structure:**

*Files:*
- `clinic.py` - Main file where options are provided to help navigate the whole app. 
- `reception.py` - Interface where user inputs patient’s details and creates CSV file. 
- `doctor.py`- Search particular patient using generated ID and displays data with recommended laboratory tests. Can print report as a PDF.
4. `entities.py` - Contains all entity definitions.
5. `create_pdf.py`- Shows methods to generate PDF.
6. `requirements.txt`- Lists required modules and packages to run the app.

## **License:**

Licensed under [Apache License 2.0](https://github.com/DellieKate/KateClinicPython/blob/main/LICENSE)

## **PIP-Licenses:**

Full detail in [Third party licenses](third_party_licenses.txt)

| Name            | Version     | License                                       |
|-----------------|-------------|-----------------------------------------------|
| Pygments        | 2.19.2      | BSD License                                   |
| fpdf            | 1.7.2       | GNU Lesser General Public License v3 (LGPLv3) |
| iniconfig       | 2.1.0       | MIT License                                   |
| numpy           | 2.2.6       | BSD License                                   |
| packaging       | 25.0        | Apache Software License; BSD License          |
| pluggy          | 1.6.0       | MIT License                                   |
| pytest          | 8.4.1       | MIT License                                   |
| python-dateutil | 2.9.0.post0 | Apache Software License; BSD License          |
| six             | 1.17.0      | MIT License                                   |

## **References:**
[W3schools](https://www.w3schools.com/python/default.asp)

[Canvas](https://edstem.org/au/courses/23675/lessons)

[Phyton](https://www.python.org/)
