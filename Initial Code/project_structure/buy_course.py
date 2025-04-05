import pandas as pd
from helper import Helper
import os
import logging

class Buy_Course(Helper):
    def __init__(self, course_name, username):
        super().__init__()
        self.course_name = course_name
        self.username = username

    def buy_course(self):
        path = os.path.join("dataset", "courses.xlsx")
        df = pd.read_excel(path)
        for index, row in df.iterrows():
            if row['title'] == self.course_name:
                df.at[index, 'username'] = self.username
                break
        logging.info(f"{self.username} added to {self.course_name}")
        df.to_excel(path, index=False)
        

data = Buy_Course("course3", "Da")
data.buy_course()


"""Logged in user find cours
        e with given course_name and add in the same line course_buyser"""