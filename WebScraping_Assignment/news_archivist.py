
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9812482
#    Student name: Kevin Gunawan
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.

from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path-naming conventions used on this
# computer.  Apply this function to the full name of your
# HTML document so that your program will work on any
# operating system.
from os.path import normpath
    
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date and time function.
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


################ PUT YOUR SOLUTION HERE #################

#Getting the current file directory
path=getcwd()

#Function Extractnews is created to extract relevant information from archived
#document and recreate a new html page that will be diaplayed in browser.
def extractnews(file):
    global path
    global internet_archive
    #creating a path for the selected archive document in internet archive folder
    full=path+"\\"+internet_archive+"\\"+file
    #creating a normalised path
    norm=normpath(full)
    text_out=open(norm,"r",encoding='UTF-8')
    opensesame=text_out.read()
    text_out.close()
    #Date of archived document
    article_date=findall('<lastBuildDate>(.*)<\/lastBuildDate>',opensesame)
    #Finding all the sections of article from the archived document
    item_appear=findall('<item>[\s\S]+?</item>',opensesame)
    #creating of new html file
    text_in=open("new"+file,"w",encoding='UTF-8')
    text_in.write('''<!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
            <title>Assignment2 python</title>
            <style>
                body{background-color: antiquewhite}
                header{font-size: 5vw}
                p{font-size: 3vw}
                date{font-size: 3vw}
                img{width: 60%;
                    max-width: 100%;
                    height:auto;
                }
                h2{font-size: 4vw}
                h3{font-size: 3vw}
            
            </style>
        </head>
        <body>
            <section align='center'>
                <header>NBC News Archive</header>
                <img src='https://www.thewrap.com/wp-content/uploads/2013/10/nbc-news-logo.jpg' alt="NBC logo"/>
                <p>News source:<a href='http://feeds.nbcnews.com/feeds/topstories'>http://feeds.nbcnews.com/feeds/topstories</a></p>
                <p>Archvist:Kevin Gunawan</p>
                <date>'''+article_date[0]+'''</date>
            </section>
            <hr>

    ''')
    ##introducing a count variable so that articles will be numbered
    count=1
    #extracting the relevant information from the extracted sections of the archived document
    for item in item_appear:
        text_in.write('''        <article align='center'>'''+'''\n''')
        #titles
        titleoccurences=findall('<title>([^\"]+)<\/title>',item)
        text_in.write('            <h2>' + str(count)+'.'+' '+titleoccurences[0]+'</h2>'+'\n')
        
        #images
        images=findall('<media:content url=\"([^\"]+)\"',item)
        if len(images)== 0:
            text_in.write('            <img src= "https://www.thewrap.com/wp-content/uploads/2013/10/nbc-news-logo.jpg"')
        else:
            text_in.write('            <img src="'+images[0]+'"')
        #image desc
        alt=findall('<media:text type=\"plain\">(.*)</media:text>',item)
        if len(alt)== 0:
            text_in.write(' alt="No description"/>'+'\n')
        elif alt[0]=="":
            text_in.write(' alt="No description"/>'+'\n')
        else:
            text_in.write(' alt="'+alt[0]+'"/>'+'\n')
        #Description
        description=findall('<description>([a-zA-Z\"\']+.*\D*)<\/description>',item)
        text_in.write('            <h3>'+description[0]+'</h3>'+'\n')
        #links
        links=findall('<link>(.*)<\/link>',item)
        text_in.write('            <p><b>Full Story:</b>'+'<a href="'+links[0]+'">'+links[0]+'</a></p>'+'\n')
        #Dates
        publishingdate=findall('<pub[dD]ate>([a-zA-Z]+.*)<\/pub[dD]ate>',item)
        text_in.write('            <date>'+'PubDates:'+publishingdate[0]+'</date>'+'\n')

        text_in.write('''    </article>'''+'''\n''')
        text_in.write('''    <hr>'''+'''\n''')
        count+=1


    text_in.write('''    </body>'''+'''\n''')
    text_in.write('''</html>''')
    text_in.close()
#Creating a function to download the latest news and storing it into the internet archive folder
def storing():
    # Putting web page address here
    url = 'http://feeds.nbcnews.com/feeds/topstories'
    # Open the web document for reading
    web_page = urlopen(url)

    # Read its contents as a Unicode string
    web_page_contents = web_page.read().decode('UTF-8')

    # Write the contents to a html file (overwriting the file if it
    # already exists!)
    html_file = open('InternetArchive//Latest_News.html', 'w', encoding = 'UTF-8')
    html_file.write(web_page_contents)

    html_file.close()

#Creating a function to open the new html file to the default browser
def show(file):
    global path
    showing_path=path+"\\"+"new"+file
    normal=normpath(showing_path)
    webopen(normal)
    
##
## FRONT END PYTHON GUI
##

#create a TK window
news = Tk()

#give the window a title
news.title('NBC Latest News')

#changing background color of tk widget
news.configure(background="#ADD8E6")


#Creating a label widget to store image
photo= PhotoImage(file="logo.gif")
logo=Label(news,image=photo)
logo.photo=photo
logo.grid(row=1,column=0,rowspan=3,columnspan=4,sticky="w")

#Create a Label widget to inform users what to do
information=Label(news,text = 'Please select a date to extract',
                  font=20,width=40,height=3)

information.grid(row=4,column=0,columnspan=4,rowspan=3)

#Function to change the text in the label when a Extract&display button is pressed and a date is picked.News is also displayed simultaeously.
## if latest news is extracted before being archived, an error will be displayed
def update():
    global var
    if choices.curselection() == (0,):
        information['text']='News extracted and displayed :)'
        extractnews("2oct_nbc.html")
        show("2oct_nbc.html")
        if var.get():
            logextract()
    elif choices.curselection() == (1,):
        information['text']='News extracted and displayed :)'
        extractnews("3oct_nbc.html")
        show("3oct_nbc.html")
        if var.get():
            logextract()
    elif choices.curselection() == (2,):
        information['text']='News extracted and displayed :)'
        extractnews("4oct_nbc.html")
        show("4oct_nbc.html")
        if var.get():
            logextract()
    elif choices.curselection() == (3,):
        information['text']='News extracted and displayed :)'
        extractnews("5oct_nbc.html")
        show("5oct_nbc.html")
        if var.get():
            logextract()
    elif choices.curselection() == (4,):
        information['text']='News extracted and displayed :)'
        extractnews("6oct_nbc.html")
        show("6oct_nbc.html")
        if var.get():
            logextract()
    elif choices.curselection() == (5,):
        information['text']='News extracted and displayed :)'
        extractnews("7oct_nbc.html")
        show("7oct_nbc.html")
        if var.get():
            logextract()
    elif choices.curselection() == (6,):
        information['text']='News extracted and displayed :)'
        extractnews("8oct_nbc.html")
        show("8oct_nbc.html")
        if var.get():
            logextract()
    elif choices.curselection() == (7,) and Trigger:
        information['text']='News extracted and displayed :)'
        extractnews("Latest_News.html")
        show("Latest_News.html")
        if var.get():
            logextract()
    elif choices.curselection() == ():
        information['text']='Error please choose an option!'
        if var.get():
            logerror()
    else:
        information['text']='Please archive the latest news first'
        if var.get():
            logerror()

# A trigger variable that changes to True when latest news is archived with the press of archive button
Trigger=False

#Function to change the text when user presses on archive after they select latest news or select other dates
def archived():
    global var
    if choices.curselection() == (7,):
        information['text']='Storing in archive'
        global Trigger
        Trigger=True
        storing()
        if var.get():
            logarchive()
    elif choices.curselection() == ():
        information['text']='Error please choose latest news'
        if var.get():
            logerror()
    else:
        information['text']='News are already in archived'
        if var.get():
            logerror()

#List of dates to choose from
Dates = ['02_october','03_october','04_october','05_october','06_october'
         ,'07_october','08_october','Latest News']
#Creating a listbox widget to display the news dates
choices = Listbox(news,height=len(Dates),width=40,font=10)
for item in Dates:
    choices.insert(END,item)
choices.grid(row=7,column=0,columnspan=4)

#Creating Buttons
extract= Button(news,text='Extract&Display',width=20,command=update)
store=Button(news,text='Archive',width=20,command=archived)
#Arranging buttons
extract.grid(row=8,column=0,sticky='w',padx=25)
store.grid(row=8,column=3,padx=25)


##
##Assignment Part B
##
##A function that logs activities about checkbox
def box():
##Connecting and logging events into database when checkbox is clicked
    connection=connect(database='event_log.db')
#get a cursor on the database
    log=connection.cursor()
    global var
    if var.get():
#checkbox is clicked
        click='insert into Event_Log(Description) values ("Event Logging is switched on")'
        log.execute(click)
        connection.commit()
    else:
        #checkbox is switched off
        off='insert into Event_Log(Description) values ("Event Logging is switched off")'
        log.execute(off)
        connection.commit()
    log.close()
    connection.close()
    
#A function that logs activities about extract&display button
def logextract():
    ##Connecting and logging events into database when checkbox is clicked
    connection=connect(database='event_log.db')
#get a cursor on the database
    logex=connection.cursor()
    #button is pressed
    query='insert into Event_Log(Description) values ("News extracted from archive and displayed")'
    logex.execute(query)
    connection.commit()
    logex.close()
    connection.close()

#A function that logs activities about archive button
def logarchive():
    ##Connecting and logging events into database when checkbox is clicked
    connection=connect(database='event_log.db')
#get a cursor on the database
    logar=connection.cursor()
    query2='insert into Event_Log(Description) values ("Latest News downloaded and stored in archive")'
    logar.execute(query2)
    connection.commit()
    logar.close()
    connection.close()

#A function that logs errors made by users when clicking buttons
def logerror():
    ##Connecting and logging events into database when checkbox is clicked
    connection=connect(database='event_log.db')
#get a cursor on the database
    loger=connection.cursor()
    query3='insert into Event_Log(Description) values ("Error")'
    loger.execute(query3)
    connection.commit()
    loger.close()
    connection.close()
    


#Creating the checkbox for event logger
#creating a variable var that checks whether the checkbox has been selected
var=IntVar()
event_log=Checkbutton(news,text='Log Events',variable=var,command=box)
#packing checkbox
event_log.grid(row=11,column=1,pady=8)


#start event loop to react to user inputs
news.mainloop()


