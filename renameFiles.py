import os

def renameFiles():

   initialDirectory = os.getcwd()

   print("Initial directory is " + initialDirectory)

   directory = "/data/dev/python/prank/"
   os.chdir(directory)

   list = os.listdir(directory)

   print(list)

   for filename in list:
      os.rename(filename, directory + filename.translate(None, "0123456789"))

   os.chdir(initialDirectory)
renameFiles()
