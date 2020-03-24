"""File:ChuKetterer_12.1.py
Name: Joi Chu-Ketterer
Date: 5/30/19
Course: DSC510 - Introduction to Programming
Desc: This program calculates retrieves temperatures using 'OpenWeatherApp' API based on where the user's input for location.
Usage: The user will indicate if they want to find the weather using a city name, or a zipcode and country code. They will then enter the relevant information.
"""

#these are all the packages I will refer to throughout this program
import requests
import json
import string
import sys

#I decided to use classes to distinguish between celsius and fahrenheit. Since OWA API defaults to Kelvins, I just applied the appropriate math to convert to the user's desired temperature unit
#I created the new variable 'location', because I noticed if the city input is 90020, OWA retrieves information for Caltanissetta, Italy (rather than Los Angeles, CA). To eliminate confusion, I extracted the location data directly from OWA to display to the user
class celsiusUnit():
    def __init__(self):
        pass

    def cityname_celsius(self):
        cityName = input('\n' "What is your city? ")

        try:
            api = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID=858a38b4f15ecdcacc524948ba8f2d3f'.format(cityName)
            source = requests.get(api)
            data = json.loads(source.text)
            temperature = data['main']['temp']
            location = data['name']
            print( '\n' "                     The temperature in", string.capwords(location), "is", int(temperature-273.15),'degrees Celsius')

        except:
            print("Sorry, we were unable to retrieve that city.")

    def zipcode_celsius(self):
        zipCode = input('\n' "What is your zip code? ")
        countryCode = input("What is your country code? ")

        try:
            api = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&APPID=858a38b4f15ecdcacc524948ba8f2d3f'.format(zipCode,countryCode)
            source = requests.get(api)
            data = json.loads(source.text)
            temperature = data['main']['temp']
            location = data['name']
            print('\n''                     The temperature in', string.capwords(location), 'is', int(temperature-273.15), 'degrees Celsius')

        except:
            print("Sorry, we were unable to retrieve that zip code or country code.")


class fahrenheitUnit():
    def __init__(self):
        pass

    def cityname_fahrenheit(self):
        cityName = input('\n' "What is your city? ")
        try:
            api = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID=858a38b4f15ecdcacc524948ba8f2d3f'.format(cityName)
            source = requests.get(api)
            data = json.loads(source.text)
            temperature = data['main']['temp']
            location = data['name']
            print('\n' "                     The temperature in", string.capwords(location), "is", int((temperature-273.15)*(9/5)+32),'degrees Fahrenheit.')

        except:
            print("Sorry, we were unable to retrieve that city.")

    def zipcode_fahrenheit(self):
        zipCode = input('\n' "What is your zip code? ")
        countryCode = input("What is your country code? ")
        try:
            api = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&APPID=858a38b4f15ecdcacc524948ba8f2d3f'.format(zipCode,countryCode)
            source = requests.get(api)
            data = json.loads(source.text)
            temperature = data['main']['temp']
            location = data['name']
            print('\n' "                     The temperature in ", string.capwords(location), " is ", int((temperature-273.15)*(9/5)+32),' degrees Fahrenheit.', sep='')

        except:
            print("Sorry, we were unable to retrieve that zip code or country code.")

#since my formatting for the welcome and goodbye messages were chunky, I wanted to keep them isolated in their own functions
def welcomeMessage():

    welcome = "Welcome to Joi's Weather App!"
    print('-'*len(welcome))
    print(welcome)
    print('-'*len(welcome))

def goodbyeMessage():

    goodbye = "Thank you for you using Joi's Weather App. Please come again!"
    print('\n')
    print("-"*len(goodbye))
    print(goodbye)
    print("-"*len(goodbye))

#this is the main program that takes the user's initial requests, and gives the user the ability to toggle between celsius and fahrenheit
#since the user has to choose between celsius and fahrenheit first, then between city or zipcode I did not notice any issues with both the celcius and cityname lists containing both 'c' and 'C'
#I used sys.exit() because when I had 'break' instead it would display the goodbye message as expected, but then loop back to the else clause for unitChoice, and continue to run the program
def runProgram():

    unitChoice = input('\n' "Would you like your temperatures to be in Celsius or Fahrenheit?")

    celsius = ['celsius','CELSIUS','c','C','Celsius']
    fahrenheit = ['fahrenheit', 'FAHRENHEIT','f','F','Farenheit']
    switch = ["switch", "SWITCH", "s", "S"]
    cityname = ['cityname', 'city','name','city name','c','cn','CITYNAME','City','CITY','Name','NAME','City Name','CITY NAME','C', 'CN']
    zipcode = ['zipcode' ,'zip code','zip', 'code', 'z','ZIPCODE','Zip Code','ZIP CODE','ZIP','CODE','Z']
    done = ['done', 'DONE', 'Done', 'D', 'd']

    if unitChoice in celsius:
        while True:

            units = celsiusUnit()
            userChoice = input('\n' "Would you like to search by zip code or city name? You can say 'switch' to change units or 'done' to leave.")

            if userChoice in cityname:
                units.cityname_celsius()
                continue

            if userChoice in zipcode:
                units.zipcode_celsius()
                continue

            if userChoice in switch:
                runProgram()
                continue

            if userChoice in done:
                goodbyeMessage()
                sys.exit()

            else:
                print("I'm sorry, please try again.")
                continue

    if unitChoice in fahrenheit:
        while True:

            units = fahrenheitUnit()
            userChoice = input('\n' "Would you like to search by zip code or city name? You can say 'switch' to change units or 'done' to leave.")

            if userChoice in cityname:
                units.cityname_fahrenheit()
                continue

            if userChoice in zipcode:
                units.zipcode_fahrenheit()
                continue

            if userChoice in switch:
                runProgram()
                continue

            if userChoice in done:
                goodbyeMessage()
                sys.exit()

            else:
                print("I'm sorry, please try again.")
                continue

    if unitChoice in done:
        goodbyeMessage()

    else:
        print("I'm sorry, please try again.")
        runProgram()

#this starts the program
welcomeMessage()
runProgram()
