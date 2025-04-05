import logging
from helper import Helper

class Register(Helper):

    def __init__(self, username, email, password, account_balance,user_role):
        super().__init__()
        self.username = username
        self.email = email
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
        if self.username == "" or len(self.username) < 8:
            return "Username should be at least 8 characters long."
        if "@" not in self.email:
            return "Email should contain '@' symbol."      
        if len(self.password) < 8:
            return "Password must be at least 8 characters long."
        else:
            has_uppercase = False
            has_digit = False
            for char in self.password:
                if char.isupper():
                    has_uppercase = True
                if char.isdigit():
                    has_digit = True
            if not has_uppercase or not has_digit:
                return "Password must contain at least 1 uppercase letter and 1 digit."
        logging.info("Validation successful for user: %s", self.username)
        return True

    
    def register_user(self):
        logging.info("Registration process started for user: %s", self.username)
        validation_result = self.check_validation()

        if validation_result == True:
            
            excel_data = {
                "username": self.username,
                "email": self.email,
                "password": self.password,
                "account_balance": self.account_balance,
                "user_role": self.user_role,
                "logged_in": False  
            }

            
            logging.info("Writing user data to Excel.")
            self.create_and_write_users_excel(excel_data=excel_data)

            logging.info("User registered successfully: %s", self.username)
            return "User registered successfully."
        else:
            logging.error("Validation failed for user: %s. Error: %s", self.username, validation_result)
            return validation_result 
    
       
