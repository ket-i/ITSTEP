import requests

# Send a GET request to the API
url = "https://fakestoreapi.com/products"
response = requests.get(url)


if response.status_code == 200:
    products = response.json()

    # ა) შექმენით პროდუქტის ფასების სია და გამოიტანეთ როგორც მაქსიმალური ასევე მინიმალური და სასშუალო ფასები
    prices = list(product['price'] for product in products)
    max_price = max(prices)
    min_price = min(prices)
    average_price = sum(prices) / len(prices)
    print(f"Maximum price: {max_price}")
    print(f"Minimum price: {min_price}")
    print(f"Average price: {average_price}")

    # bბ) შექმენით კატეგორიების სია (დუბლიკაციების გარეშე) და დაასორტირეთ 
    categories = sorted(list(set(product['category'] for product in products)))
    print("Categories:")
    for category in categories:
        print(category)

    # გ) შექმენით სია რომელშიც გექნებად პროდუქტის აღწერა (title) და id. დაასორტირეთ შედეგი title-ის მიხედვით
    product_info = sorted([(product['title'], product['id']) for product in products], key=lambda x: x[0])
    print("Sorted Product Info:")
    for title, product_id in product_info:
        print(f"Title: {title}, ID: {product_id}")

    # დ) შემქენით რეიტინგების სია რომელიც იქნება დასორტირებული ("rate"-ის მიხედვით) ზრდადობით
    ratings = sorted([product['rating']['rate'] for product in products])
    print("Sorted Ratings:")
    print(ratings)
