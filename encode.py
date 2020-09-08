from base64 import b64encode
import random
import string
import pathlib

print("===============================================")
print("|           ENCODE STRING TO BASE64           |")
print("|              BY ANGGA MANGGALA              |")
print("===============================================\n")
file_name = input("Enter file name : ")
try:

	# READ & CONVERT
	f = open(file_name, "r")
	ascii = f.read().encode('ascii')
	base64 = b64encode(ascii)	
	f.close()

	# SAVE
	ranstr = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
	new_file_name = "enc_" + ranstr + pathlib.Path(file_name).suffix
	fw = open(new_file_name, "x")
	fw.write(str(base64.decode()))
	fw.close()

	print("Encode file saved in file :", new_file_name)
	print("Success !")

except Exception:
	print("File not found !")