import requests

def search_mercado_livre(query):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"
    response = requests.get(url)
    data = response.json()
    products = []
    for item in data.get("results", []):
        products.append({
            "title": item["title"],
            "link": item["permalink"],
            "image": item["thumbnail"],
            "current_price": item["price"]
        })
    return products