from selenium.webdriver import Firefox
from time import sleep

def find_by_text(navegador, tag, text):
    """Encontrar o elemento com o texto 'text'

    Argumentos: 
        - Navegador = Instancia do browser [firefox, chrome, etc...]
        - Conteudo que deve estar na tag
        - tag = tag onde o texto será procurado 
    """
    elementos = navegador.find_elements_by_tag_name(tag) # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


navegador = Firefox()
url = 'https://selenium.dunossauro.live/aula_04_b.html'

navegador.get(url)

nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:  
    find_by_text(navegador, 'div', nome).click()

for nome in nomes_das_caixas: 
    sleep(0.3) 
    navegador.back()

for nome in nomes_das_caixas:
    sleep(0.3)  
    navegador.forward()
