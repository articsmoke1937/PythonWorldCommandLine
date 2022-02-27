import University.globals as globals
import requests
import json

#Function used to pull weather information
def weather(city):   
    citychoice=1
    while (citychoice != 3):
        api_key = "78ed65bbe878c5c5b37152e70a8ae591"
        print(globals.border)
        print("Would you like to choose the city you are from or enter a new city?")
        print(globals.border)
        print(" 1. Keep Home City\n","2. Choose New City\n","3. Exit")
        citychoice=int(input("Choose the number for your choice: "))
        if citychoice==1:
            city=city
        elif citychoice==2:
                city=input("Enter the city of your choice: ")
                print('\n')
                print(globals.border)
        else:
            break
        print("You have chosen to find out how the weather is for:",city)
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
        request = requests.get(url)
        #print(request)
        json = request.json()
        #print(json)
        description = json.get("weather")[0].get("description")
        tempmin = json.get("main").get("temp_min")
        tempmax = json.get("main").get("temp_max")
        tempfeel = json.get("main").get("feels_like")
        print ("Today's forecast is", description)
        print ("The temperature in "+city+" will be between", tempmin, " and", tempmax, "but it will feel like", tempfeel)
        print(globals.border)
        print("What would you like to do next")