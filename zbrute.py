def logo ():
	logo = """    ______            _       
    | ___ \\          | |      
 ___| |_/ /_ __ _   _| |_ ___ 
|_  / ___ \\ '__| | | | __/ _ \\
 / /| |_/ / |  | |_| | ||  __/
/___\\____/|_|   \\__,_|\\__\\___|
nopeebee7 [@] skullxploit
	"""
	print(logo)

def opt ():
	zipname = input(" [+] zip file > ")
	if os.path.exists(zipname):
		try:
			filezip = pyzipper.AESZipFile(zipname)
		except pyzipper.zipfile.BadZipfile:
			print(" [-] bad zip file")
			exit()

		try:
			filezip.testzip()
		except RuntimeError as e:
			if 'encrypted' not in str(e):
				print("\n [-] zip file is not encrypted")
				exit()
	else:
		print(" [-] zip file not found")
		exit()
	passfile = input(" [+] wordlist > ")
	if os.path.exists(passfile):
		filepass = open(passfile, "r+").readlines()
	else:
		print(" [-] wordlist not found")
		exit()

	return filezip, filepass

def out(msg: str):
    last_msg_length = len(out.last_msg) if hasattr(out, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    out.last_msg = msg

if __name__ == "__main__":
	logo()
	import sys, os
	if sys.version_info[0] < 3:
		print(" [-] please run this script with python3")
		exit()
	try: import pyzipper
	except: print(" [-] require module pyzipper\n [-] pip3 install pyzipper"); exit(0)
	sx = opt()
	listFile = sx[0].namelist()
	if len(listFile) > 0:
		for password in sx[1]:
			password = password.replace("\n", "").replace("\r", "")
			out(" [+] trying with pass : "+password)
			try:
				sx[0].pwd = bytes(password, "utf-8")
				unzip = sx[0].read(listFile[0])
			except RuntimeError:
				continue
			out("")
			print(" [+] password found : "+password)
			exit()
		out("")
		out(" [+] not found match password :(")
		exit()
