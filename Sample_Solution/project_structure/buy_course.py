from helper import Helper
import logging
import os
import pandas as pd


class Buy_Course(Helper):
    def __init__(self, title, username):
        super(). __init__()
        self.username = username
        self.title = title

    def buy_course(self):
        """Logged in user find course with given course_name and add in the same line course_buyser"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.course_excel)
        df = pd.read_excel(excel_path)
        df.loc[df["title"] == self.title, "course_buyer"] = self.username
        df.to_excel(excel_path, index=False)
        logging.info(f"{self.username} bought course {self.title}")
