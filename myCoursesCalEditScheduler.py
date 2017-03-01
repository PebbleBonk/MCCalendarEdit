'''
Created on 28.2.2017

@author: Olli
'''
import os
from datetime import datetime
from threading import Timer
from editTags import parseMyCoursesCalendar



def editCalendar():

    """The file path for testing:"""
    icalFile = ''.join(["/Users/Olli/Documents/LiClipse Workspace/", \
                       "MCCalWrapper/icalexport.ics"])

    dirout = "/u/46/riikono2/unix/public_html/"
    outputFileName = os.path.join(dirout, 'editedCal.ics')

    parseMyCoursesCalendar(icalFile, outputFileName)


x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

t = Timer(secs, editCalendar)
t.start()