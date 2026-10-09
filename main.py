import requests
import pprint
from bs4 import BeautifulSoup as BS


def sort_stores_by_votes(hn_list):
    return sorted(hn_list, key=lambda k : k['Score'], reverse=True)


def how_many_page_news_to_read(page_num: int):
    
    hn = []

    for i in range(1, page_num+1):
        URL = f"https://news.ycombinator.com/?p={i}"
        ## We will get the data using request. request act as our browser and we will pass the URL to it.
        ## It will give us all the HTML content
        res = requests.get(URL)

        ## Now our task is to get the content filtered from the HTML we get , for this purpose we will use Beautiful SOup
        ## We will filter whose points are greater then 100 and the jobs posted
        soup = BS(res.text, 'html.parser')
        links = soup.select('.titleline > a')
        subtext = soup.select('.subtext')


        # we just want the title, and there URLs
        for idx, item in enumerate(links):
            title = item.getText()
            href = item.get('href', None)
            votes = subtext[idx].select('.score')
            # lets also get the ponyts
            if len(votes):
                points = int(votes[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'Title': title, 'Links': href, 'Score': points})
    return sort_stores_by_votes(hn_list=hn)


# User input
pages = int(input("How many pages do you want to scrape? "))
results = how_many_page_news_to_read(pages)

pprint.pprint(results)
print(f"\nTotal stories with >99 points found: {len(results)}")