import subprocess,requests,wget,io,json,cv2,pytesseract,time,os
from bs4 import BeautifulSoup 
import numpy as np
from PIL import Image
def action():
	url = requests.get("https://www.vpnbook.com/freevpn")
	result = BeautifulSoup(url.content,'html.parser')
	zip_url = result.find_all('img')
	x = str(zip_url[-3])
	x = x.replace('<img src="','')
	x= x.replace('"/>','')
	x= x.replace(' ','%')
	x= 'https://www.vpnbook.com/'+x+'.png'
	try:
		l = subprocess.run(["rm img.png"],shell=True)
	except:
		print('error')
	wget.download(x,'img.png')
	time.sleep(2)
	text = pytesseract.image_to_string(Image.open('img.png'))
	return text
url = requests.get("https://www.vpnbook.com/freevpn")
result = BeautifulSoup(url.content,'html.parser')
zip_url = result.find_all('a',href=True)
for z in zip_url:
	#print(z['href'])

	if 'CA' in z['href']:
		zip_dow = 'https://www.vpnbook.com'+z['href']
		#print(zip_dow)
		#print(z['href'])
		file = z['href'] 
		file=file.replace('/free-openvpn-account/','')
		#print('wget '+ zip_dow)
		list_files = subprocess.run("rm *.zip",shell=True)
		list_files = subprocess.run("rm *.ovpn",shell=True)
		text = action()
		print ("pass : {}".format(text))
		file_name = wget.download(zip_dow)
		list_files = subprocess.call(["unzip {}".format(file),'ls'],shell=True)
		files = os.listdir()
		list_files = subprocess.run(["openvpn {}".format(files[1])],shell=True)
		break
