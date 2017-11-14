import sqlite3

class dataStore:
    """ class to get and store information for videos"""
    def __init__(self):
        self.db = sqlite3.connect("clipStore.db")
        self.c  = self.db.cursor()

    def buildDB(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS clips (
                    ID INTEGER AUTO_INCREMENT,
                    movieName TEXT,
                    clipLength INTEGER,
                    director TEXT,
                    releaseDate TEXT,
                    filename TEXT,
                    PRIMARY KEY(ID)
                    )""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS videos (
                    ID INTEGER AUTO_INCREMENT,
                    videoName TEXT,
                    filename TEXT,
                    PRIMARY KEY(ID)
                    )""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS videoClips (
                    videoID INTEGER,
                    clipID INTEGER,
                    PRIMARY KEY(videoID, clipID)
                    )""")

    #TODO change to f"" strings in when updated to python3.6

    #TODO add starring catagory
    def addClip(self, movieName='', clipLength=0, director='', releaseDate='',filename=''):
        self.c.execute("""INSERT INTO clips VALUES (
                                            '{ID}',
                                            '{movieName}',
                                            '{clipLength}',
                                            '{director}',
                                            '{releaseDate}',
                                            '{filename}'
                                            )"""
            .format("NULL", movieName,clipLength,director,releaseDate, filename))
        conn.commit()

    def addVideo(self, videoName='', numberOfItems=0, filename=''):
        self.c.execute("""INSERT INTO videos VALUES (
                                            '{ID}',
                                            '{videoName}',
                                            '{numberOfItems}',
                                            '{filename}')"""
            .format("NULL", videoName, numberOfItems, filename))
        conn.commit()

    def addVideoClip(self, videoID=0, clipID=0):
        self.c.execute("""INSERT INTO videoClips VALUES (
                            '{videoID}',
                            '{clipID}'
                            )"""
            .format(videoID, clipID))
        conn.commit()


    def searchClip(self,movieName=''):
        self.c.execute("""SELECT * FROM clips WHERE movieName=?""", movieName)
        return self.c.fetchone()

class Video:
    """class to store the details of each video """

    def __init__(self, title='', movies=[]):
        self.title = title
        self.movies = movies
        self.clipList = self.buildClipList()

    def buildClipList():
        pass
test = dataStore()
#test.buildDB()
#test.addClip(movieName='TEST',clipLength=100, director='TEST', releaseDate='TEST',filename='TEST' )
print(test.searchClip(movieName="*"))
