import praw
import datetime
import os.path
from os import path
import pathlib
import csv
import pandas
#import sklearn

from gamethread import GameThread

fileLoc= "c:\\data\\billsreddit\\"
class BillsReddit():
    def __init__(self):
        self.process()

    def writeToCSV(self, gamethread):
        file =pathlib.Path(os.path.join(fileLoc, gamethread.title + ".csv"))
        if file.exists():
            print ("File exists:"+str(file.exists()))
            os.remove(file)

        fields = ['ID', 'Author', 'Date', 'Comment']

        with open(file, mode='w') as reddit_file:
            reddit_writer= csv.writer(reddit_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            reddit_writer.writerow(fields)

    def process(self):
        reddit = praw.Reddit(client_id ='J-QEMFqtVvg2UA',
                                 client_secret ='mp4xLH-gPdTuP1MHOhW-agywtUgfag',
                                 user_agent ='my user agent')
        #print(reddit.read_only)

        bills = reddit.subreddit("buffalobills")

        # display the subreddit name
        print(bills.display_name)

        #print(subreddit.banned)
        #display the subreddit title
        print(bills.title)

        # display the subreddit description
        #print(bills.description)

        #search for the game threads
        keyword = "Game Thread"
        gamethreads = []

        for i in bills.search(keyword, sort='new'):
            #if the title contains "Game Thread" we keep it, otherwise toss it
            if keyword in i.title:
                #print("TITLE: " + i.title)
                time = datetime.datetime.fromtimestamp(i.created_utc).strftime('%Y-%m-%d %H:%M:%S')
                print("THREAD Date:" + time + " Title " + i.title)
                i.comments.replace_more(limit=0)

                gt = GameThread(i)
                #self.writeToCSV(gt)
                #gamethreads.append(gt)

        print("Number of Game Day Threads " + str(len(gamethreads)))

        #the gamethread submission
        #i is the submission
        #for i in gamethreads:

            #time = datetime.datetime.fromtimestamp(i.date).strftime('%Y-%m-%d %H:%M:%S')
            #print("Date:" + time + " Title " + i.title)
            #print ("Number of Comments " + str(len(i.comments)))

            # expand out all of the comments. this takes a long time


