import requests, sys, webbrowser, bs4
#get search term from command line
res=requests.get("http://google.com/search?q="+"".join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
linkElems=soup.select('.r a')
numopen=min(5,len(linkElems))

for i in range(numopen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
