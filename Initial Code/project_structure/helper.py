import logging
import pandas as pd
import os
import shutil
class Helper:
    def __init__(self, dirname="Dataset", user_excel_name="users.xlsx", course_excel_name="courses.xlsx", logname="project.log"):

        self.dirname = dirname
        self.user_excel_name = user_excel_name
        self.course_excel_name = course_excel_name
        self.logname= logname
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename=self.logname,
            filemode="a",
            encoding="utf-8",
        )
        logging.info(f"The name of directory is {dirname}")
        logging.info(f"The name of users excel is {user_excel_name}")
        logging.info(f"The course excel name is {course_excel_name}")


    def create_dir(self):
        """Create dirname=<Dataset> folder, return folder path"""
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)
            logging.info(f"Directory {self.dirname} was created")
        else:
            logging.info(f"Directory {self.dirname} already exists")
        return os.path.abspath(self.dirname)
   
   
    def create_and_write_users_excel(self, excel_data):
        """ Create excel "users.xlsx", in case file doesn't exists
        Excel sheet should contain username, email, password, account_balance, user_role, logged_in columns
        """
        data = {
        "username": [excel_data["username"]],
        "email": [excel_data["email"]],
        "password": [excel_data["password"]],
        "account_balance": [excel_data["account_balance"]],
        "user_role": [excel_data["user_role"]],
        "logged_in": [excel_data["logged_in"]],
    }   
        file_path = os.path.join(self.dirname, self.user_excel_name)
        
        if not os.path.exists(file_path):
            df = pd.DataFrame(data)
            df.to_excel(file_path, index=False)
            logging.info(f"Excel file '{file_path}' created successfully.")
        else:
            source_df = pd.read_excel(file_path)
            new_df = pd.DataFrame(data)
            combined_df = pd.concat([source_df, new_df], ignore_index=True)
            combined_df.to_excel(file_path, index=False)
            logging.info(f"Excel file '{file_path}' updated with new data.")     


    def create_and_write_courses_excel(self, excel_data):
        """ Create or update the 'courses.xlsx' file with new data.
        Excel sheet should contain title, price, description, course_type (fundamental, advanced), course_buyer (empty).
        If the file already exists, new data will be appended.
        """
        
        # Construct the file path
        file_path = os.path.join(self.dirname, self.course_excel_name)

        # Define the columns for the courses
        columns = ['title', 'price', 'description', 'course_type', 'course_buyer']

        # Check if the file already exists
        if os.path.exists(file_path):
            # If file exists, read the current content into a DataFrame
            df_existing = pd.read_excel(file_path)

            # Create a DataFrame from the provided excel_data
            df_new = pd.DataFrame(excel_data, columns=columns)

            # Concatenate the existing data with the new data
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)

            # Write the combined DataFrame to the Excel file
            df_combined.to_excel(file_path, index=False)
            logging.info(f"Excel file '{self.course_excel_name}' updated successfully with new data.")
        else:
            
            df_new = pd.DataFrame(excel_data, columns=columns)
            df_new.to_excel(file_path, index=False)
            logging.info(f"Excel file '{self.course_excel_name}' created and data written successfully.")


    def read_from_excel(self, excel_file_path, column_name, column_value):
        df = pd.read_excel(excel_file_path)
        row = df.loc[df[column_name] == column_value]
        logging.info(f"column name is return {column_name}")
        return row


    def clean_up(self):
        confirm = input(f"Do you want to delete '{self.dirname}' and log file '{self.logname}'? (yes/no): ").strip().lower()

        if confirm == "yes":
            if os.path.exists(self.dirname):
                shutil.rmtree(self.dirname)
                print(f"Directory '{self.dirname}' deleted.")
            else:
                print(f"Directory '{self.dirname}' does not exist.")

            if os.path.exists(self.logname):
                print(f"Log file '{self.logname}' deleted.")
            else:
                print(f"Log file '{self.logname}' does not exist.")

            logging.shutdown()
            if os.path.exists(self.logname):
                os.remove(self.logname)
        else:
            print("Files and the directory are not deleted.")


