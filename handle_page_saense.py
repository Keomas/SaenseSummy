import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urlsplit
import unicodedata
import re


class HandlePage:
    def __init__(self, url):
        self.url = url
        self.dict = {}
        self.titulo = None
        self.soup = None
        self.jsonobj = None
        self.text = None
        self.autor = None
        self.data = None
        self.image_url = None
        
    def getSoup(self):
        response = requests.get(self.url, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.soup = soup

    def cleanText(self, text):
        text = text.replace('\n', ' ')
        cleanText = []
        # Parametro criado para auxiliar a remover referencias do texto #
        ref = False
        for ch in text:
            if ch == "[":
                ref = True
            elif ch == "]":
                ref = False
            
            elif ref:
                pass
            else:
                nfkd = unicodedata.normalize('NFKD', ch)
                filter = re.sub('[^A-z 0-9 , . ( ) / - -\\\]', '', nfkd)
                char = u"".join([c for c in filter if not unicodedata.combining(c)])
                cleanText.append(char)
        return ''.join(cleanText)

    def getTitulo(self):
        titulo = self.soup.title.string.split("–")[0].rstrip().lower()
        self.titulo = self.cleanText(titulo)       

    def getTexto(self):
        bodydiv = self.soup.body.find("div",{"itemprop":"articleBody"})
        bodycontent = bodydiv.find_all(lambda tag: tag.name == 'p' and not tag.attrs)
        bodycontentfinal = ""
        for p in bodycontent[1:]:
            bodycontentfinal += p.get_text() + " "
        self.text = self.cleanText(bodycontentfinal)
        
    def getAutor(self):
        try:
            bodydiv = self.soup.body.find("div",{"itemprop":"articleBody"})
            autor, data = bodydiv.p.getText().split('\n')
        except Exception as e:
            autor = "Vazio"
            pass
        self.autor = autor

    def getData(self):
        try:
            bodydiv = self.soup.body.find("div",{"itemprop":"articleBody"})
            autor, data = bodydiv.p.getText().split('\n')
        except Exception as e:
            data = "Vazio"
            pass
        self.data = data

    def getImageUrl(self):
        image_url = self.soup.find('figure').img['src']
        self.image_url = image_url

    def getJson(self):
        dict = {
            "url": self.url,
            "titulo": self.titulo,
            "autor": self.autor,
            "data": self.data,
            "imgurl": self.image_url
        }
        self.dict = dict #jsonobj
