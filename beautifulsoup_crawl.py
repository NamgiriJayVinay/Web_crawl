from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  
page_url = "https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1&ref_=nmls_vm_dtl"


uClient = uReq(page_url)


page_soup = soup(uClient.read(), "html.parser")
uClient.close()


containers = page_soup.findAll("div", {"class": "lister-item mode-detail"})

filename="celebraties.csv"
f=open(filename,"w")

headers=" index,image,Name, Movie, About\n"

f.write(headers)
x=0
for container in containers:

    x=x+1

    name=container.div.a[0].text

    name=container.div.a.'src'

    profession_moviename=container.findAll("p",{"class":"text-muted text-small"})
    pro_movie=profession_moviename[0].text.strip()

    about_container=container.findAll("p")
    about=about_container[1].text

    print("index "+x)
    print("image "+image)
    print("name "+name)
    print("movie acted: "+pro_movie)
    print("about: "+about)

    f.write(x + ","+image + ","+ pro_movie.replace("|" , ",") + ","+about+"\n")
f.close()
