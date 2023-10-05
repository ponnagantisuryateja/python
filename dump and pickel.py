import os
import pickle
#os.mkdir("d:\\suryafiles")

picklefile = open("d:\\suryafiles\\binaryfile.pdf","ab+")
mylist = {"a","b","c", "d"}
pickle.dump(mylist,picklefile)
print("my list is::",mylist)