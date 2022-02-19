# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import Counter
import requests
import csv
from requests import api
import random
border = "========================================="
api_key = "78ed65bbe878c5c5b37152e70a8ae591"
print(border)
city = input("What City do you live in: ")
print(border)
url = "https://api.chucknorris.io/jokes/random"
good_answer = [['N','n'], ['Y', 'y']]
rps=['WIN', 'TIE', 'LOSE']
activities = ['1. Norris Jokes', '2. Weather Channel']
cycle = 2

#for i in range(cycle):
    
print("\nLet's play a game! ")  
age = int(input("How old are you: ")) 
print(border)
answer = input("Would you Like to hear a chuck Norris Joke? Y or N ")

for x in range(age):
    if answer in good_answer[0]:
        print("Well that's too damn bad")
        request = requests.get(url)
        json = request.json()
        joke = json.get("value")
        print(joke)
        answer = input("Would you Like to hear a chuck Norris Joke? Y or N ")
    elif answer in good_answer[1]:
        num=int(input("How many Norris Jokes would you like to hear? "))
        for x in range(num):
            request = requests.get(url)
            json = request.json()
        # print(json)
            joke = json.get("value")
            print('\n',joke)
        print('\n',"You have just been Norrished!\n")
        print("What would you like to do next: ")
        print(border)
        for x in activities:
            print(x)
        choice=int(input("Enter the number of your choice here: "))
        if choice==1:
            num=int(input("How many Norris Jokes would you like to hear? "))
            for x in range(num):
                request = requests.get(url)
                json = request.json()
            # print(json)
                joke = json.get("value")
                print('\n',joke)
            print("\n","You have just been Norrished yet again!\n")
        elif choice==2:
            print("Would you like to choose the city you are from or enter a new city?")
            print("1. Keep Home City","\n", "2.Choose New City")
            citychoice=int(input("Choose the number for your choice: "))
            if citychoice==1:
                city=city
            elif citychoice==2:
                    city=input("Enter the city of your choice: ")
                    print('\n')
                    print(border)
            print("You have chosent to find out how the weather is for:",city)
            url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
            request = requests.get(url)
            json = request.json()
        # /* Prints Json file output */
           # print(json)

            description = json.get("weather")[0].get("description")
            tempmin = json.get("main").get("temp_min")
            tempmax = json.get("main").get("temp_max")
            tempfeel = json.get("main").get("feels_like")

            print ("Today's forecast is", description)
            print ("The temperature in "+city+" will be between", tempmin, " and", tempmax, "but it will feel like", tempfeel)
            break
        else:
            print("You didn't do it right, now you play Rock, Paper Scissors:")
            computer_choice = random.choice(['scissors', 'rock', 'paper'])
            user_choice = input('Do you want - rock, paper, or scissors?\n')
            
            if computer_choice == user_choice:
                print("The Computer chose",computer_choice,'so the game is a TIE')
            elif user_choice == 'rock' and computer_choice == 'scissors':
               playrps=print("The Computer chose",computer_choice,'so you WIN')
            elif user_choice == 'paper' and computer_choice == 'rock':
              playerrps=print("The Computer chose",computer_choice,'so you WIN')
            elif user_choice == 'scissors' and computer_choice == 'paper':
                playerrps=print("The Computer chose",computer_choice,'so you WIN') 
            else:
                playerrps=print("The Computer chose",computer_choice,'so you Lose')
                if playerrps==rps[0]:
                    break
                elif playerrps==[1]:
                    print("ahh mannnnn....so close")
                else:
                    print("Here we go again.....")
               
    else: 
        print("Since you can't follow directions, then you will see the weather forecast ")
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
        request = requests.get(url)
        json = request.json()
    # /* Prints Json file output */
       # print(json)

        description = json.get("weather")[0].get("description")
        tempmin = json.get("main").get("temp_min")
        tempmax = json.get("main").get("temp_max")
        tempfeel = json.get("main").get("feels_like")

        print ("Today's forecast is", description)
        print ("The temperature in "+city+" will be between", tempmin, " and", tempmax, "but it will feel like", tempfeel)

        break
