file=open('text.txt','r')

print(file.read())

file.close()

file=open('text.txt','r')

print("\n Reading parts \n")

print(file.read(8))

file.close()

file=open('text.txt','a')

file.write("\n This is appended line.")

file.close()