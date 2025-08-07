# KLM LabTest Advisor

***Find out what clinical lab test you need!***

[![License](https://img.shields.io/badge/License-Apache-red)](https://www.apache.org/licenses/LICENSE-2.0)
![License](https://img.shields.io/badge/License-MIT-blue)
![License](https://img.shields.io/badge/License-BSD-%23AB2B28)
![License](https://img.shields.io/badge/License-GNU-%23A42E2B)

## Table of Contents

▶ [About](#about)
▶ [Installation](#installation)
▶ [Usage](#usage)
▶ [Ethical & Security-based](#ethical--security-based)
▶ [Licenses](#licenses)
▶ [Acknowledgements](#acknowledgements)

## About

<!-- The Purpose of the Application -->
Welcome to KLM LabTest Advisor app.  This app determinines clinical laboratory tests for medical patients.

Designed and developed to be used in a small clinical setting, primarily by Doctors and staff (i.e. Reception, Nurses, etc.), this app offers convenience and organisation by automating the process, helping save time and energy.  Since small medical practices can be a chaotic place, keeping things organised and not having to rush during and between patients can be difficult.  With this app, things can be kept running smoothly, allowing those who work in them to provide better care and treatment given the increase of available time.

## Features

<!-- The Features of the Application -->
The app's main feature is the automation of recommending pathology tests.  To achieve this, users can select between 'Reception' and 'Doctor' interfaces.  In the 'Reception' section, patient data can be added, stored, and exported.  When exported, a separate file is created, having the previously added info stored in CSV format.  Acting as database, when new patient info is added, then subsequently exported, the file updates, rather than a completely new file being made.  To distinguish between records, a unique patient ID is automatically created and assigned to each patient, allowing users to assuredly identify each record.  From here, users can then enter the 'Doctor' section of the app, where they will be prompted to enter a patient ID, and in return be provided with a list of recommended lab/pathology tests, which is based off an automatic analyses conducted by the software.  Currently, only the following tests recommendations are offered: Blood Count, Electrolytes, Liver Function Test, Cholesterol (Lipids), Sugar Level, Prostate Antigen, and Papsmear.  Additionally, users can print the patient reports if they wish to.  This is done by the app generating and exporting a pdf file for each individual record.

## Installation

Below is a quick quick installation guide for WSL/Linux users.  For a more comprehensive installation guide, see: [Installation Guide](README_Files/INSTALLATION.md).

`user@user-desktop:~$ git clone git@github.com:DellieKate/KateClinicPython.git` *Clone repo locally*

`user@user-desktop:~/KateClinicPython$ python3 -m venv venv` *Create virtual environment*

`user@user-desktop:~/KateClinicPython$ source venv/bin/activate` *Activate virtual environment*

`user@user-desktop:~/KateClinicPython$ pip install -r requirements.txt` *Install required dependencies*

## Usage

Below is a brief summary of instructions on how to use the app.  For more detailed instructions, see: [Instruction Guide](README_Files/INSTRUCTIONS.md)

1. Run project in terminal.
```
python3 clinic.py
```
2. Select option in main menu.
3. In reception interface, select option to enter patient's details. (Note: A patient ID will be generated that will be used for patient look up.) Another option is to create a CSV file containing the lists of patients.
4. In doctor interface, patient is searched using ID. The system will display a report with an option to print as a PDF.

## Ethical & Security-based Considerations

As this application handles sensitive medical data, several ethical and privacy-related issues were identified and addressed in alignment with the **Australian Privacy Principles (APPs)**.

During an initial team security audit and review of the codebase, the following vulnerabilities were identified:

#### **1. Unsecured CSV File Storage (APP 11)**:
Patient data is stored in a plain-text CSV file, which presents risks of unauthorised access. Future versions should implement encryption or access controls.

#### **2. No Authentication or User Access Control (APP 6, APP 11):**
The current CLI interface does not restrict access based on user roles (e.g., doctor or receptionist). Adding a basic login system would protect sensitive data and ensure only authorised personnel can access patient records.

#### **3. Inability to Edit Incorrect Records (APP 10)**:
Data errors cannot currently be corrected, which may lead to medical or biographical inaccuracies. A mechanism for updating patient records is essential.

#### **4. Lack of Consent Mechanism (APP 3, APP 5)**:
There is currently no process for confirming patient consent prior to data entry. A prompt for user verification and consent is recommended.

More detail and elaboration of these issues and proposed solutions can be found in our project's internal documentation and read [HERE](README_Files/ETHICS_SECURITY.md).

## Licenses

This app is licensed under [Apache License 2.0](https://github.com/DellieKate/KateClinicPython/blob/main/LICENSE)

Below is a condensed table of third party modules, their licenses, and the versions used.  For more detail about their licenses, see: [Third Party Modules](third_party_licenses.txt)

<!-- - Make link to third party licenses work. -->

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


## Acknowledgements

* [W3schools](https://www.w3schools.com/python/default.asp)

* [Canvas](https://edstem.org/au/courses/23675/lessons)

* [Python](https://www.python.org/)

* [Make a README](https://www.makeareadme.com/)

* [readmine](https://github.com/mhucka/readmine?tab=readme-ov-file#getting-help)

* [APP(Quick Reference)](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-quick-reference)
