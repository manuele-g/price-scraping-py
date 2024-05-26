def extract_numbers(price):
    float_price = price.replace("€", "")
    float_price = float_price.replace(",", ".")
    return float(float_price)

