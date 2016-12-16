import requests
import string
from bs4 import BeautifulSoup


class Spider:
    def __init__(self, url):
        print("[*] Se procesa la pagina")
        self.respuesta = requests.get(url)
        self.user = url.split('/')[len(url.split('/')) - 2 ]
        print("[*] Correspondiente a :" + self.user)

    def guardar(lista):
        pass

    def obtener_links(texto_html):
        pass

class Spider_mosaic(Spider):
    def __init__(self, url):
        Spider.__init__(self, url)

    def guardar(self, lista):
        print("[*] Se comienzan a guardar los resultados")
        print("[*] se guardan" + str(len(lista)) + " resultados")
        with open("links_de_mosaic.txt", "a") as file:
            for link in lista:
                file.write(link + "\n")

    def obtener_links(self, guardar= False):
        soup = BeautifulSoup(self.respuesta.text, "html.parser")
        tags_con_links = soup.find('div', {"id":"pagination"}).findAll('a')
        links = []
        for tag in tags_con_links:
            links.append(tag["href"])
            print("[*] Mosaico encontrado")
        if guardar:
            self.guardar(links)
        return links

class Spider_post(Spider):
    def __init__(self, url):
        Spider.__init__(self, url)

    def guardar(self, lista):
        print("[*] Se comienzan a guardar los resultados")
        print("[*] se guardan" + str(len(lista)) + " resultados")
        with open("links_de_post.txt", "a") as file:
            for link in lista:
                file.write(link + "\n")

    def obtener_links(self, guardar= False):
        soup = BeautifulSoup(self.respuesta.text , "html.parser")
        tags_con_links = soup.findAll('img',{"alt": self.user})
        links = []
        for tag in tags_con_links:
            links.append(tag["src"])
            print("[*] Post encontrada")
        if guardar:
            self.guardar(links)
        return links

class Spider_imagen(Spider):
    def __init__(self, url):
        print("[*] Se procesa la pagina")
        self.respuesta = requests.get(url)
        self.user = url.split('/')[len(url.split('/')) - 3 ]
        print("[*] Correspondiente a :" + self.user)

    def guardar(self, link):
        print("[*] Se comienzan a guardar direccion de imagen")
        with open("links_de_imagenes.txt", "a") as file:
            file.write(link + "\n")
        self.retrive(link)

    def obtener_links(self, guardar= False):
        soup = BeautifulSoup(self.respuesta.text , "html.parser")
        tag_con_link = soup.find('a',{"class": "wall_img_container_big"}).find('img')
        if (tag_con_link):
            link = tag_con_link["src"]
            print("[*] Imagen encontrada")
            if guardar:
                self.guardar(link)
            return link
        else:
            print("[*] Imagen no encontrada")
                
    def retrive(self, url):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            print("200")
            with open("imagen", 'wb') as f:
                for chunk in r:
                    f.write(chunk)





url= "http://www.fotolog.com/banchero25/49072774/"
#spider = Spider_mosaic(url)
#spider.obtener_links(guardar = True)

spider = Spider_imagen(url)
spider.obtener_links(guardar = True)































