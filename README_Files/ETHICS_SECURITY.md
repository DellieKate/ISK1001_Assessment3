<!-- Ethical and Security based considerations-->
# Introduction
This section provides a comprehensive overview of the ethical and security considerations that were addressed during the development of the project.

- basic idea: The proposed solutions for ethical/security issues we raise in the project can be detailed here and just briefly mentioned in the larger README file.

Current considerations:
#### **1. Unsecured CSV File Storage (APP 11)**: Patient data is stored in a plain-text CSV file, which presents risks of unauthorised access. Future versions should implement encryption or access controls.

#### **2. No Authentication or User Access Control (APP 6, APP 11)** The current CLI interface does not restrict access based on user roles (e.g., doctor or receptionist). Adding a basic login system would protect sensitive data and ensure only authorised personnel can access patient records.

#### **3. Inability to Edit Incorrect Records (APP 10)**: Data errors cannot currently be corrected, which may lead to medical or biographical inaccuracies. A mechanism for updating patient records is essential.

#### **4. Lack of Consent Mechanism (APP 3, APP 5)**: There is currently no process for confirming patient consent prior to data entry. A prompt for user verification and consent is recommended.



## Proposed Solutions

### Issue 1: Data Security – Insecure Storage of Sensitive Data

A critical security vulnerability involving the insecure storage of sensitive patient data was identified in the `reception.py` file. The `master_list` function takes all patient data—which includes sensitive and private health information—and writes it directly to an unencrypted plain-text CSV file: `patient_master_list.csv`. This exposes patient data to unauthorised access, as the file is readable by any user or process with access to its location.
---

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
