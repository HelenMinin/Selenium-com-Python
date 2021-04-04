from selenium.webdriver import Firefox
from urllib.parse import urlparse 

navegador = Firefox()
url = 'https://selenium.dunossauro.live/aula_04_b.html'

navegador.get(url)

url_parseada = urlparse(navegador.current_url)