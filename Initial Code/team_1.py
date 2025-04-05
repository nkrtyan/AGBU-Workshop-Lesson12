import logging
import os


class Helper:
    def __init__(self, dirname="Dataset", user_excel_name="users.xlsx", course_excel_name="courses.xlsx"):
        self.dirname = dirname
        self.user_excel_name = user_excel_name
        self.course_excel_name = course_excel_name

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename="project.log",
            filemode="a",
            encoding="utf-8",
        )

        logging.info(f"The name of directory is {dirname}")
        logging.info(f"The name of users excel is {user_excel_name}")
        logging.info(f"The course excel name is {course_excel_name}")

    def create_dir(self):
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)
            logging.info(f"Directory {self.dirname} was created")
        else:
            logging.info(f"Directory {self.dirname} already exists")
        return os.path.abspath(self.dirname)


if __name__ == "__main__":
    helper = Helper()
    new_dir = helper.create_dir()
    



        

    
