import os
from helper import Helper
import pandas as pd
class Get_Courses(Helper):
    def get_course_data_by_title(self, column_value, column_name="title"):
        """Return row with full data from courses.xlsx by title"""
        file_path = os.path.join(self.dirname, self.course_excel_name)
        row = self.read_from_excel(file_path, column_name, column_value)
        return row
    
    def get_total_courses(self):
        """Get all rows from courses.xlsx and return total rows number"""
        file_path = os.path.join(self.dirname, self.course_excel_name)
        df = pd.read_excel(file_path)
        return len(df)
