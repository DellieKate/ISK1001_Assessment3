<!-- Ethical and Security based considerations-->

# Ethical & Security Considerations

## Introduction

This document presents an analysis and reflection on recieved feedback items from our project’s development process, focusing on ethical, privacy, and security considerations.

From the full set of feedback logs recorded in `feedback_log.md`, **four key issues** were chosen for deeper examination. These were selected because they represent significant ethical and security-related challenges identified during the project, either through internal audits or external reviews.

For each issue, we:
- Summarise the feedback received
- Analyse its ethical and legal implications, referencing relevant frameworks and standards, and
- Outline action items to be considered or taken in future iterations of the application

The aim of this document is to demonstrate how feedback was used not only to improve the technical quality of the application, but also to ensure compliance with professional, ethical, and legal industry standards.


## Proposed Solutions

### Issue 1: Data Security – Insecure Storage of Sensitive Data

A critical security vulnerability involving the insecure storage of sensitive patient data was identified in the `reception.py` file. The `master_list` function takes all patient data which includes sensitive and private health information and writes it directly to an unencrypted plain-text CSV file: `patient_master_list.csv`. This exposes patient data to unauthorised access, as the file is readable by any user or process with access to its location.


**Legal & Ethical Considerations**

With respect to the relevant legal literature, this risk is likely in violation of APP 11 (Security of personal information) as  it does not take reasonable steps to protect the data from unauthorised access and use. APP 11 states that compliance requires taking reasonable steps to protect personal information it holds from misuse, interference, modification or disclosure, and also from unauthorised access. This vulnerability is also in non-compliance with the AHPRA Code of Conduct which demands awareness and compliance with privacy requirements that pertain to the holding of health records, preventing unauthorised access as well as maintaining the privacy, protection, and integrity of electronic records. The Department of Health’s Private Policy Act (2020) delineates what they understand to constitute ‘reasonable steps’, and lists “password protection for electronic files” as a central key security control to be implemented; something the initial design of KLM LabTest Advisor CLI application lacked. Consequently, our remediation plan involves a solution to mirror industry standard best practices by refactoring the relevant code to create a password-protected encrypted file.

---

### Solution: Implement Encryption or Access Controls

Future versions must implement, at minimum, **encryption** for the contents of the exported csv file. This can be done using Python’s built-in [`cryptography`](https://cryptography.io/en/latest/) library.

We propose:

- Using **Fernet symmetric encryption** for data export.
- Prompting the user for a password to generate the encryption key via a key derivation function.

---

### Action Items – Remediation Plan

1. **Codebase Changes**
   - Install the `cryptography` library.
   - Implement a key derivation function from a user-supplied password.
   - Refactor `master_list` in `reception.py` to:
     - Prompt for password.
     - Write an **encrypted** file with the `.csv.encrypted` extension.

2. **Documentation Updates**
   - Update `INSTALLATION.md`:
     - Add instructions to install the `cryptography` library via `pip`.
   - Update `INSTRUCTIONS.md`:
     - Explain new password prompt for the export function.
     - Clarify that the export file is now an encrypted `.csv.encrypted`.
   - Update `requirements.txt`:
     - Include `cryptography`.
   - Update `README.md`:
     - Reflect the secure export feature in:
       - **Features**
       - **Ethical Considerations**

## Issue 2: Data Security – Insecure Storage of Sensitive Data

An important procedural and compliance gap was identified in the patient data entry workflow of **KLM LabTest Advisor** by both an external reviewer (see entry #2 in `feedback_log.md`) and during the initial group application audit. Both reviews reported that, presently, there is no mechanism to confirm that patient consent has been obtained before their sensitive health information is collected and stored.

The `add_patient` function in `reception.py` allows the entry of personal and sensitive information (including full name, date of birth, and sex) without any verification step to ensure that the patient has been informed of, and agreed to, the collection and intended use of their data.

This omission creates potential compliance risks under the **Australian Privacy Principles (APPs)**:

- **APP 3 – Collection of solicited personal information**: Requires that an entity must not collect sensitive information (including health information) unless the individual has consented and the information is reasonably necessary for the entity’s functions or activities.
- **APP 5 – Notification of the collection of personal information**: Requires that, at or before the time of collection, the individual is notified of the purpose of collection, how the information will be used, and to whom it may be disclosed.

These obligations for health practitioners are reinforced by the **AHPRA Code of Conduct**, which requires that they obtain informed consent before the collection or use of patient information and data, and that they comply with privacy laws when handling health records.

Likewise, according to the **Department of Health Privacy Policy’s** practices (p. 9, 2020), where reasonable, individuals must be issued with a privacy notice articulating the purpose, intended use, and disclosure of their personal information.

The current application design does not provide any such notice or confirmation step, meaning it fails to support users (e.g., receptionists, doctors) in meeting these professional and legal obligations.

---

## Solution:
Implementation of a **mandatory consent confirmation mechanism** in the patient data entry workflow (for example, adding it to `add_patient()` in `reception.py`) that includes error handling.

## Remediation Plan & Action Items:

### Implementation details:
- **Consent Prompt:** Before saving a new patient record, display a prompt:
  `"Has the patient given informed consent to collect their information and been provided with the necessary privacy notice? (y/n)"`
- **Abort on “n” / No Consent:** If the user selects “n”, abort record creation and return to the main menu.
- **Privacy Notice Display:** Store the privacy notice text in a separate `.txt` file or `config.py` constant, and display it in the terminal so the receptionist can read it to the patient.
- **Consent Logging:** Append a record to `consent_log.csv` containing:
  - Patient ID
  - Date and time of consent
  - Staff username or ID
- **Future Iterations:** Consider integrating the consent log into a secure database for better auditability, such as if the application were utilised in a proper medical setting.
- **Error Handling:** Validate input so only “y” or “n” is accepted when prompting the receptionist.


## Reflection – Documentation Disclaimers, Privacy Transparency, and Data Handling

### Overview of Feedback
On **2025-08-08**, we received an external review and feedback from **Billy Vasiliadis**, who reviewed our `README.md`, `INSTALLATION.md`, and `INSTRUCTIONS.md` files. His feedback included both **usability improvements** as well as **ethical considerations**.

**Concerning usability**, he suggested the following improvements:
- Structuring the feature list in the README for clarity.
- Adding clear deactivation and uninstallation instructions to the Installation Guide.
- Improving formatting and section headings in the Instructions Guide for better readability.

While much of his feedback relates to documentation clarity and usability, several points have **direct ethical and legal implications**:

---

### Informed Use & Avoiding Misrepresentation
- Without a disclaimer, there is a risk that users may interpret the application’s recommendations as definitive medical advice.
- This could lead to misuse of the system, potentially resulting in harm if decisions are made without professional oversight.
- From an ethical standpoint, this relates to **duty of care** and **avoiding harm**. This is aligned with the **ACM Code of Ethics Principle 1.2: "Avoid harm"**, which refers to negative consequences, especially those that are both significant and unjust.

---

### Transparency in Data Handling
- **APP 5** (Notification of the collection of personal information) requires that individuals are informed about how their data will be stored, disclosed, and used.
- Even though this is a test project, failing to include a privacy statement could be seen as a lack of transparency, which undermines trust and fails to mirror best practice for handling sensitive health data.
- This is a relevant aspect to consider in this new project when reviewing the codebase and documentation.

---

### Preventing Unauthorised Use of Real Data
- Including a disclaimer to not use real patient data is both an ethical safeguard and a legal precaution.
- This aligns with **APP 3** (Collection of solicited personal information), which prohibits collecting sensitive information without consent and a legitimate purpose.
- Additionally, this aligns with the **AHPRA Code of Conduct**, which requires health practitioners to protect patient confidentiality and only collect information when and if necessary.

---

## Remediation Plan

Based on this feedback, we crafted the following action items to be carried out and/or considered for future iterations of the application:

1.  `README.md`
- Add a disclaimer at the top stating:
  - The system is for educational and demonstration purposes only.
  - It is not a substitute for professional medical advice.
  - All recommendations must be reviewed by a qualified doctor – ensuring professional oversight.
- Reformat the **Features** section into a bullet-point list with brief descriptions for each feature.
- Add a **Privacy & Data Handling** section explaining:
  - How the application processes patient data.
  - That no data is transmitted externally and that users should not enter real patient data.

2.  `INSTALLATION.md`
- Update to include instructions for deactivating the virtual environment.
- Update to include an uninstallation guide for removing the application as well as its dependencies.

3.  `INSTRUCTIONS.md`
- Reformat with clear section headings:
  - "Getting Started"
  - "Adding Patients"
  - "Determining Lab Tests"
  - "Generating Reports"
- Add a disclaimer at the start reiterating that:
  - The system is for demonstration purposes only.
  - Users must not enter real patient data.

---

Furthermore, by adding clear disclaimers and privacy statements, we:
- Reduce the risk of misuse or misinterpretation of the system’s outputs.
- Model best practice for transparency in handling sensitive data.
- Align our documentation with **APP 3**, **APP 5**, the **AHPRA Code of Conduct**, as well as covering **Principle 1.2: “Avoid harm”** of the **ACM’s Code of Ethics**.
