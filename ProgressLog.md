<b> Day 3_1: 18 April 2019 </b>
- Missed: 17-Apr

Topics
- Understand the Regular expression through book 'Automate the Boring Stuff' 
- Understand few changes from pyton 2 / 3 and also how to run using main method and unit tests

\d - a digit character <br>
So sample for phone number check <br> 
\d\d\d-\d\d\d-\d\d\d\d

{n} - Macth a pattern n times, so the above pattern would become <br>
\d{3}-\d{3}-\d{4}

Steps for regex:
- import re
- define regex pattern and get regex object
- use regex.search() to get results 

Also downloaded pyku and tried to run it. In that process, has to make few changes in the code base to make it compatible to python 3. 

Python 2/3 differences.
- print needs parenthesis
- xrange of 2 does not exists in 3. range function in 3 does the same thing as xrange. 

Also run the unit test caes, and also understood how a main function is written.



<b> Day 2: 16 April 2019 </b>

Program to read csv file through pandas and plot a pie chart through matplotlib.pyplot

Additional thoughts on:
 - Reco engine based on past bookings 
 - Progam to pull data from oracle db through pandas
 - Timepass idea: haiku generator.

Sites introduced: 
- https://pybit.es/
- https://talkpython.fm/


<b> Day 1: 15 April 2019 </b>

Install packages with proxy (e.g installing pandas)
- pip install --proxy=domain\\userid:password@www-proxy-whatever:port pandas

Upgrade (without proxy)
- python -m pip install --upgrade pandas

Comment
- Single line #
- Double line ''' '''


Program to read rows in csv file through 
- csv module
- pandas.

Site introduced: 
- @SirajRawal - School of AI - Videos on sentiment analysis


<b> Day 0: 14 April 2019 </b>

Few months ago i had enrolled for a course in Udemy- "Python Mega Course" in the intention of learning Python. Though I started it - it was not progress in a consistent way. So today i decided that i would restart my learning of Python either through the course or other mechanism. So started the course and learned the following things.

Notes:
- www.pythonanywhere.com
- Useful Linux commands to be used in pythonanywhere
  - ls 
  - pwd
  - mkdir
  - touch
  - nano
  - rm 
  - cp
  - mv
- Run python program
  - python3 program.py
- Get current directory in Python
  - import os
  - os.getcwd()
  - os.chdir('c:\\users\\somedir\\')

