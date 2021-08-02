#get all authors from the webpage https://quotes.toscrape.com/
import requests
import bs4

def get_authors():
    pagenum = 1
    author_set = set()
    
    while True:
        #get to the webpage
        req = requests.get(f"https://quotes.toscrape.com/page/{pagenum}/")

        #get soup
        soup = bs4.BeautifulSoup(req.text,'lxml')
        get_authors = soup.select('.col-md-8')
        content = get_authors[1]
        
        if 'class="next"' in str(content):

            #get authors in webpage
            authors = content.select(".author")

            #add authors in author_set
            for author in authors:
                author_set.add(author.text)

            #update page to next
            pagenum += 1

        #get authors for final page
        else:
            #get authors in webpage
            authors = content.select(".author")

            #add authors in author_set
            for author in authors:
                author_set.add(author.text)
            break
    
    return author_set

authors = get_authors()
print(authors)