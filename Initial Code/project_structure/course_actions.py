import os
import pandas as pd
import logging
from helper import Helper

class Course_Actions(Helper):
    
    def __init__(self, dirname, course_excel_name):
        super().__init__(dirname, course_excel_name)


    def add_course(self, title, price, description, course_type):
        """Add new course(row) in course.xlsx with title, price, description, course_type data"""        
        data = [{
            "title": title,
            "price": price,
            "description": description,
            "course_type": course_type,
        }]
        self.create_and_write_courses_excel(data)

    def edit_course(self, title, column, new_data):
        """Find course with title and update given data"""
        file_path = os.path.join(self.dirname, self.course_excel_name)
        if not os.path.exists(file_path):
            logging.error("Course file does not exist.")
            return
        df = pd.read_excel(file_path)
        df.loc[df['title'] == title, column] = new_data
        df.to_excel(file_path, index=False)
        logging.info(f"Course '{title}' updated: {column} = {new_data}")

    def delete_course(self, title):
        """Find course with title and delete from course.xlsx"""
        file_path = os.path.join(self.dirname, self.course_excel_name)
        if not os.path.exists(file_path):
            logging.error("Course file does not exist.")
            return
                
        df = pd.read_excel(file_path)
        index = df[df['title'] == title].index
        if df is None or df.empty or index.empty:
            logging.error(f"No course found with the title '{title}'.")
            return
        df = df.drop(index)
        df.to_excel(file_path, index=False)
        logging.info(f"Course '{title}' deleted.")