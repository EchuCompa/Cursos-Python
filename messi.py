import scrapy
import html2text
import seaborn as sns 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
# from actividad3_1 import histo_wordcloud # No se cómo poner un path en el from :(

def extraer_links(self, data):
       lista_palas = data.split("doi")
       for i, j in enumerate(lista_palas): #Hago esto para que agarre lo que necesito nada más.
           lista_palas[i] = j.strip(": \n").split(" ")
       mis_links = []
       for pala in lista_palas:
           if "/" in pala[0]:
               mis_links.append("https://dx.doi.org/" + pala[0][:-1])
       return mis_links

#Lo pongo así porque no se cómo importarlo :(

def separar_texto(texto):
    lista_pala = texto.split(" ")
    for i,pala in enumerate(lista_pala): #Saco los puntos y comas de las palabras.
        if len(pala)>=1:
            if pala[-1] in [".", ",", ":"]:
                lista_pala[i] = pala[:-1] 
            lista_pala[i] = (pala.strip()).lower()
    # Hago esto para quitar los espacios en blanco
    palabras = [x for x in lista_pala if len(x)>0]
    return palabras

def generar_dic_fil(texto, palabras_filtro, n):
    palas = []
    frec = []
    for pala in texto:
            if pala not in palas:
                palas.append(pala)
                frec.append(1)
            else:
                frec[palas.index(pala)] += 1
    if n<= 0:
        n = len(palas)  - len(palabras_filtro)
    diccio = {}
    i= 0
    while i<n:
        # Agrego al diccionario la palabra con mayor frecuencia de la lista.
        indi_frec  = frec.index(max(frec))
        frecu = frec.pop(indi_frec)
        pala = palas.pop(indi_frec)
        if pala not in palabras_filtro and len(pala)>3:
            diccio[pala] = frecu 
            i += 1
    return diccio

def histo_wordcloud(texto, palabras_filtro, nom_cloud):
    new_data = separar_texto(texto)
    frec_pals = generar_dic_fil(new_data, palabras_filtro, 20)
    # Histograma.
    # palabras = pd.DataFrame.from_dict({"Frecuencia": frec_pals})
    # sns.barplot( x=palabras.index , y=palabras["Frecuencia"], errwidth=100)
    # plt.xticks(rotation="90")
    # plt.show()
    
    wordcloud = WordCloud(width=480, height=480, margin=0)
    wordcloud.generate_from_frequencies(frec_pals)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.savefig(nom_cloud) #Esto es para guardar la wordcloud. 
    # plt.show()
    

    
   # Ejercicio 12
def parse_paper_data(papers):
    with open("data_necesaria/common_words.txt", "rt", encoding="utf8") as f2:
        r = f2.read()
        filtro = r.split("\n")
        filtro.extend(["*", "=","acad"])
        filtro.extend(list(range(100)))
    #Es un archivo que encontre por Internet con las más 1000 palabras más frecuentes, copa3.
    
    with open("papers/papers_unidos" + str(papers) + ".txt", "w", encoding="utf-8") as new_file:
        for x in range(1,papers):    
            paper = str(x)
            with open("papers/paper_numero" + str(paper) + ".txt", "rt", encoding="utf-8") as file:
                f = file.read()
                histo_wordcloud(f, filtro, "nube_paper" + str(paper) ) # Acá también guardo la nube
                new_file.write("\n" + f) #Acá voy agregando la data de los papers a un paper más grande.
    # Ahora lo vuelvo a abrir pero para leerlo
    with open("papers/papers_unidos" + str(papers) + ".txt", "r", encoding="utf-8") as new_file1:
        papers_unidos = new_file1.read()
        print(" \n \n \n \n \n \n 3 \n \n \n \n \n \n")
        histo_wordcloud(papers_unidos, filtro, "nube_final_papers" + str(papers))


class MessiSpider(scrapy.Spider):
    name = 'messi'
    # allowed_domains = ['prueba.com']
    start_urls = ['https://pubmed.ncbi.nlm.nih.gov/?term=baldness&filter=simsearch2.ffrft&size=10']
    paper = 1

    def parse(self, response):
        paper_totales = 1
        converter=html2text.HTML2Text()
        converter.ignore_links=True
        converter.ignore_images=True
        converter.ignore_tables=True
        texto = converter.handle(response.css('*').get())
        links = extraer_links(self, texto)
        for link in links:
            yield scrapy.Request(link, callback=self.parse_paper)   
            paper_totales += 1
        parse_paper_data(paper_totales) #Acá es donde revisaría la información de los papers
        print ("\n \n \n Analizaste " + str(paper_totales) + " páginas, congrats master \n \n \n")
        # Ya se que no son los papers que analice porque estoy contando las páginas
        # fallidas pero es para tener un contador
    
    def parse_paper(self, response):
        if hasattr(response, "text"):
            converter=html2text.HTML2Text()
            converter.ignore_links=True
            converter.ignore_images=True
            converter.ignore_tables=True
            data = converter.handle(response.css('*').get())
            f = open( "papers/paper_numero" + str(self.paper) + ".txt", "w" , encoding="utf-8")
            f.write(data)
            f.close
            self.paper += 1
        else:
            print("No es una página Html, no se puedo convertir a texto. \n")


