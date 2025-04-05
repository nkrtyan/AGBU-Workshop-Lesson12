from helper import Helper
import logging
import os
import pandas as pd


class Change_Password(Helper):

    def __init__(self, username, new_password):
        super(). __init__()
        self.username = username
        self.new_password = new_password
        
        
    def check_password(self):
        """Check given password validation"""
        password_digit = 0
        password_upper = 0

         # validate password
        if len(self.new_password) != 8:
            logging.error(f"{self.new_password} password validation failed")
            return False
        
        # check passord digit and uppercase
        for i in self.new_password:
            if i.isdigit():
                password_digit+=1
            elif i.isupper():
                password_upper+=1
        if password_digit>=1 and password_upper>=1:
            logging.info("Passowrd validation is correct")
            return True
        else:
            logging.error("Password doesnt contain correct digit and/or uppercase.")
            return False 

    def change_password(self):
        """Logged in user navigate to users.xlsx, find logged in user row and update with new given password"""
        if self.check_password() is True:
            excel_path = os.path.join(os.getcwd(), self.dirname, self.user_excel)
            df = pd.read_excel(excel_path)
            df.loc[df["username"] == self.username, "password"] = self.new_password
            df.to_excel(excel_path, index=False)
            logging.info(f"{self.username} password is changed")
            


