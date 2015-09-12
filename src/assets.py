import os
import sys

def path(filename):
    workingDir = os.path.dirname(sys.argv[0])

    # Look for the assets folder in few default locations
    assets = workingDir + "/../assets/" \
        if os.path.isdir(workingDir + "/../assets") else workingDir + "/assets/"

    filepath = assets + filename
    if not os.path.isfile(filepath):
        print "Warning: " + filepath + " is not a file!"
    return filepath
