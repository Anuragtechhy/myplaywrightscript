import os


a=open('C:/Users/MDP/Pictures/Screenshots/filepycharm.txt', 'w')
a.write("Hello World")
a.close()


a = open('C:/Users/MDP/Pictures/Screenshots/filepycharm.txt', 'a')
a.write("Hello World new")
a.close()


a = open('C:/Users/MDP/Pictures/Screenshots/filepycharm.txt', 'r')
c=a.read()
print(c)
a.close()

os.mkdir("C:/Users/MDP/Pictures/Screenshots/mydir")
print("done")


