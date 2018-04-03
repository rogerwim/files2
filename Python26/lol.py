from Crypto import Random
a = 1
f = open("files.txt", 'w')
while True:
 	try:
		print(a,"passes done")
		a = a+1
                f.write("a bit of data")
	except:
		file.close
		print("we are offline now")
		a = raw_input()
		break
