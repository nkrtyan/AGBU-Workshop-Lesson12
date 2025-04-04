class Register(Helper):

    def __init__(self, username, email, password, account_balance,user_role):
        super().__init__()
        pass
    
    def check_validation(self):
        """username: required(8 symbol). 
            email: contains @ symbol.
            password: contains at least 1 uppercase, 1 digit(8 symbol)
            account_balance: Is numeric
            user_role: "admin", "non-admin"
            Validation message: In case of data issue, should give validation message of corresponding field
        """ 
        pass


    def register_user(self):
        """Open user.xlsx file, and write corresponding user data"""
        pass
       
    

