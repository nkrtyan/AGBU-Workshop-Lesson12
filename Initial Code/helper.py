import logging
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
        pass

    def create_and_write_courses_excel(self, excel_data):
        """ Create excel "courses.xlsx", in case file doesn't exists
        Excel sheet should contain title, price, description, course_type(fundamental, advanced), course_buyser(empty) columns
        """
        pass


    def readRow(self, excel_file_path, column_name, column_value):
        df = pd.read_excel(excel_file_path)
        row = df.loc[df[column_name] == column_value]
        logging.info(f"column name is return {column_name}")
        return row

    def clean_up(self):
        """Clean  all data(directory with excel files and log file) created during code execution """
        # logging.shutdown(), before delete shutdown the logging file
        pass


