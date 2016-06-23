from bs4 import BeautifulSoup
import urllib
import json
import csv
import os

years = ['1976', '1979', '1981', '1981', '1982', '1983', '1986', '1987']
for year in range(1989,2017): years.append(str(year))
# years = ['1976']

current_location = os.getcwd().replace('\\', '/')
if (current_location[-1] != '/'):
	current_location += '/'

if (not os.path.exists("image_data")): os.mkdir("image_data")
# if (not os.path.exists("images")): os.mkdir("images")
os.chdir("image_data")

base_url = "http://www.amul.com/m/amul-hits"
for year in years:
	os.chdir(current_location + '/image_data/')
	if (not os.path.exists(str(year))): os.mkdir(str(year))
	os.chdir(str(year))
	with open((str(year) + "_advertisement_data.csv"), "w") as data_file:
		page_number = 0
		ads_present = 3
		while (ads_present):
			link = base_url + "?s=" + str(year) + "&l=" + str(page_number)
			page = urllib.urlopen(link)
			soup = BeautifulSoup(page.read(), "html.parser")
			content_region = soup.find_all("div", class_="contant1")
			tag_count = len(content_region[0].find_all("td", align="center"))
			ad_count_page = ( tag_count - 1) / 3
			image_details = []
			tag_counter = 0
			if (ad_count_page):
				print ad_count_page, "advertisements found on page", (page_number + 1), "of the advertisement listings of the year", year
				print "Downloading metadata.....\n"
				for tag in (content_region[0].find_all("td", align="center")):
					if (tag_counter%3 == 0 and tag_counter!=0):
						string = ''
						for element in image_details:
							string += str(element) + '^'
						string = string[:-1] + '\n'
						data_file.write(string)
						image_details = []
					elif (tag_counter%3 == 1):
						image_details.append(str(tag.a["href"].encode('utf-8')))
						image_details.append(str(tag.a["title"].encode('utf-8')))
						image_details.append(str(tag.img["src"].encode('utf-8')))
						image_details.append(str(tag.img["alt"].encode('utf-8')))
						image_details.append(str(tag.img["title"].encode('utf-8')))
					elif (tag_counter%3 == 2):
						image_details.append(str(tag.findAll(text=True)))
					tag_counter = tag_counter + 1
			else:
				ads_present = ads_present - 1
				if (ads_present == 0):
					print "No further advertisements found for the year", year
					print '\n\n\n'
			page_number = page_number + 1

fieldnames = ("a_href", "a_title", "img_src", "img_alt", "img_title", "img_caption")

for year in years:
	os.chdir(current_location + 'image_data/' + str(year) + '/')
	with open((str(year) + "_advertisement_data.csv"), "r") as csv_file:
		with open((str(year) + "_advertisement_data.json"), "w") as json_file:
			reader = csv.DictReader(csv_file, fieldnames, delimiter = '^', quoting=csv.QUOTE_NONE)
			json_content = json.dumps([advertisement for advertisement in reader])
			json_file.write(json_content)