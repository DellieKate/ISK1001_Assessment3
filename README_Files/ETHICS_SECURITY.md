<!-- Ethical and Security based considerations-->
# Introduction
This section provides a comprehensive overview of the ethical and security considerations that were addressed during the development of the project.

- basic idea: The proposed solutions for ethical/security issues we raise in the project can be detailed here and just briefly mentioned in the larger README file.

Current considerations:
#### **1. Unsecured CSV File Storage (APP 11)**: Patient data is stored in a plain-text CSV file, which presents risks of unauthorised access. Future versions should implement encryption or access controls.

#### **2. No Authentication or User Access Control (APP 6, APP 11)** The current CLI interface does not restrict access based on user roles (e.g., doctor or receptionist). Adding a basic login system would protect sensitive data and ensure only authorised personnel can access patient records.

#### **3. Inability to Edit Incorrect Records (APP 10)**: Data errors cannot currently be corrected, which may lead to medical or biographical inaccuracies. A mechanism for updating patient records is essential.

#### **4. Lack of Consent Mechanism (APP 3, APP 5)**: There is currently no process for confirming patient consent prior to data entry. A prompt for user verification and consent is recommended.
