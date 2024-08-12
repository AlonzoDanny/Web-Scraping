import requests
from bs4 import BeautifulSoup


URL = 'https://www.pacifiko.com/compras-en-linea/laptop-lenovo-ideapad-3-15-6-pulgadas-fhd-touch-core-i5-1155g7-8gb-ram-512gb-ssd-w11h-intel-iris-xe-teclado-ingles-color-azul-abismo&pid=NWZlZDhhYW'

if __name__ == '__main__': 

    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text # str

        soup = BeautifulSoup(content, 'html.parser')

        productos = []

        for product in soup.find_all('body', class_='product-product ltr layout-16 loaded'):
            Nombre = product.find('div', class_='title-product').get_text()
            cantidad = product.find('div', class_='input-group quantity-control').get_text()
            Precio =  product.find('span', id='price-special').get_text()
                

            productos.append({
                'Nombre': Nombre,
                'cantidad': cantidad,
                'Precio': Precio
            })   
            
        for producto in productos:
            print(f"producto: {producto['nombre']}")
            print(f"cantidad: {producto['cantidad']}")
            print(f"precio: {producto['precio']}")
            print('-' * 20)


    else: 
        print(f'Error al acceder a la página: {response.status_code}')