import logging
import os
import pandas as pd

class Helper:
    def __init__(self, dirname="Dataset", user_excel_name="users.xlsx", course_excel_name="courses.xlsx"):
        logging.basicConfig()
        pass

    def create_dir(self):
        """Create dirname=<Dataset> folder, return folder path"""
        pass
    
    
    def create_and_write_users_excel(self, excel_data):
        """ Create excel "users.xlsx", in case file doesn't exists
        Excel sheet should contain username, email, password, account_balance, user_role, logged_in columns
        """
        
        data = {
            "username": excel_data["username"],
            "email": excel_data["email"],
            "password": excel_data["password"],
            "account_balance": excel_data["account_balance"],
            "user_role": excel_data["user_role"],
            "logged_in": excel_data["logged_in"],
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
        """ Create excel "courses.xlsx", in case file doesn't exists
        Excel sheet should contain title, price, description, course_type(fundamental, advanced), course_buyser(empty) columns
        """
        pass


    def read_from_excel(self, excel_file_path, column_name, column_value):
        """Read row data from corresponding excel by column_value name. 
        FYI: Get row based on column name. Example
        df = pandas.read_excel("data.xlsx")
        row = df.loc[df["Name"]] == "Alice"
        """
        pass


    def clean_up(self):
        """Clean  all data(directory with excel files and log file) created during code execution """
        # logging.shutdown(), before delete shutdown the logging file
        pass
