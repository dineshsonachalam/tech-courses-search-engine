from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests,json,time
from random import randint

if __name__ == "__main__":
    count = 1
    website = "https://hackr.io/"
    html_content = urlopen(website)
    soup_data = BeautifulSoup(html_content, 'lxml')
    urls = soup_data.findAll('a', attrs={'class': ' topic-grid-item js-topic-grid-item'})
    for data in urls:
        time.sleep(randint(0, 4))
        # Get HTML content of the URL
        url = data.attrs["href"]

        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        # find results from the table structure
        table = soup.findAll('div', attrs={'class': 'tut-list tut-row '})


        for result in table:
            d1 = result.find('a', {'class': 'js-details'})
            d2 = result.find('span', {'class': 'count'})
            d3 = result.findAll('span', attrs={'class': 'label label-xs label-primary'})
            d4 = result.find('a', {'class': 'icon-details'})
            topic = d1.attrs["data-topic"]
            title = d1.attrs["data-tutorial"]
            url = d4.attrs["href"]
            upvotes = int(d2.get_text())
            labels = []
            for label in d3:
                labels.append(label.get_text())

            print("Topic: ", topic)
            print("Title: ", title)
            print("Total Upvotes: ", upvotes)
            print("Labels: ", labels)
            print("URL: ",url)

            post_url = "http://localhost:9200/hacker/tutorials"
            post_autocomplete_url ="http://localhost:9200/autocomplete/titles"
            payload ={
                "upvote":int(upvotes),
                "topic":topic,
                "title":title,
                "url":url,
                "labels":labels
            }
            payload_autocomplete={
                "title": title,
                "title_suggest":title
            }

            headers = {
                'Content-Type': "application/json",
                'cache-control': "no-cache"
            }
            payload = json.dumps(payload)
            payload_autocomplete = json.dumps(payload_autocomplete)
            response = requests.request("POST", post_url, data=payload, headers=headers)

            response_autocomplete = requests.request("POST", post_autocomplete_url, data=payload_autocomplete, headers=headers)
            if(response.status_code==201):
                print("Values Posted in hacker index")
            if(response_autocomplete.status_code==201):
                print("Values Posted in autocmplete index")


            print("----------------", count, "----------------------")
            count = count + 1

