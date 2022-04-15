Data used in Digital Movie Ticket Stubs:
Data source: TicketStubsDigital Google Sheet

Year - The year in which a movie was seen
Title - The title of the movie as it appeared on the stub
Theater - Name of the theater at which the movie was seen
Day of the Week - Day on which the movie was seen. Ex. Monday
Date - The year/month/day of which the movie was seen
Time - The start time of the movie
System Requirements
Python v3.10.1
pandas v1.4.0
matplotlib v3.5.1
Active internet connection
### Instructions
From the command line:

Clone the PythonWorldCommandLine repo from GitHub:
https://github.com/articsmoke1937/PythonWorldCommandLine
Navigate to the PythonWorldCommandLine directory.
Create and activate a virtual environment.
Use pip to install system requirements:
pip install -r requirements.txt
Run the project:
DoItAllProgram.py
Menu Option Descriptions
1. Movie Lookup
User inputs a movie title
If the title exists in the DataFrame, returns the details from the stub.
If the input doesn't exist, the function returns a negative message.
Searches by exact spelling and punctuation but not casing.
'Spiderman: No Way Home' will be found. 'Spider man No Way Home' will not be found.
'Lincoln' and 'LiNColN' will both be found.
2. Most Recent Movie
Returns the most recent movie seen, the date seen, and how many days ago the movie was seen.
3. Number of Movies Watched in a Year
User inputs a year with format 'xxxx' from within range 2012-Current Year.
If year exists in the DataFrame, returns the number of movies seen that year.
If input is a year before 2012 or input is not in correct format, returns an invalid input message.
If input is the current year but there is no data, returns a corresponding message.
4. Movies by Start Time
Returns a bar chart of number of movies seen against start times.
5. Movie Suggestions
User inputs a movie title
If the title does not exist in the DataFrame, logs the title to an INFO log.
If the title already exists in the DataFrame, the user is notified and the title is not logged.
6. Random Ticket
Returns the ticket info for a random movie from the DataFrame.
Code Louisville Project Requirements
Category 1
Project implements a master loop console application. User can enter commands to choose options, exit select options, and exit program.
Option 2 calculates and displays data based on an external factor (the day the function is called)
Option 3 creates lists and a dictionary, and then the dictionary is searched with user input as the key, outputs value back to the user.
Option 4 creates lists used to populate chart.
Category 2
This project reads data from an external Google Sheets URL. Sheet is read as a CSV.
Category 3
Options 1 and 6 visualize data in tabular form.
Option 4 visualizes data in a bar chart.
Category 4
This project utilizes a virtual environment and lists dependencies in a requirement.txt file.
movies.py has an accompanying test module, Test_movies.py. Test_movies.py includes 4 unit tests to test the concept of Option 1.
Options 1, 3, and 5 utilize INFO logging to track user inputs.
