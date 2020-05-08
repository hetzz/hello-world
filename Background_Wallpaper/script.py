import random, os
import requests
import bs4
import string

# Get a new image from the internet
def get_image():
	r = requests.get('https://www.wallpaperflare.com/')
	soup = bs4.BeautifulSoup(r.text)
	print("Yes")
	images = soup.select('img')
	links = []
	for item in images:
		links.append(item.get('data-src'))
	links = links[1:]
	return random.choice(links)

#Choose a random image from your folder
def get_folder_image():
	return random.choice(os.listdir('Wallpapers')) # list the relative path for your wallpapers folder

def create_image():
	res = ''
	res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = 7))
	f = open('Wallpapers/'+res+'.jpg','wb')  # list the relative path for your wallpapers folder
	f.write(requests.get(get_image()).content)
	f.close()
	return res

def set_wallpaper():
	file_name = create_image() + ".jpg"
	#file_name = get_folder_image()
	location = "/home/hetal/Projects/hello-world/Background_Wallpaper/Wallpapers/"+file_name  # use the complete path for your wallpapers folder
	os.system('gsettings set org.gnome.desktop.background picture-uri '+location)

set_wallpaper()

