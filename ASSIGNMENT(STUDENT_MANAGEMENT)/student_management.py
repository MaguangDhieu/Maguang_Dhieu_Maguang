import csv
import json
import logging
import os
import re
from datetime import datetime
from typing import List, Dict, Optional

# CUSTOM EXCEPTION CLASSES

class StudentManagementException(Exception):
    """Base custom exception for all student management system errors."""
    pass
class StudentNotFoundError(StudentManagementException):
    """Raised when a student record cannot be found."""
    pass
class InvalidInputError(StudentManagementException):
    """Raised when user input is invalid or malformed."""
    pass
class FileOperationError(StudentManagementException):
    """Raised when CSV or JSON file operations fail."""
    pass
# LOGGING CONFIGURATION
def setup_logging():
    log_filename = "student_system.log"
    
    # Create logger
    logger = logging.getLogger("StudentManagement")
    logger.setLevel(logging.DEBUG)
    
    # Clear existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # File handler - logs everything to file
    file_handler = logging.FileHandler(log_filename, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler - logs only INFO and above
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter for consistent log format
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


# Initialize logger globally
logger = setup_logging()

# STUDENT RECORD MANAGEMENT CLASS
class StudentRecordManager:
       
    def __init__(self, csv_file: str = "students.csv", json_file: str = "students.json"):
        
        self.csv_file = csv_file
        self.json_file = json_file
        self.csv_headers = ['Registration_Number', 'First_Name', 'Last_Name', 'Email', 'Phone']
        
        logger.info(f"StudentRecordManager initialized with CSV: {csv_file}, JSON: {json_file}")
        
        # Initialize files if they don't exist
        self._initialize_files()
    
    def _initialize_files(self):
        try:
            # Initialize CSV file
            if not os.path.exists(self.csv_file):
                with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=self.csv_headers)
                    writer.writeheader()
                logger.info(f"Created new CSV file: {self.csv_file}")
            
            # Initialize JSON file
            if not os.path.exists(self.json_file):
                with open(self.json_file, 'w', encoding='utf-8') as f:
                    json.dump({}, f, indent=2)
                logger.info(f"Created new JSON file: {self.json_file}")
        
        except IOError as e:
            logger.error(f"File initialization failed: {str(e)}")
            raise FileOperationError(f"Could not initialize files: {str(e)}")
    
    def validate_registration_number(self, reg_num: str) -> bool:
        if not reg_num:
            return False

        normalized_reg_num = reg_num.strip()
        if not normalized_reg_num:
            return False

        return bool(re.fullmatch(r"[A-Za-z0-9]+(?:/[A-Za-z0-9]+)*", normalized_reg_num))
    
    def validate_email(self, email: str) -> bool:
       
        return '@' in email and '.' in email.split('@')[-1]
    
    def validate_phone(self, phone: str) -> bool:

        digits_only = ''.join(c for c in phone if c.isdigit())
        return len(digits_only) >= 7
    
    def student_exists(self, reg_num: str) -> bool:

        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['Registration_Number'] == reg_num:
                        return True
            return False
        except IOError as e:
            logger.error(f"Error checking student existence: {str(e)}")
            raise FileOperationError(f"Could not read from {self.csv_file}")
    
    def add_student(self, reg_num: str, first_name: str, last_name: str, 
                   email: str, phone: str, address: str, 
                   program: str, gpa: float) -> bool:
       
        try:
            reg_num = reg_num.strip()

            # Validate all inputs
            if not self.validate_registration_number(reg_num):
                raise InvalidInputError("Invalid registration number format (use letters, numbers, and / separators)")
            if not first_name or not last_name:
                raise InvalidInputError("First and last names cannot be empty")
            if not self.validate_email(email):
                raise InvalidInputError("Invalid email format (must contain @ and .)")
            if not self.validate_phone(phone):
                raise InvalidInputError("Invalid phone number (minimum 7 digits required)")
            
            # Check if GPA is valid
            try:
                gpa_float = float(gpa)
                if gpa_float < 0 or gpa_float > 4.0:
                    raise InvalidInputError("GPA must be between 0.0 and 4.0")
            except ValueError:
                raise InvalidInputError("GPA must be a valid number")
            
            # Check if student already exists
            if self.student_exists(reg_num):
                raise StudentManagementException(
                    f"Student with registration number {reg_num} already exists"
                )
            
            # Add to CSV file
            csv_record = {
                'Registration_Number': reg_num,
                'First_Name': first_name,
                'Last_Name': last_name,
                'Email': email,
                'Phone': phone
            }
            
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.csv_headers)
                writer.writerow(csv_record)
            
            # Add to JSON file
            with open(self.json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            json_data[reg_num] = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'address': address,
                'program': program,
                'gpa': gpa_float,
                'date_added': datetime.now().isoformat()
            }
            
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Student added successfully: {reg_num} - {first_name} {last_name}")
            return True
        
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"File operation error while adding student: {str(e)}")
            raise FileOperationError(f"Could not save student record: {str(e)}")
    
    def view_all_students(self) -> List[Dict]:
       
        try:
            students = []
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['Registration_Number']:  # Skip empty rows
                        students.append(row)
            
            logger.info(f"Retrieved all students. Total count: {len(students)}")
            return students
        
        except IOError as e:
            logger.error(f"Error reading CSV file: {str(e)}")
            raise FileOperationError(f"Could not read from {self.csv_file}")
    
    def search_student(self, reg_num: str) -> Dict:
       
        try:
            # Get CSV data
            csv_data = None
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['Registration_Number'] == reg_num:
                        csv_data = row
                        break
            
            if not csv_data:
                logger.warning(f"Search failed: Student {reg_num} not found")
                raise StudentNotFoundError(f"No student found with registration number: {reg_num}")
            
            # Get detailed data from JSON
            with open(self.json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            if reg_num not in json_data:
                logger.error(f"Inconsistency: {reg_num} in CSV but not in JSON")
                raise FileOperationError("Data inconsistency between CSV and JSON files")
            
            detailed_info = json_data[reg_num]
            combined_record = {**csv_data, **detailed_info}
            
            logger.info(f"Student searched successfully: {reg_num}")
            return combined_record
        
        except IOError as e:
            logger.error(f"File operation error during search: {str(e)}")
            raise FileOperationError(f"Could not search student records: {str(e)}")
    
    def update_student(self, reg_num: str, **kwargs) -> bool:
       
        try:
            # Check if student exists
            if not self.student_exists(reg_num):
                raise StudentNotFoundError(f"No student found with registration number: {reg_num}")
            
            # Validate provided fields
            if 'email' in kwargs and not self.validate_email(kwargs['email']):
                raise InvalidInputError("Invalid email format")
            if 'phone' in kwargs and not self.validate_phone(kwargs['phone']):
                raise InvalidInputError("Invalid phone number")
            if 'gpa' in kwargs:
                try:
                    gpa = float(kwargs['gpa'])
                    if gpa < 0 or gpa > 4.0:
                        raise InvalidInputError("GPA must be between 0.0 and 4.0")
                    kwargs['gpa'] = gpa
                except ValueError:
                    raise InvalidInputError("GPA must be a valid number")
            
            # Update CSV file
            csv_headers_to_update = {k: v for k, v in kwargs.items() 
                                     if k in self.csv_headers}
            
            if csv_headers_to_update:
                students = self.view_all_students()
                for student in students:
                    if student['Registration_Number'] == reg_num:
                        student.update(csv_headers_to_update)
                
                with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=self.csv_headers)
                    writer.writeheader()
                    writer.writerows(students)
            
            # Update JSON file
            json_headers_to_update = {k: v for k, v in kwargs.items() 
                                      if k not in self.csv_headers or k == 'email' or k == 'phone'}
            
            if json_headers_to_update:
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                if reg_num in json_data:
                    json_data[reg_num].update(json_headers_to_update)
                    json_data[reg_num]['date_modified'] = datetime.now().isoformat()
                
                with open(self.json_file, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Student updated successfully: {reg_num} with fields {list(kwargs.keys())}")
            return True
        
        except IOError as e:
            logger.error(f"File operation error during update: {str(e)}")
            raise FileOperationError(f"Could not update student record: {str(e)}")
    
    def delete_student(self, reg_num: str) -> bool:
        try:
            # Check if student exists
            if not self.student_exists(reg_num):
                raise StudentNotFoundError(f"No student found with registration number: {reg_num}")
            
            # Delete from CSV
            students = self.view_all_students()
            students = [s for s in students if s['Registration_Number'] != reg_num]
            
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.csv_headers)
                writer.writeheader()
                writer.writerows(students)
            
            # Delete from JSON
            with open(self.json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            if reg_num in json_data:
                del json_data[reg_num]
            
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Student deleted successfully: {reg_num}")
            return True
        
        except IOError as e:
            logger.error(f"File operation error during deletion: {str(e)}")
            raise FileOperationError(f"Could not delete student record: {str(e)}")

# USER INTERFACE - MENU SYSTEM
def display_menu():
    print("\n" + "="*60)
    print("STUDENT RECORD MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Add a new student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Update student details")
    print("5. Delete a student record")
    print("6. Exit")
    print("="*60)


def get_valid_input(prompt: str, validation_func=None) -> str:
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise InvalidInputError("Input cannot be empty")
            if validation_func and not validation_func(user_input):
                raise InvalidInputError("Invalid input format")
            return user_input
        except InvalidInputError as e:
            print(f"Error: {str(e)}")
            logger.warning(f"Invalid input received: {str(e)}")


def add_student_menu(manager: StudentRecordManager):
    try:
        print("\n--- Add New Student ---")
        
        reg_num = get_valid_input(
            "Registration Number: ",
            manager.validate_registration_number
        )
        
        first_name = get_valid_input("First Name: ")
        last_name = get_valid_input("Last Name: ")
        
        email = get_valid_input(
            "Email Address: ",
            manager.validate_email
        )
        
        phone = get_valid_input(
            "Phone Number: ",
            manager.validate_phone
        )
        
        address = get_valid_input("Address: ")
        program = get_valid_input("Program of Study: ")
        
        gpa = get_valid_input("GPA (0.0-4.0): ")
        
        manager.add_student(reg_num, first_name, last_name, email, phone, 
                           address, program, gpa)
        print("Student added successfully!")
        logger.info(f"User successfully added student: {reg_num}")
    
    except (InvalidInputError, StudentManagementException, FileOperationError) as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error in add_student_menu: {str(e)}")


def view_all_students_menu(manager: StudentRecordManager):
    try:
        students = manager.view_all_students()
        
        if not students:
            print("\nNo students in the system yet.")
            return
        
        print("\n" + "="*100)
        print(f"{'Reg. Number':<12} {'First Name':<15} {'Last Name':<15} {'Email':<25} {'Phone':<15}")
        print("="*100)
        
        for student in students:
            print(f"{student['Registration_Number']:<12} {student['First_Name']:<15} "
                  f"{student['Last_Name']:<15} {student['Email']:<25} {student['Phone']:<15}")
        
        print("="*100)
        print(f"Total Students: {len(students)}")
        logger.info(f"User viewed all students. Total: {len(students)}")
    
    except FileOperationError as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error in view_all_students_menu: {str(e)}")


def search_student_menu(manager: StudentRecordManager):
    try:
        reg_num = get_valid_input("Enter Registration Number to search: ")
        student = manager.search_student(reg_num)
        
        print("\n" + "="*60)
        print("STUDENT DETAILS")
        print("="*60)
        for key, value in student.items():
            # Format key for display
            display_key = key.replace('_', ' ').title()
            print(f"{display_key:<20}: {value}")
        print("="*60)
        logger.info(f"User searched for student: {reg_num}")
    
    except StudentNotFoundError as e:
        print(f"Error: {str(e)}")
        logger.warning(f"Search failed - Student not found: {str(e)}")
    except FileOperationError as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error in search_student_menu: {str(e)}")

def update_student_menu(manager: StudentRecordManager):
    try:
        reg_num = get_valid_input("Enter Registration Number to update: ")
        
        # Verify student exists
        manager.search_student(reg_num)
        
        print("\nWhat would you like to update?")
        print("1. First Name")
        print("2. Last Name")
        print("3. Email")
        print("4. Phone")
        print("5. Address")
        print("6. Program")
        print("7. GPA")
        print("8. Back to main menu")
        
        choice = input("Select option: ").strip()
        
        updates = {}
        
        if choice == '1':
            updates['first_name'] = get_valid_input("New First Name: ")
        elif choice == '2':
            updates['last_name'] = get_valid_input("New Last Name: ")
        elif choice == '3':
            updates['email'] = get_valid_input("New Email: ", manager.validate_email)
        elif choice == '4':
            updates['phone'] = get_valid_input("New Phone: ", manager.validate_phone)
        elif choice == '5':
            updates['address'] = get_valid_input("New Address: ")
        elif choice == '6':
            updates['program'] = get_valid_input("New Program: ")
        elif choice == '7':
            updates['gpa'] = get_valid_input("New GPA: ")
        elif choice == '8':
            return
        else:
            print("Invalid option")
            logger.warning("Invalid update option selected")
            return
        
        if updates:
            manager.update_student(reg_num, **updates)
            print("Student updated successfully!")
            logger.info(f"User updated student {reg_num}: {list(updates.keys())}")
    
    except (StudentNotFoundError, InvalidInputError, FileOperationError) as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error in update_student_menu: {str(e)}")


def delete_student_menu(manager: StudentRecordManager):
    try:
        reg_num = get_valid_input("Enter Registration Number to delete: ")
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete student {reg_num}? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            manager.delete_student(reg_num)
            print("Student deleted successfully!")
            logger.info(f"User deleted student: {reg_num}")
        else:
            print("Deletion cancelled")
            logger.info(f"User cancelled deletion for student: {reg_num}")
    
    except StudentNotFoundError as e:
        print(f"Error: {str(e)}")
        logger.warning(f"Deletion failed - Student not found: {str(e)}")
    except FileOperationError as e:
        print(f"Error: {str(e)}")
        logger.error(f"Error in delete_student_menu: {str(e)}")

# MAIN PROGRAM
def main():
    print("\n Initializing Student Record Management System...")
    try:
        # Initialize manager
        manager = StudentRecordManager()
        logger.info("Application started successfully")
        
        while True:
            try:
                display_menu()
                choice = input("Enter your choice (1-6): ").strip()
                
                if choice == '1':
                    add_student_menu(manager)
                elif choice == '2':
                    view_all_students_menu(manager)
                elif choice == '3':
                    search_student_menu(manager)
                elif choice == '4':
                    update_student_menu(manager)
                elif choice == '5':
                    delete_student_menu(manager)
                elif choice == '6':
                    print("\nThank you for using Student Management System. Goodbye!")
                    logger.info("Application closed by user")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
                    logger.warning("Invalid menu choice selected")
            
            except KeyboardInterrupt:
                print("\n\nApplication interrupted by user")
                logger.warning("Application interrupted (Ctrl+C)")
                break
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                logger.error(f"Unexpected error in main loop: {str(e)}")
    
    except Exception as e:
        print(f" Failed to initialize application: {str(e)}")
        logger.critical(f"Application initialization failed: {str(e)}")
    
    finally:
        print("\n--- System Shutdown ---")
        logger.info("Application terminated")


if __name__ == "__main__":
    main()
