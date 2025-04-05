from helper import Helper
import logging
import os
import pandas as pd


class User(Helper):
    def __init__(self, username):
        super(). __init__()
        self.username = username

    def check_user_role(self):
        """Check user role and return True in case of admin, False in case of non-admin"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.user_excel)
        df = pd.read_excel(excel_path)
        role = df.loc[df['username'] == self.username, 'user_role'].values[0]
        logging.info(f"User role is {role}")
        if role.lower() == "admin":
            return True
        else:
            return False
        
    def change_role(self, changed_username, new_role):
        """Change given username role"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.user_excel)
        df = pd.read_excel(excel_path)
        df.loc[df["username"] == changed_username, "user_role"] = new_role
        df.to_excel(excel_path, index=False)
        logging.info(f"{self.username} role is changed to {new_role}")
       
         

    def delete_user(self, deleted_user):
        """ Delete given username"""
        excel_path = os.path.join(os.getcwd(), self.dirname, self.user_excel)
        df = pd.read_excel(excel_path)
        df = df[df["username"] != deleted_user]
        df.to_excel(excel_path, index=False)
        logging.info(f"User {deleted_user} is deleted")



