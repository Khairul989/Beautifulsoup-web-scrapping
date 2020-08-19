import datetime as dt
import requests
from bs4 import BeautifulSoup

data = []
url = "https://www.statsheep.com/p/Top-Subscribers?page="
for i in range(1, 5):
    text = requests.get(url + str(i)).text
    soup = BeautifulSoup(text, "html.parser")

    table = soup.find('table', attrs={"data-table m-top-standard m-bottom-standard top-charts"})
    rows = table.find_all('tr')

    now = dt.datetime.utcnow()

    for row in rows:
        if row.find('img'):
            spans = row.find_all('span')

            d = {'rank': spans[0].text, 'video_views':spans[1].text,'profile_pic': row.find('img')['src'], 'name': row.find('a').text, 'date_accessed': now}
            data.append(d)

if __name__ == "__main__":
    print(data)
    print(len(data))