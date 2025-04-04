import logging
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


