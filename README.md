
System Requirements
Python v3.10.1
pandas v1.4.0
matplotlib v3.5.1
Active internet connection

## Instructions
    Clone the PythonWorldCommandLine repo from GitHub:
        https://github.com/articsmoke1937/PythonWorldCommandLine
    
    Navigate to the PythonWorldCommandLine directory.
    
    Create and activate a virtual environment.
    
    Use pip to install system requirements:
        pip install -r requirements.txt
    
    Run the project:
    DoItAllProgram.py

### Menu Option Descriptions
    1. Login
      Diaglog will appear to ask user if they are the previous user to login.
      If the user enters '1' the program will proceed to the main menu
      If the user enters '2' the program will do a user setup and the user will now be added to the user catalog
    2. Norris Jokes - this program uses a call to https://api.chucknorris.io/jokes/random to pull back a specified number of jokes.
       The user must enter a number here and the program will return that number of jokes.
    3. Weather Channel - this program calls out to "http://api.openweathermap.org/data/2.5/" using an api key and returns weather information
       The user must use an real city such as 'Louisville'.  They will have the option of using the city they logged or choosing a new city.
    4. Review Stocks - This program utilizes the yfinance package to obtain information about stocks
       The user must enter a valid stock symbol such as 'MSFT'.  They will get a description of the company.
       The user can then choose a new stock or continue with stock to a sub menu that will provide more information.  If the infomration does not exist, nothing will          be returned.
       The user can also do a stock comparison.  the user is asked how many stocks they would like to compare, this must be a number such as '2' And the user must            enter in valid stock symbols such as 'msft' and 'amzn'.  This will return a plot graph of price history for the stocks.
     5. The final program is rock, paper, scissors.  In this the user must declare which item they want to use, they must correctly spell the item such as 'rock'
        The program will return the results to the user.

## Code Louisville Requirements
### Category 1
        Project implements a master loop console application. User can enter commands to choose options, exit select options, and exit program.
        Option 2 calculates and displays data based on an external factor, the Chuck Norris jokes and the Weather program
        Option 3 creates lists and a dictionary which are utilized for user information and last user login.
        Option 4 A list is created for the stocks and will display a graph

### Category 2
        This project reads data from an external json file.

### Category 3
        Option 4 Stock data is visualized in a plot graph

### Category 4
        This project utilizes a virtual environment and lists dependencies in a requirement.txt file.

