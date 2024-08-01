#read a text file
r = open("hello.txt","r")
print(r.read())
r.close()

#read one line at a time
r = open("sample.txt","r")
print(r.readline())
r.close()

#read list of lines
r = open("sample.txt","r")
print(r.readlines())
r.close()