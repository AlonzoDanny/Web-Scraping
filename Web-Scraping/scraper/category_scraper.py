import requests
from bs4 import BeautifulSoup
from scraper.data_cleaner import clean_price

def scrape_category(url, category_name):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        productos = []
        productoContainer = soup.find('div', class_='products-list')

        if productoContainer: 
            for product in soup.find_all('div', class_='product-item-container'):
                nombre_tag = product.find('div', class_='title-block').find('h4').find('a')
                nombre = nombre_tag.get_text().strip()
                
                #if nombre:
                 #   nombre = "Realiza tu compra en Pacifiko y recibe tu envío en cualquier dirección de Guatemala.   " in nombre
                  #  pass
                #else:
                 #   nombre = nombre
                precio = product.find('div', class_='price').get_text().strip()
                #if precio:
                 #   precio == "Envío GRATIS" in precio
                  #  pass
                #else:
                 #   precio = precio
                imagenes_url = product.find('div', class_='product-image-container').find('img')
                if imagenes_url:
                    imagenes_url = imagenes_url.get('data-src')
                else:
                    imagenes_url = "no disponible"


                productos.append({
                    'Nombre': nombre,
                    'Precio': precio,
                    'Imagen': imagenes_url
                })   

            # Mostrar los productos de la categoría
            print(f"\nCategoría: {category_name}")
            for producto in productos:
                print(f"Nombre: {producto['Nombre']}")
                print(f"Precio: {producto['Precio']}")
                print(f"Imagen: {producto['Imagen']}\n")

        else:
            print(f"No se encontró el contenedor de productos en {category_name}.")
    else: 
        print(f'Error al acceder a la página: {response.status_code}')

