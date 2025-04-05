from project_structure.register import Register
from project_structure.login import Login
from project_structure.course_actions import Course_Actions
from project_structure.get_courses import Get_Courses
from project_structure.buy_course import Buy_Course
from project_structure.change_password import Change_Password
from project_structure.user import User
from helper import Helper
import logging

"""
1. Register two users: admin and non-admin.
2. Login with the admin user and add one fundamental course.
3. Login with the non-admin user, get the added course by title and buy it.
4. The non-admin user changes his/her password and login again, login should be successful
5. Admin user changes the non-admin user role to admin and delete that user.
6. User delete the course and get message course is deleted.
7. Admin user logout
"""


obj_helper = Helper()
obj_helper.create_dir()


# register admin and non-admin user
# getting admin user data
username_admin = "admin888"
email_admin ="admin@gmail.com"
password_admin = "Admin888"
account_balance_admin = "100"
user_role_admin = "admin"

# getting admin user data
username_non_admin = "nonadmin"
email_non_admin ="nonadmin@gmail.com"
password_non_admin = "Nonadmi8"
account_balance_non_admin = "200"
user_role_non_admin = "non-admin"

obj_admin = Register(username_admin, email_admin, password_admin, account_balance_admin,user_role_admin )
obj_nonadmin = Register(username_non_admin, email_non_admin, password_non_admin, account_balance_non_admin,user_role_non_admin)
obj_admin.register_user()
obj_nonadmin.register_user()

# login with the admin user
obj_login = Login()
obj_login.user_login(username_admin, password_admin)

# add one fundamental course
obj_user = User(username_admin)
user_role = obj_user.check_user_role()
if user_role is True:
    obj_course_actions = Course_Actions()
    obj_course_actions.add_course("New_course", 180, "Description of the course", "fundamental")
else:
    logging.error("You don't have permission to add a course.")
        

# login with non-admin user
obj_login.user_login(username_non_admin, password_non_admin)

# get_added_course by title
obj_get_course = Get_Courses()
obj_get_course.get_course_data_by_title(column_value="New_course")

# buy course
obj_buy_course = Buy_Course(username_non_admin, "New_course")
obj_buy_course.buy_course()

# change password
obj_change_pass = Change_Password(username_non_admin, "Blabla88")
obj_change_pass.change_password()

# login with new password
obj_login.user_login(username_non_admin, "Blabla88")

# delete course
obj_course_actions.delete_course("New_course")


# change_role
obj_user.change_role(user_role_non_admin, "admin")

# delete user
obj_user.delete_user(username_non_admin)
obj_login.user_logout(username_admin)

# clenup
cleanup = input("Would you like to clean unnessasry files, Y/N: ")
if cleanup.lower()=="y":
    obj_helper.clean_up()
