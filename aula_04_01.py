from selenium.webdriver import Firefox

navegador = Firefox()
url = 'https://selenium.dunossauro.live/aula_04_a.html'

navegador.get(url)

lista_nao_ordenada = navegador.find_element_by_tag_name('ul')

lis = lista_nao_ordenada.find_elements_by_tag_name('li')

lis[0].find_element_by_tag_name('a')
