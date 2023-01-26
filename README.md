# ABOUT THE CODE:

This is an own python project which use the python library SCRAPY to scrap the website ldlc.
The goal of the project was to collect informations about 4g routers in the ldlc website what involves:
- the name 
- the price
- the picture 
- the description
- the rating 

The informations collected are stored in a csv file. The code use the source code of the website to know what informations they need to take, (you can access it by pressing F12 on a website)
look at the main.py and the router.py to understand

# USAGES:

step 1:

don't forget to install scrapy

step 2:

go to the project folder in your terminal and execute this command (The command is the same on every operating system.):


scrapy crawl routeur -o  (your_csv_file_name).csv


That's it, enjoy playing with this and feel free to modify it to scrap what ever you want, you can also sort the information you get to have such a beautiful csv file.
