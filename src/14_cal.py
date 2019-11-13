"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
today = datetime.today()

month = input("Enter month: ")
year = input("Enter year: ")
try:
    val = int(month) and int(year)
except ValueError:
    if month or year:
        print("One of your input string is not an integer")
        print("Month and year must both be integers for this simple program to work \n Please try again!!")
        sys.exit(1)


def cal(month, year):
    if len(month) == 0 and len(year) == 0:
        print(calendar.month(today.year, today.month))
        return
    elif int(month) >= 0 and int(month) <= 12 and len(year) == 0:
        print(calendar.month(today.year, int(month)))
        return
    elif int(month) >= 0 and int(month) <= 12 and int(year) >= 0:
        print(calendar.month(int(year), int(month)))
        return
    else:
        print("Come on, A month between 1 and 12 please! please Start the program and try again")


cal(month, year)
