f=open("data.txt","w")
f.write("Emergency Call")
f.close()

f=open("data.txt","r")
print(f.read())