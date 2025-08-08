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
## **3. Log of recieved feedback**

### Entry #1: Feedback Received – Lack of Consent Mechanism

- **The specific documentation checked:**
`reception.py` (patient data entry workflow) and overall application data collection process.

- **When it was checked:**
2025-08-06

- **Who checked it:**
Ahmed Karakaci (external reviewer)

- **Any feedback provided:**
"There’s no step in the app to confirm that the patient has given consent before their personal and health information is entered. This could be a legal and ethical issue under privacy laws. A small fix would be to add a prompt to confirm consent before saving the record. I am not familiar with Australian privacy laws, so cannot make recommendations but they should be easy to find. Cross reference them with laws and frameworks that deal with the collection of senstitive personal data, of which, medical records and biographical details will among them."

- **Any actions to do based on the feedback provided:**
1. Create a **consent confirmation prompt** in the `add_patient` function of `reception.py` that requires the user to confirm the patient has been informed and has agreed to data collection.
2. Prevent record creation if consent is not confirmed.
3. Update `INSTRUCTIONS.md` and `README.md` to document the new consent step.
4. Add inline code comments explaining the legal basis (if necessary APP 3 and APP 5).
5. Link to the full analysis in `ETHICAL_SECURITY.md` for detailed legal and technical reasoning.

----

## **4. Log of provided feedback**

### **Entry #1: Internal Security & Documentation Review** [04/09/2025]
Contributers and reviewers: Dylan Esteban, Kate Mendoza, George Vasiliadis

#### Findings:
As this application handles sensitive patient data, we conducted an internal audit of the application's codebase to identify potential security vulnerabilities and ethical concerns. In doing so, we have identified several key ethical and security considerations based principally on the Australian Privacy Principles (APPs):

1. Data Security: The current version exports patient data to an unencrypted CSV file, posing a risk if the file is accessed by unauthorised users (violates APP 11).
2. Access Control: The application lacks a login system, meaning there is no way to verify if a user is an authorised doctor or receptionist.
3. Data Integrity: There is currently no feature to edit or correct a patient's details, which could lead to incorrect medical recommendations if a mistake is made during data entry (violates APP 10).
4. Lack of Consent Mechanism (APP 3, APP 5): There is currently no process for confirming patient consent prior to data entry. A prompt for user verification and consent is recommended.

To view view our analysis of these considerations with respect to industry standard legal and ethical frameworks, as well as our remediation strategies and action items, please refer to the [ETHICS_SECURITY.md](ETHICS_SECURITY.md)


### Entry #2: Feedback Given

- **The specific documentation checked:**
  `README.md`, `INSTALLATION.md`, `USAGE.md` (Instruction Guide), and Class/Function usage documentation.

- **When it was checked:**
  2025-08-06

- **Who checked it:**
  George Vasiliadis (from Team: Kate, Dylan, and George)

- **Any feedback provided:**
  1. The README, Installation, and Usage files are all structured well, with a logical flow that makes it easier to understand, especially for beginners. The way it’s put together makes it easy to grasp concepts and standards without being overwhelming.
  2. Mentioning using Command Prompt (CMD), not PowerShell, in the Installation Guide is a helpful detail for beginners who might confuse the two.
  3. In the installation steps, the `git clone` command is used, but some users might not know they need to have Git installed first. It could be worth mentioning Git in the System Requirements.
  4. Consider adding very basic/brief installation and usage instructions directly in the main README for quick reference, in addition to linking to the detailed guides.
  5. The examples given are succinct and easy to understand, especially the example for the `scores(hand)` class method.
  6. Consider adding more examples in the 'Class and Function Usage' documentation, particularly showing how classes and functions interact with each other to help visualise data flow.

- **Any actions to do based on the feedback provided:**
  1. Add a note in `INSTALLATION.md` clarifying the use of Command Prompt (CMD) instead of PowerShell for Windows users.
  2. Update the System Requirements section to mention that Git must be installed before running `git clone`.
  3. Add a short, basic installation and usage summary to the main `README.md` for quick reference.
  4. Review the 'Class and Function Usage' documentation and consider adding more examples showing interaction between classes and functions.











#### **Giving Feedback 1 Checklist: Group x [name 1, 2, 3]:**
----
##### **README Review**
- [ ] Clarity of Purpose:Are the project's purpose and features clearly explained?
- [ ] Installation Test: Are all dependencies listed in requirements.txt? Can I create a virtual environment, install the dependencies from requirements.txt, and have it work on the first try?
- [ ] Usage Instructions: Are the instructions on how to run and use the application clear enough for a first-time user? Do they work? Is there an example command?
- [ ] Project Structure: Is the explanation of the file structure clear? Do I know the purpose of each .py file from the description?

##### **Code Comment Review (pick one or two files):**
-  [ ] Function Docstrings: Does each function have a comment/docstring explaining its purpose, what arguments it takes (Args), and what it returns (Returns)?
-  [ ] Class Docstrings: If they use classes, is the purpose of each class explained?
-  [ ] Clarity of Comments: Are the comments easy to understand? Do they explain the why behind complex code, not just what the code does?
-  [ ] Imported Code: Is it clear why external libraries are being used? Is their source/purpose mentioned?

##### **Ethical & Security Review (using your Google Doc as a guide):**
- [ ] Data Handling: What kind of data does this app create, store, or process (e.g., user input, scores, configuration files)? Is this data handled appropriately? (e.g., Is a game's high score list stored in a way that can't be easily cheated?).
- [ ] Input Validation: How does the app handle incorrect or malicious user input? Does it crash, or does it handle the error gracefully? (e.g., What happens if you enter text where a number is expected?).
- [ ] Access & Permissions: Who is the intended user? Does the app have any features that should be restricted or protected in some way?
- [ ] Accountability & Consequences: What are the potential negative consequences if the app produces an incorrect result or fails? Is there a disclaimer or warning to the user about the app's limitations?
- [ ] Licensing & Attribution: Does the app use external code or assets? If so, is the license for that code compatible with their project, and is it properly attributed in the README?

----
### Feedback Session 2: [date]


#### Giving Feedback 2: Group x [name 1, 2, 3]
