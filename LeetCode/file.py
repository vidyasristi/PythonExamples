import os.path

from pip._vendor.distlib.compat import raw_input

save_path = '/Users/vidyaprabhakarsristi/Desktop'

name_of_file = raw_input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file + ".txt")

file1 = open(completeName, "w")

toFile = raw_input("Write what you want into the field")

file1.write(toFile)

file1.close()
