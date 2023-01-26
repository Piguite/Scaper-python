# WHAT IS SCRAPING:

Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.[1] Web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis. (wikipedia)

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

# USAGE:

step 1:

don't forget to install scrapy

step 2:

go to the project folder in your terminal and execute this command (The command is the same on every operating system.):


scrapy crawl routeur -o  (your_csv_file_name).csv


That's it, enjoy playing with this and feel free to modify it to scrap what ever you want, you can also sort the information you get to have such a beautiful csv file.

Here is the SCRAPY documentation if you want to modify the code https://docs.scrapy.org/en/latest/
