

Messenger Project
Description
Messenger is a Django-based project that allows administrators to send WhatsApp messages to students regarding their marks. The app processes two Excel files: one containing students' names, enrollment numbers, and marks, and another containing students' names, enrollment numbers, and phone numbers. It validates phone numbers based on Indian standards and generates a report of invalid phone numbers or missing students. The valid phone numbers receive a WhatsApp message with the student's marks.

Features
Upload two Excel files for marks and phone numbers.
Validate phone numbers to ensure they follow Indian standards.
Send personalized WhatsApp messages to valid students about their marks.
Generate an Excel report of students with invalid or missing phone numbers.

Usage
1. Upload Excel Files
Navigate to http://127.0.0.1:8000/messenger/upload/.
Upload two Excel files:
Marks File: Contains columns Student Name, Enrollment No, and Marks.
Phone Numbers File: Contains columns Student Name, Enrollment No, and Phone No.
2. Send WhatsApp Messages
Once the files are uploaded, the app:

Validates phone numbers based on Indian standards (10 digits, starting with 7, 8, or 9).
Sends WhatsApp messages to students with valid phone numbers about their marks.
Messages will be sent using WhatsApp Web via the pywhatkit library.

3. Generate Invalid Students Report
The app also generates an Excel report called invalid_students.xlsx containing:

Students with missing or invalid phone numbers.
Students present in one file but missing in the other (marks or phone numbers file).
4. Download the Invalid Students Excel
A separate button is available to generate and download the invalid_students.xlsx report if needed.

