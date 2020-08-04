import fnmatch
import os
import random
import datetime


def writefile(content_in, filename="index.html"):
    wf = open(filename, "w")
    wf.write(content_in)
    wf.close()


def getfile():
    pattern = "*.png"
    picList = list()
    listOfFiles = os.listdir('images')
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            picList.append(entry)
        else:
            pass
    return picList[random.randint(0, len(picList) - 1)]


def makepage(file="0.jpg"):
    file = str(file)
    # print("<html>\n\t<body>\n\t\t<img src=images/{0}>\n\t</body>\n</html>".format(file))
    return('''\
    <HTML>
        <body>
        <center>
            <img src=images/{0}>
        </center>
        </body>
        <!-- {1} -->
    </HTML>
    '''.format(file, datetime.datetime.now()))

writefile(makepage(getfile()))
