"""
create_pdf.py - PDF Report generator

This module is responsible for generating a PDF file which contains the patient's details and all their recommended lab tests.

Import
------
- FPDF from fpdf : library that is used to create PDF documents.
- Patient from entities : The Patient class that holds all relevant patient information.

Parameters
----------
- patient : Patient
    An instance of the Patient class, which contains patient's details and lab tests.
    
Output
------
- 'Patient_File.pdf' file will be created and saved in the current directory.
- Appropriate layout of the file was also created (Tabular form showing patient name, birthday, sex, lab tests, description, left-aligned).
"""

from fpdf import FPDF
from entities import Patient

def print(patient):
    pdf = FPDF()
    pdf.add_page ()
    pdf.set_font("Arial", size = 12)
    pdf.cell(0, 10, txt=(f'Patient: {patient.full_name}'), align="L", ln=True)
    pdf.cell(0, 10, txt=(f"Birthday: {patient.birthday}"), align="L", ln=True)
    pdf.cell(0, 10, txt=(f"Sex: {patient.sex}"), align="L", ln=True)
    pdf.set_x(20)
    pdf.cell(0, 10, txt="Recommended labs", align="L", ln=True)
    for lab_test in patient.labtest_list:
        pdf.set_x(25)
        pdf.cell(0, 10, txt=(f"{lab_test.description}"), align="L", ln=True)
    pdf.output("Patient_File.pdf")