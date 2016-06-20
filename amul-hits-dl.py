from bs4 import BeautifulSoup
import urllib

years = ['1976', '1979', '1981', '1981', '1982', '1983', '1986', '1987']
for year in range(1989,2017): years.append(str(year))

base_url = "http://www.amul.com/m/amul-hits"
with open("advertisement_data.csv", "w") as data_file:
	for year in years:
		page_number = 0
		data_file.write('\n\n' + str(year) + '\n\n')
		ads_present = 3
		while (ads_present):
			link = base_url + "?s=" + str(year) + "&l=" + str(page_number)
			page = urllib.urlopen(link)
			soup = BeautifulSoup(page.read(), "html.parser")
			content_region = soup.find_all("div", class_="contant1")
			tag_count = len(content_region[0].find_all("td", align="center"))
			ad_count_page = ( tag_count - 1) / 3
			print ad_count_page, "advertisements found on page", page_number, "of the advertisement listings of the year", year
			image_details = []
			tag_counter = 0
			if (ad_count_page):
				for tag in (content_region[0].find_all("td", align="center")):
					if (tag_counter%3 == 0 and tag_counter!=0):
						string = ''
						for element in image_details:
							string += str(element) + '^'
						string = string[:-1] + '\n'
						data_file.write(string)
						image_details = []
						print "New Advertisement"
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
			page_number = page_number + 1