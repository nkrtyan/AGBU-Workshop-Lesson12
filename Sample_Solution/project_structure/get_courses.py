
from helper import Helper
import logging
import pandas as pd
import os

class Get_Courses(Helper):

    def get_course_data_by_title(self, column_value, column_name="title"):
        """ Return row with full data from courses.xlsx by title"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.course_excel)
        result = self.read_from_excel(excel_path, column_name, column_value)
        logging.info(f"{column_value} is found.")
        return result

    def get_total_courses(self):
        """Get all rows from courses.xlsx and return total rows number"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.course_excel)
        df = pd.read_excel(excel_path)
        total = len(df)
        logging.info(f"Total number of courses are {total}")
        return total
