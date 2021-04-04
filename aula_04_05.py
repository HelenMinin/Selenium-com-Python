"""
1. Pegar todos os links de aula
  {'nome da aula': 'link da aula'}
2. Navegar até o exercicio 3
  achar a url do exercicio 3 e ir até lá 
"""
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

navegador = Firefox()
url = 'https://selenium.dunossauro.live/aula_04.html'

navegador.get(url)

def get_links(navegador, elemento):
  """
  Pega todos os links dentro de um elemento

  - navegador = Instancia do browser
  - elemento = webelement[aside, main, ...]
  """
  sleep(2)
  elemento = navegador.find_element_by_tag_name(elemento)

  ancoras = elemento.find_elements_by_tag_name('a')

  resultado = {}
  for ancora in ancoras:
    resultado[ancora.text] =  ancora.get_attribute('href')

  return resultado
"""
Parte 1 
"""

aulas = get_links(navegador, 'aside')
pprint(aulas)

"""
Parte 2
"""
exercicios = get_links(navegador, 'main')
pprint(exercicios)

navegador.get(exercicios['Exercício 3'])