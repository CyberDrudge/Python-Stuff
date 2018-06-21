from multiprocessing import Pool
import bs4
import requests
import random
import string

def starting_url(num):      
    url = "".join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(num))
    url = "".join(["http://", url, ".com"])
    #print(url)
    return url

def handle_local_links(url, link):
    if link.startswith("/"):
        return "".join([url,link])
    else:
        return link

def get_links(url):
    try:
        req= requests.get(url)
        soup = bs4.BeautifulSoup(req.text, "lxml")
        body = soup.body
        links = [link.get("href") for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        return links
    
    except TypeError as e:
        print(e)
        print("Probably tried iterating over a None")
        return []
    except IndexError as e:
        print(e)
        print("Probably didnt found any useful links")
        return []
    except AttributeError as e:
        print(e)
        print("Probably got None links")
        return []
    except Exception as e:
        print(str(e))
        return []
        
if __name__ == "__main__" :
    number = 20
    p = Pool(processes=number)
    length = 3
    parse = [starting_url(length) for _ in range(number)]
    links = p.map(get_links, [link for link in parse] )
    links = [url for url_list in links for url in url_list]
    p.close()
    
    with open("spider.txt", "w") as f:
        f.write(str(links))