# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#imports for packages
from University.user_profile import user as up
import University.globals as globals
import University.validation as val
import Programs.activity_choice as activity_choice
import Programs.chucknorris
import Programs.weather
import Programs.stocks
import Programs.rocks_paper_scissors as rocks_paper_scissors
import Programs.admin as admin



#local variables
activities = ['1. Norris Jokes', '2. Weather Channel', '3. Review Stocks', '4. Rocks, Paper, Scissors', '5. Exit']
userconfirm=1
cycle=1
choice=1


#============================================
#Start Program
#============================================
print(globals.border)
print(globals.user_log_filename, globals.users_file)
print("Welcome To My World")
print(globals.border)

#set username to last user in logfile
pname=up.last_user(globals.user_log_filename)

#check user name to see if it is in the global user log
user_log=up.username_check(globals.users_file,pname)

#Validate user with validation program
userrecognized,user_id=val.user_validation(user_log,pname)

#Grab user information from user log
user_id,pname,lname,city,age=up.get_user_info(globals.users_file,user_id)

#Host start and introduction
activity_choice.host_start(userrecognized)

#Get user choice for activity
#while (choice != 5):
while True:
    choice=activity_choice.activity_start(globals.program_jsons)

    #Play Chuck Norris Jokes
    if choice==1:
        Programs.chucknorris.chucknorris_jokes(pname)

    #Review weather in different cities
    elif choice==2:
        Programs.weather.weather(city)

     #Review Stock data
    elif choice==3:
        Programs.stocks.stocks_choice(pname)

     #Play Rocks Papers Scissors
    elif choice==4:
        rocks_paper_scissors.rocks_paper_scis(globals.cname, pname, choice)

    #  #Exit program
    elif choice==5:
         break
       # answer='exit'

     #Enter Secret admin window
    elif choice==99:
       admin.admin_menu(user_id,pname,lname,city,age)

    # else:
    #     print(pname, "didn't do it right")
    #     Programs.weather.weather(city)

