from selenium.webdriver import Firefox

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

def find_by_href(navegador, link):
    """Encontrar o elemento `a` com o texto `link`

    Argumentos: 
        - Navegador = Instancia do browser [firefox, chrome, etc...]
        - link = link que será procurado em todas as tags `a`
    """
    elementos = navegador.find_elements_by_tag_name('a') 


    for elemento in elementos:
        if link in  elemento.get_attribute('href'):
            return elemento

navegador = Firefox()
url = 'https://selenium.dunossauro.live/aula_04_a.html'

navegador.get(url)

elemento_ddg = find_by_text(navegador, 'li', 'DuckDuckGo')

elemento_ddg_href = find_by_href(navegador, 'ddg') 