import os
import logging
import pandas as pd
import shutil

class Helper:
    def __init__(self, dirname="Dataset", user_excel_name="users.xlsx", course_excel_name="courses.xlsx"):
        self.dirname = dirname
        self.user_excel = user_excel_name
        self.course_excel = course_excel_name
        self.log_file_name = "project.log"

        logging.basicConfig(
                filename=self.log_file_name,
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
                filemode="a"
                )

    def create_dir(self):
        """Create dirname=<Dataset> folder, return folder path"""
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)
            logging.info(f"{self.dirname} is created.")
        else:
            logging.info(f"{self.dirname} is already exitst.")
        return os.path.join(os.getcwd(),self.dirname) 
    
    def create_and_write_users_excel(self, excel_data=None):
        """ Create excel "users.xlsx", in case file doesn't exists
        Excel sheet should contain username, email, password, account_balance, user_role, logged_in columns
        write file path to "paths.py" file as variable_name = value"""

        data = {
                "username": [excel_data["username"]],
                "email": [excel_data["email"]],
                "password": [excel_data["password"]],
                "account_balance": [excel_data["account_balance"]],
                "user_role": [excel_data["user_role"]],
                "logged_in": [excel_data["logged_in"]]
                }
        
        users_file_path = os.path.join(self.dirname, self.user_excel)
        if not os.path.exists(users_file_path):
            df = pd.DataFrame(data)
            df.to_excel(users_file_path, index=False)
            logging.info(f"{users_file_path} excel is created")
        else:
            existing_data = pd.read_excel(users_file_path)
            updated_data = pd.concat([existing_data, pd.DataFrame(data)], ignore_index=True)
            updated_data.to_excel(users_file_path, index=False)
            logging.info(f"{users_file_path} excel is updated")
        return users_file_path


    def create_and_write_courses_excel(self, excel_data=None):
        """ Create excel "courses.xlsx", in case file doesn't exists
        Excel sheet should contain title, price, description, course_type(fundamental, advanced), course_buyser(empty) columns
        write file path to "paths.py" file as variable_name = value"""

        data = {"title": [excel_data["title"]],
                "price": [excel_data["price"]],
                "description": [excel_data["description"]],
                "course_type": [excel_data["course_type"]],
                "course_buyer": [excel_data["course_buyer"]]}
        courses_file_path = os.path.join(self.dirname, self.course_excel)
        if not os.path.exists(courses_file_path):
            df = pd.DataFrame(data)
            df.to_excel(courses_file_path, index=False)
            logging.info(f"{courses_file_path} excel is created")
        else:
            existing_data = pd.read_excel(courses_file_path)
            updated_data = pd.concat([existing_data, pd.DataFrame(data)], ignore_index=True)
            updated_data.to_excel(courses_file_path, index=False)
            logging.info(f"{courses_file_path} excel is updated")
        return courses_file_path


    def read_from_excel(self, excel_file_path, column_name, column_value):
        """Read row data from corresponding excel by column_value name. Get File Path from paths.py 
        FYI: Get row based on column name. Example
        df = pandas.read_excel("data.xlsx")
        row = df.loc[df["Name"]] == "Alice"
        """
        df = pd.read_excel(excel_file_path)
        row = df.loc[df[column_name] == column_value]
        logging.info(f"{column_value} was found.")
        return row


    def clean_up(self):
        """Clean  all data(directory, files) created during code execution """
        if os.path.exists(self.dirname):
            shutil.rmtree(self.dirname)
            logging.info(f"Folder '{self.dirname}' and its contents have been removed.")
        else:
            logging.warning(f"Folder '{self.dirname}' does not exist, skipping clean-up.")
        
        if os.path.exists(self.log_file_name):
            logging.shutdown()
            os.remove(self.log_file_name)



