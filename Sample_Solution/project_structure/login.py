from helper import Helper
import logging
import os
import pandas as pd


class Login(Helper):

    def user_login(self, username, password):
        """When Log in is logged in make true"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.user_excel)
        df = pd.read_excel(excel_path)
        if username in df["username"].values and password in df["password"].values:
            df.loc[df["username"] == username, "logged_in"] = True
            df.to_excel(excel_path, index=False)
            logging.info(f"User {username} is logged in")
        else:
            logging.error("Incorrect username or password")
            print("Incorrect username or password")


    def user_logout(self, username):
        """When Log out is logged in make false"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.user_excel)
        df = pd.read_excel(excel_path)
        df.loc[df["username"] == username, "logged_in"] = False
        df.to_excel(excel_path, index=False)
        logging.info(f"User {username} is logged out")

