# **Feedback Log**

## **1. Purpose of this Document**
This document tracks all feedback given to and received from peer groups throughout the development of the KLM LabTest Advisor project. Its purpose is to provide a transparent and comprehensive record of our collaborative review process, ensuring our final documentation is clear, useful, and professionally robust.


## **2. Scope of Feedback**

Our feedback process is guided by two core principles, directly aligned with the assessment rubric:

#### **Pillar 1: General Documentation Quality & Usefulness:**
- This focuses on the practical utility of the documentation. Feedback in this category addresses whether the documentation provides a new developer or user with all the necessary information to understand, install, and run the application effectively.

#### **Pillar 2: Ethical & Security Considerations:**
- This focuses on professional responsibility. Feedback in this category addresses whether the project has adequately identified and considered the potential risks, ethical implications, and security vulnerabilities associated with its design and data handling.

----
## **3. Log of Received Feedback**


### Entry #1 of Given Feedback: Internal Security Audit & Documentation Review [04/09/2025]
Contributers and reviewers: Dylan Esteban, Kate Mendoza, George Vasiliadis

#### Findings:
As this application handles sensitive patient data, we conducted an internal audit of the application's codebase to identify potential security vulnerabilities and ethical concerns. In doing so, we have identified several key ethical and security considerations based principally on the Australian Privacy Principles (APPs):

1. Data Security: The current version exports patient data to an unencrypted CSV file, posing a risk if the file is accessed by unauthorised users (violates APP 11).
2. Access Control: The application lacks a login system, meaning there is no way to verify if a user is an authorised doctor or receptionist.
3. Data Integrity: There is currently no feature to edit or correct a patient's details, which could lead to incorrect medical recommendations if a mistake is made during data entry (violates APP 10).
4. Lack of Consent Mechanism (APP 3, APP 5): There is currently no process for confirming patient consent prior to data entry. A prompt for user verification and consent is recommended.

To view view our analysis of these considerations with respect to industry standard legal and ethical frameworks, as well as our remediation strategies and action items, please refer to the [ETHICS_SECURITY.md](ETHICS_SECURITY.md).


### Entry #2: Feedback Received – Lack of Consent Mechanism

**The specific documentation checked:**
`README.md`, `INSTALLATION.md`, `reception.py` (patient data entry workflow) and overall application data collection process.

**When it was checked:**
2025-08-06

**Who checked it:**
Ahmed Karakaci (external reviewer)

**Any feedback provided:**
"There is currently no step in the application to confirm that a patient has provided informed consent before their personal and health information is entered into the system. This presents a potential legal and ethical risk under privacy and health data protection laws. A straightforward improvement would be to add a mandatory prompt in the data entry workflow requiring the user (e.g., receptionist) to confirm that the patient has been informed about how their data will be collected, stored, and used, and that they have agreed to this. The record should not be saved unless consent is confirmed. While I am not familiar with the specific details of Australian privacy legislation, relevant requirements should be easy to locate. These frameworks set out obligations for obtaining consent, providing privacy notices, and ensuring transparency in the handling of sensitive health data and are designed to help companies and IT professionals build and develop safe, secure, and responsible software"

**Any actions to do based on the feedback provided:**
1. Create a **consent confirmation prompt** in the `add_patient` function of `reception.py` that requires the user to confirm the patient has been informed and has agreed to data collection.
2. Prevent record creation if consent is not confirmed.
3. Update `INSTRUCTIONS.md` and `README.md` to document the new consent step.
4. Add inline code comments explaining the legal basis (if necessary APP 3 and APP 5).
5. Link to the full analysis in `ETHICAL_SECURITY.md` for detailed legal and technical reasoning.

--

### Entry #3 Feedback Received - General Documentation Feedback

**The specific documentation checked:**
`README.md` / `INSTALLATION.md` / `INSTRUCTIONS.md`

**When was it checked:**
2025-08-08

**Who checked it:**
Billy Vasiliadis (external reviewer, programmer)

**Any feedback provided:**

`README.md`:
- Needs disclaimers about the system being advisory-only and needing a doctor to oversee. (Ethical)
- The feature list could be better structured to highlight the features.  Some dot points would be good. (Usefulness)
- Patients should be explicitly told how their data is being handled and used. (Ethical)

`INSTALLATION.md`:
- Mention how to deactivate the virtual environment when done (Usefulness)
- Including an uninstall guide would help. (Usefulness)

`INSTRUCTIONS.md`:
- Formatting can be improved so that sections can be broken up and have headings i.e. "Getting Started", "Adding Patients", etc. (Usefulness)
- Inclusion of disclaimers about this being on a test project so far, and to not use real patient info/data should be mentioned. (Ethical)

**Any actions to do based on the feedback provided:**
`README.md`:
- Disclaimer to be added at the start of the README.md to highlight the importance of it and make sure readers see it.
- Feature list to be re-formatted into a list of features, with corresponding brief descriptions, and a summary above to make readers aware of what the section contains.
- A Privacy section to be written up within the README.md file, that contains informations and disclaimers, in particular mentioning 'Data Handling' use.

`INSTALLATION.md`:
- Extra guided steps regarding 'deactivation' and 'uninstallation' to be appended to the Installation Guide.

`INSTRUCTIONS.md`:
- Document to be re-formatted to accomodate for better readability.  Sections will be labelled: 'Getting Started', 'Adding Patients', 'Determining Lab Tests', 'Generating Reports'.
- Disclaimer stating users not to use real patient info/data to be added to the start of the INSTRUCTIONS.md file, as well as the main README.md file, to highlight the importance of it and make sure readers see it.

----

### Entry #4: Feedback Received – Repository Structure, Documentation, and Code Clarity

**The specific documentation checked:**
`README.md`, `INSTALLATION.md` (proposed rename to `Set_up.md`), repository folder structure, and `clinic.py`.

**When it was checked:**
2025-08-08

**Who checked it:**
Paul Augustine (external reviewer)

**Any feedback provided:**
1. **Repository structure**
   - The current repository layout should follow a layered structure as outlined in the Python documentation (http://docs.python-guide.org/writing/structure).
     Recommended example:
       - **Docs/**
         - `ReadMe.md`
         - Other documentation files referenced by the README
       - **Source/**
         - All code files (e.g. `commands.py`)
       - **Data/Output/**
         - Sample files (e.g. `.csv`) linked in README

2. **README File**
   - Provide links to the official websites of all third-party modules used in the project.
   - Rename `Installation.md` to `Set_up.md`.
   - Rename “Usage/Instructions” to “Usage”.

3. **Installation (Set_up.md) File**
   - Expand the “create” and “activate” instructions.
     - Clearly explain what is being created (e.g. a virtual environment) and what is being activated.

4. **Code in `clinic.py`**
   - Include a comment or explanation describing the purpose of the main `while` loop.

- **Any actions to do based on the feedback provided:**
1. Reorganise the repository into a layered structure (`Docs/`, `Source/`, `Data/Output/`) and update all file references in the README accordingly.
2. Add hyperlinks in the README to the official documentation for all third-party modules listed in `requirements.txt`.
3. (Optional) Rename `Installation.md` to `Set_up.md` for consistency with feedback.
4. Rename “Usage/Instructions” section in the README to “Usage”.
5. Expand the “create” and “activate” steps in the installation guide to explain what a virtual environment is and what activation does.
6. Add a descriptive comment above the main `while` loop in `clinic.py` explaining its role in controlling the application’s main menu and handling user input.







## **4. Log of Provided Feedback**

### Entry #1 of Given Feedback:

**The specific documentation checked:**
  `README.md`, `INSTALLATION.md`, `USAGE.md` (Instruction Guide), and Class/Function usage documentation.

**When it was checked:**
  2025-08-06

**Who checked it:**
  George Vasiliadis (from Team: Kate, Dylan, and George)

**Any feedback provided:**
  1. The README, Installation, and Usage files are all structured well, with a logical flow that makes it easier to understand, especially for beginners. The way it’s put together makes it easy to grasp concepts and standards without being overwhelming.
  2. Mentioning using Command Prompt (CMD), not PowerShell, in the Installation Guide is a helpful detail for beginners who might confuse the two.
  3. In the installation steps, the `git clone` command is used, but some users might not know they need to have Git installed first. It could be worth mentioning Git in the System Requirements.
  4. Consider adding very basic/brief installation and usage instructions directly in the main README for quick reference, in addition to linking to the detailed guides.
  5. The examples given are succinct and easy to understand, especially the example for the `scores(hand)` class method.
  6. Consider adding more examples in the 'Class and Function Usage' documentation, particularly showing how classes and functions interact with each other to help visualise data flow.

**Any actions to do based on the feedback provided:**
  1. Add a note in `INSTALLATION.md` clarifying the use of Command Prompt (CMD) instead of PowerShell for Windows users.
  2. Update the System Requirements section to mention that Git must be installed before running `git clone`.
  3. Add a short, basic installation and usage summary to the main `README.md` for quick reference.
  4. Review the 'Class and Function Usage' documentation and consider adding more examples showing interaction between classes and functions.

--
### Entry #2 of Given Feedback: Kate's
