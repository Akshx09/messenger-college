import pandas as pd
import re
import pywhatkit as kit

def is_valid_phone_number(phone_number):
    """
    Check if the provided phone number is a valid Indian phone number.
    Indian phone numbers are 10 digits long and start with 7, 8, or 9.
    """
    pattern = re.compile(r'^[789]\d{9}$')
    return bool(pattern.match(phone_number))

def create_excel_files():
    # Sample data for students' marks
    marks_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Enrollment No': ['EN001', 'EN002', 'EN003', 'EN004', 'EN005'],
        'Marks': [85, 90, 78, 88, 92]
    }
    
    # Sample data for students' phone numbers
    phone_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Eve', 'Frank'],
        'Enrollment No': ['EN001', 'EN002', 'EN003', 'EN005', 'EN006'],
        'Phone No': ['7879397605', '7879397605', '7879397605', '7879397605', 'invalid_number']
    }
    
    # Create dataframes
    marks_df = pd.DataFrame(marks_data)
    phone_df = pd.DataFrame(phone_data)
    
    # Save to Excel files
    marks_df.to_excel('marks.xlsx', index=False)
    phone_df.to_excel('phones.xlsx', index=False)
    
    return marks_df, phone_df

def find_invalid_students(marks_df, phone_df):
    # Merge DataFrames on Name and Enrollment No
    merged_df = pd.merge(marks_df, phone_df, on=['Name', 'Enrollment No'], how='outer', indicator=True)

    # Check for invalid phone numbers
    merged_df['Valid Phone'] = merged_df['Phone No'].apply(lambda x: is_valid_phone_number(str(x)) if pd.notnull(x) else False)

    # Filter students present only in one file or with invalid phone numbers
    invalid_students = merged_df[(merged_df['_merge'] != 'both') | (~merged_df['Valid Phone'])]

    # Select relevant columns
    result_df = invalid_students[['Name', 'Enrollment No', 'Phone No', '_merge']]

    # Save result to Excel
    result_df.to_excel('invalid_students.xlsx', index=False)

    return result_df

def send_whatsapp_messages(marks_df, phone_df):
    # Merge to get phone numbers of students
    merged_df = pd.merge(marks_df, phone_df, on=['Name', 'Enrollment No'], how='inner')

    for index, row in merged_df.iterrows():
        message = f"Hello {row['Name']}, your marks are {row['Marks']}."
        phone_number = row['Phone No']
        try:
            kit.sendwhatmsg_instantly(f"+91{phone_number}", message)
            print(f"Message sent to {row['Name']} at {phone_number}.")
        except Exception as e:
            print(f"Failed to send message to {row['Name']} at {phone_number}: {str(e)}")

if __name__ == "__main__":
    # Create Excel files
    marks_df, phone_df = create_excel_files()
    
    # Find invalid students and generate the output Excel
    invalid_students_df = find_invalid_students(marks_df, phone_df)
    print("Invalid students exported to 'invalid_students.xlsx'.")

    # Send WhatsApp messages to valid students
    send_whatsapp_messages(marks_df, phone_df)
    
