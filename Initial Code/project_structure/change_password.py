import os 
import pandas as pd

class Change_Password(Helper):

    def __init__(self, username, new_password):
        super().__init__()
        self.username = username
        self.new_password = new_password
        

    def check_password(self):
        if len(self.new_password) < 8:
            return False
        else:
            upper = 0
            digit = 0
            for i in self.new_password:
                if i.isupper():
                    upper += 1
                if i.isdigit():
                    digit += 1
            if upper>=1  and digit>=1:
                return False

            else:
                return True
        

    def change_password(self):
        if self.check_password() is True:
            excel_path = os.path.join(os.getcwd(), self.dirname, self.user_excel)
            if os.path.exists(excel_path):
                df = pd.read_excel(excel_path)
                print(df)
                df.loc[df["username"] == self.username, "password"] = self.new_password
                print(df)
                df.to_excel(excel_path, index=False)