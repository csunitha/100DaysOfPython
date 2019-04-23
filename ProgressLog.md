<b> Day 7: 23 April 2019 </b>

SQLAlchemy / Pandas 
	- Started with trying to connect to Oracle db using SQLAlchemy and Pandas.
	- Refered the first article in the list and tried both the ways. using service name i was able to proceed. 
	- To run this, installed SQLAlchemy and cx_Oracle 

Introduction to Pep8 (Python Enhancement Proposal)
 - Style guide for Python code (Watched video beyond pep 8 by Raymond Hettinger - PyCon 2015)
 - P vs NP (Pythonic vs Non Pythonic)
 - writing adapter to make a non pythonic api to pythonic api 
 - Keyword arguments
 - namedtuple

Sites/articles
1. https://gist.github.com/DGrady/7fb5c2214f247dcff2cb5dd99e231483
2. https://www.youtube.com/watch?v=wf-BqAjZb8M&feature=player_embedded
3. https://treyhunner.com/2018/04/how-to-make-the-most-of-your-first-pycon/

<b> Day 6_1: 22 April 2019 </b>

Missed doing exercises on 21st April, however on that day did jupyter notebook install.
 - python -m pip install jupyter
 
In the command prompt, Got to the folder where you want the notebook to start and run this command
- jupyter notebook

Also was looking for python articles in DZone. 
Quick browse through of popular framework in Python
- Django - most famoos open source full stack python framework. Few things that make it most wanted in the SAAS business is template engine, URL routing, authentication, object relational mapping (ORM)
- Pyramid
- TurboGears

Article on why every programmer should learn python
- Data science, Machine Learning, Web development, Simplicity, Huge coomunity, Libraries & Framework, Automation, Multipurpose, Jobs and Growth, Salary

22nd April I tried the following items though coding (based on dzone article idioms brewing codes)
- simple iteration
- reversed
- list comprehension
- sequence unpacking (extract values from list to multiple variables)
- enumerate (It is an iterator that returns pairs, each of which contains the position of an element & element itself
- range  (range accepts an integer & returns range object which is nothing but a sequence of integers)
- str.format

Sites / articles:
- https://dzone.com/articles/python-data-structures-idioms-brewing-codes 
- https://www.geeksforgeeks.org/python-programming-language/

<b> Day 5: 20 April 2019 </b>

Not much of activities in python today as i spent some time looking at javaparser. 

Couple of things in regex covered today
- Creating groups in regex with parenthesis ()
- Matching multiple groups with the pipe | 

<b> Day 4: 19 April 2019 </b>

Topics
- Regex a bit more undestanding <br>
\b word boundary <br>
\w* any word character <br> 
word character is digit 0-9, lower/uppercase, underscore <br>
- Program: Opening a file using 'with open' and read and append the line to a list after stripping the new line character. 
- Program: Search a specific string in the file using string find() and append to list
- Program: Search a specific string in a file using regex and add to tuple

Sites introduced: 
- https://regexr.com/
- http://inventwithpython.com/
- https://www.computerhope.com/issues/ch001721.htm


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

Sites introduced: 
- https://regexpal.com/

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

