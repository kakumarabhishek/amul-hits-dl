from bs4 import BeautifulSoup
import urllib

years = ['1976', '1979', '1981', '1981', '1982', '1983', '1986', '1987']
for year in range(1989,2017): years.append(str(year))

link = "http://www.amul.com/m/amul-hits?s=2016&l=3"
print "Parsing "
page = urllib.urlopen(link)
soup = BeautifulSoup(page.read(), "html.parser")

content_region = soup.find_all("div", class_="contant1")

ad_count_page = ( len(content_region[0].find_all("td", align="center")) - 1) / 3

print ad_count_page, "advertisements found on page", link.split('=')[2], "of the advertisement listings of", link.split('=')[1][0:4]







-------------------------------

ctr = 0

for tag in (roi[0].find_all("td", align="center")):
	if (ctr % 3 == 1):
		print tag.a["href"]
		print tag.a["title"]
		print tag.img["src"]
		print tag.img["alt"]
		print tag.img["title"]
	if (ctr % 3 == 2):
		print tag.findAll(text=True)
		print "New Ad"
	ctr = ctr + 1