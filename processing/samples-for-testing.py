# This program just assigns random numbers to HTML and TXT files.
# This is to facilitate checking of random transcripts.

# TODO sort this out. It's a useful feature, although one we haven't used for a while.

import os
import numpy as np
import shutil
from commonfunctions import commonfunctions as cf

root_directory = os.path.abspath(os.path.dirname(os.path.abspath(os.curdir)))
directory = os.path.join(root_directory, cf.working_directory)

oldFilesList = os.listdir(directory)
filesList = []

for x in oldFilesList:
    if '.txt' in x:
        filesList.append(x)

for x in filesList:
    shutil.copy(os.path.join('transcripts-for-checking', x), 'transcripts-random')
    html = x[:-3] + "html"
    shutil.copy(os.path.join('html-files', html), 'transcripts-random')
    randInt = str(int(np.random.randint(1000, 9999)))
    os.rename(os.path.join('transcripts-random', x), os.path.join('transcripts-random', (randInt + ".txt")))
    os.rename(os.path.join('transcripts-random', html), os.path.join('transcripts-random', (randInt + ".html")))
