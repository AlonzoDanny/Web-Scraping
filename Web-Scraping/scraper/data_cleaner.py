def clean_price(price_str):
    # Limpiar el precio, eliminando símbolos o espacios innecesarios
    return price_str.replace('$', '').replace(',', '').strip()
