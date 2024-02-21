import requests

def parser_csr():
    response = requests.get("https://sf-ecom-api.silpo.ua/v1/uk/branches/00000000-0000-0000-0000-000000000000/products?limit=20&deliveryType=DeliveryHome&category=molochni-produkty-ta-iaitsia-234&includeChildCategories=true&sortBy=popularity&sortDirection=desc&inStock=true")
    items = response.json()
    sirochek = [x for x in items["items"] if x["id"] == "1ed075ec-2f50-6d7c-adc9-dd63763181f9"][0]
    return sirochek['price']

if __name__ == '__main__':    
    print('sirochek price: ', parser_csr())