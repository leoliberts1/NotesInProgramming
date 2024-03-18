'''
fp = open(r"/Users/leoliberts/PycharmProjects/pythonProjectpleasework/revision, 1st semester 2023/5.files/test.txt", "r")


print(fp.read())
fp.close()
f = open("test.txt", "r")
# move to 11 character
f.seek(11)
# read from 11th character
print(f.read())''''''
f = open("test.txt", "r")
# read first line
f.readline()
# get current position of file handle
print(f.tell())
f.close()
# Output 25'''

