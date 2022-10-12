import requests
from bs4 import BeautifulSoup
import spacy

nlp = spacy.load("en_core_web_sm")

def filtro(soup):
    for data in soup(['style', 'script', 'head', 'header', 'meta', '[document]', 'title', 'footer', 'iframe', 'nav']):
        data.decompose()
    return ' '.join(soup.stripped_strings)

url_1 = 'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/'
url_2 = 'https://www.qualtrics.com/experience-management/customer/natural-language-processing/'
url_3 = 'https://www.oanayucel.ro/en/nlp-what-is-it-and-how-can-it-help-you/'
url_4 = 'https://viso.ai/deep-learning/natural-language-processing/'
url_5 = 'https://www.oracle.com/hk/artificial-intelligence/what-is-natural-language-processing/'

urls = [url_1, url_2, url_3, url_4, url_5]

texto_1 = []
texto_2 = []
texto_3 = []
texto_4 = []
texto_5 = []

for url in urls:
  urlAtual = urls.index(url)
  html = requests.get(url).text
  soup = BeautifulSoup(html, 'html.parser')
  texto = filtro(soup)
  pagina = nlp(texto)

  for frase in pagina.sents:
    if urlAtual == 0:
      texto_1.append(frase.text)
    elif urlAtual == 1:
      texto_2.append(frase.text)
    elif urlAtual == 2:
      texto_3.append(frase.text)
    elif urlAtual == 3:
      texto_4.append(frase.text)
    elif urlAtual == 4:
      texto_5.append(frase.text)

print(texto_1)
print(texto_2)
print(texto_3)
print(texto_4)
print(texto_5)