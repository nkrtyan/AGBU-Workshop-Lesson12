import logging
from helper import Helper
import pandas as pd
import os

# TODO, team 6 is notfinishedthis part, need to update
class Login(Helper):
    
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.excelpath = os.path.join(os.getcwd(), self.dirname, self.user_excel_name)
        # df = pd.users(columns= ["username","password"])
        # df.to_excel(self.excel_path, index=False)
    
    def user_login(self):
        df = pd.read_excel(self.excelpath)
        res = df["username"].values
        if self.username in df["username"].values:
            if df.loc[df["username"] == self.username, "password"].values[0] == self.password:
                df.loc[df["username"] == self.username, "logged_in"] = True
                df.to_excel(self.excelpath, index=False)
                logging.info(f"{self.username} logged in.")
                return True
            else:
                logging.warning("Incorrect password.")
        else:
            logging.warning("Username not found.")
        return False

    def user_logout(self, username):
        df = pd.read_excel(self.excelpath)
        if username in df["username"].values:
            df.loc[df["username"] == username, "logged_in"] = False
            df.to_excel(self.excelpath, index=False)
            logging.info(f"{username} logged out.")
            return True
        else:
            logging.warning("Username not found.")
            return False
        