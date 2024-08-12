import requests
from bs4 import BeautifulSoup

URL = 'https://www.pacifiko.com/compras-en-linea/laptop-lenovo-ideapad-3-15-6-pulgadas-fhd-touch-core-i5-1155g7-8gb-ram-512gb-ssd-w11h-intel-iris-xe-teclado-ingles-color-azul-abismo&pid=NWZlZDhhYW'

if __name__ == '__main__':
    
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text  # str
        soup = BeautifulSoup(content, 'html.parser')

        # Buscar el elemento con clase 'title-product'
        nombre = soup.find('div', class_='title-product')
        cantidad = soup.find('div', class_='input-group quantity-control') 
        precio = soup.find('span', id='price-special')

        if nombre:
            print(nombre.get_text())
            print(cantidad.get_text())
            print(precio.get_text())
        else:
            print("No se encontró el elemento 'h1' con la clase 'title-product'")
    else: 
        print(f'Error al acceder a la página: {response.status_code}')
