import fnmatch
import os
import random

#randval = random.randint(0, 8)
#print(randval)


# Put all of the jpgs in directory in a list
# Pop a random file
def getfile():
    # create  list
    # Read all jpg files in directory into list
    # Get a random number between 0 and end of list-1
    # Return that file
    pattern = "*.png"
    picList = list()
    listOfFiles = os.listdir('images')
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
#            print (entry)
            picList.append(entry)
        else:
            pass
#    print("Length of picList: ", len(picList))
#    print(picList[random.randint(0, len(picList) - 1)])
    return picList[random.randint(0, len(picList) - 1)]


def makepage(file="0.jpg"):
    file = str(file)
    print("<html>\n\t<body>\n\t\t<img src=images/{0}>\n\t</body>\n</html>".format(file))


#getfile()
makepage(getfile())
