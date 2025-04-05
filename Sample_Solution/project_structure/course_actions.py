from helper import Helper
import logging
import os
import pandas as pd


class Course_Actions(Helper):

    def add_course(self, title, price, description, course_type):
        """Add new course(row) in course.xlsx with title, price, description, course_type data"""
        data = {
                "title": title, 
                "price": price, 
                "description": description, 
                "course_type": course_type, 
                "course_buyer": "undefined"
                }
        
        self.create_and_write_courses_excel(data)
        logging.info(f"Corse with title {title} is created successfully")


    def edit_course(self, title, column, new_data):
        """Find course with title and update given data"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.course_excel)
        df = pd.read_excel(excel_path)
        df.loc[df["title"] == title, column] = new_data
        df.to_excel(excel_path, index=False)
        logging.info(f"Corse data {column} for title {title} changed to {new_data}")


    def delete_course(self, title):
        """Find course with title and delete from course.xlsx"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.course_excel)
        df = pd.read_excel(excel_path)
        df = df[df["title"] != title]
        df.to_excel(excel_path, index=False)
        logging.info(f"Corse {title} is deleted")
 
