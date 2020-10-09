f = open("test.txt", "w")
f.write("Hello, World 1 !\n")
f.write("Hello, World 2 !\n")
f.write("Hello, World 3 !\n")
f.close()


f = open("test.txt", "r")
string1 = f.read()
#f.close()
print("string:", string1)

string2 = f.readline()
#f.close()
print("readline:", string2)

string3 = f.readlines()
f.close()
print("readlines:", string3)


f.readline()
f.realidlines()
f.read()

f.close()