from admin import Admin_Module
from user import User_Module

import time
import os

Admin_Sign_Out = False
User_Sign_Out = False


if __name__ == "__main__" :

    while Admin_Sign_Out == False :
        Admin_Sign_Out = Admin_Module()


    while User_Sign_Out == False :
        User_Sign_Out = User_Module()
