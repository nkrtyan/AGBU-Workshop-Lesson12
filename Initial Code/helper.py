import logging
import os
import pandas as pd
import shutil






class Helper:
    def __init__(self, dirname="Dataset", user_excel_name="users.xlsx", course_excel_name="courses.xlsx"):
        logging.basicConfig()
        


    def create_dir(self, dirname):
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


    def read_from_excel(self, excel_file_path, column_name, column_value):
        """Read row data from corresponding excel by column_value name. 
        FYI: Get row based on column name. Example
        df = pandas.read_excel("data.xlsx")
        row = df.loc[df["Name"]] == "Alice"
        """
        pass

    
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
        # logging.shutdown(), before delete shutdown the logging file



     


