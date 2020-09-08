from base64 import b64decode
import random
import string
import pathlib

print("===============================================")
print("|           ENCODE STRING TO BASE64           |")
print("|              BY ANGGA MANGGALA              |")
print("===============================================")
file_name = input("Enter file name : ")
try:

	# READ & CONVERT
	f = open(file_name, "r")	
	base64 = b64decode(f.read())	
	f.close()

	# SAVE
	ranstr = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
	new_file_name = "dec_" + ranstr + pathlib.Path(file_name).suffix
	fw = open(new_file_name, "x")
	fw.write(str(base64.decode()))
	fw.close()
	
	print("Decode file saved in file :", new_file_name)
	print("Success !")

except Exception:
	print("File not found !")