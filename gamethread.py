import pandas as pd
import datetime
import spacy
import gamecomment
nlp = spacy.load("en_core_web_sm")

class GameThread:


    def __init__(self, gamethread):
        #self.gamethread = gamethread
        self.date = gamethread.created_utc
        self.title = gamethread.title
        self.time = datetime.datetime.fromtimestamp(self.date).strftime('%Y-%m-%d %H:%M:%S')
        self.comments = gamethread.comments
        #self.__expandComments()
        self.__organizeComments()

        #print("GAMETHREAD Date:" + self.time + " Title " + self.title)

        #gamethread.comments.replace_more(limit=None)
        #print("Number of Input GameThread Comments " + str(len(gamethread.comments)))

        #self.data = pd.DataFrame

        #print("Number of This Object Comments " + str(len(self.comments)))

    def numComments(self):
        return len(self.comments)

    def getDate(self):
        return self.time

    def __organizeComments(self):
        df = pd.DataFrame(columns = ['UTC Date/Time', 'User', 'Comment'])
        for i in self.comments:
            #df.append(['UTC Date/Time', 'User', 'Comment'])
            doc = nlp(i.body)
            print(i.body)
            for token in doc:
                print(token.text, token.pos_, token.dep_)

    #expands the game comments get ALL comments
    #NOTE: very expensive to execute
    def __expandComments(self):
        self.comments.replace_more(limit=None)

    #calculates the word embeddings for the thread
    def __calcEmbeddings(self):
        pass




