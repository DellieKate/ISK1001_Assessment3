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