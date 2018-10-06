import time
from datetime import datetime as dt

# sample hosts file
hosts_temp=r"C:\Users\kdrag\Documents\Python_recap\Python_project3(website_blocker)\hosts"
# actual location of hosts file
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.youtube.com","youtube.com","www.facebook.com","facebook.com"]


while True:
    # change the timing if you want.in here from 1 to 3, the blocker is active
    if dt(dt.now().year,dt.now().month,dt.now().day,13)< dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,15):
        print("Working hours...")
        # open with r+ mode so that reading and writing of files are possible
        with open(hosts_temp,'r+') as file:
            # read() will put all the contents of file into a single string
            content=file.read()
            # print(content)
            for website in website_list:
                if website in content:
                    # if website is in content, do not do anything.Hence pass
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            # readlines will return every line in the file as a list element.Content will be a list
            # readlines print all lines and put it in a list. Readline only print the first line
            content=file.readlines()
            # seek(0) as you want the cursor/pointer to return to the very top(original position)
            # after using readlines, the cursor is at the bottom, after the last line of content in file
            file.seek(0)
            # the goal here is rewriting the whole file to its original before any websites are written in it
            for line in content:
                # if websites are not in the lines, then write out the lines again.if websites appear
                # ignore those line
                if not any(website in line for website in website_list):
                    file.write(line)
            # truncate cuts all/any content after the cursor/pointer
            file.truncate()
        print("Fun hours...")
    # run the loop after every 5 seconds instead of milliseconds, allowing a pause
    time.sleep(5)