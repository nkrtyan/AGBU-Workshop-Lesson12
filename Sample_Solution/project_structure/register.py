from helper import Helper
import logging


class Register(Helper):

    def __init__(self, username, email, password, account_balance,user_role):
        super().__init__()
        self.username = username
        self.email =email
        self.password = password
        self.account_balance = account_balance
        self.user_role = user_role
    
    def check_validation(self):
            
        """username: required(8 symbol). 
            email: contains @ symbol.
            password: contains at least 1 uppercase, 1 digit(8 symbol)
            account_balance: Is numeric
            user_role: "admin", "non-admin"
            Validation message: In case of data issue, should give validation message of corresponding field
        """
        
        password_digit = 0
        password_upper = 0

        # validate username
        if len(self.username) != 8:
            logging.error(f"{self.username} username validation failed")
            return False
        # validate email
        if "@" not in self.email:
            logging.error(f"{self.email} email validation failed")
            return False
        # validate password
        if len(self.password) != 8:
            logging.error(f"{self.password} password validation failed")
            return False
        
        # check passord digit and uppercase
        for i in self.password:
            if i.isdigit():
                password_digit+=1
            elif i.isupper():
                password_upper+=1
        if password_digit>=1 and password_upper>=1:
            logging.info("Passowrd validation is correct")
        else:
            logging.error("Password doesnt contain correct digit and/or uppercase.")
            return False    
        
        # check account balance
        if not str(self.account_balance).isdigit():
            logging.error(f"{self.account_balance} account balance validation failed.")
            return False
        
        # check user_role
        if self.user_role.lower() not in ("admin", "non-admin"):
            logging.error(f"{self.user_role} user role validation failed.")
            return False
        
        logging.info("All data is correct.")        
        return True
    

    def register_user(self):
        """Open user.xlsx file, and write corresponding user data". Check data is correctly added to excel"""

        data = {
            "username": self.username, 
            "email": self.email, 
            "password": self.password, 
            "account_balance": self.account_balance, 
            "user_role": self.user_role, 
            "logged_in": False 
            }
        
        if self.check_validation():
            self.create_and_write_users_excel(data)
            logging.info(f"{self.username} is registered successfully")
        else:
            logging.error("Data Validation is failed")
       
    

