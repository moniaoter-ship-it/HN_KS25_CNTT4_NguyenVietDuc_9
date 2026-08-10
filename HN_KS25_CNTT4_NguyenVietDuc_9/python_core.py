import re


raw_products = [
    {"sku": "SP001", "name": "Áo thun livestream", "price": 250000, "stock": 50, "status": "active"},
    {"sku": " sp002 ", "name": "Quần jean", "price": 450000, "stock": 30, "status": "active"},
    {"sku": "SP003", "name": "Giày thể thao", "price": 1200000, "stock": 20, "status": "inactive"},
    {"sku": "SP004", "name": "Váy công sở", "price": 680000, "stock": 15, "status": "sold_out"},
    {"sku": "SP005", "name": "Kính mát", "price": 350000, "stock": 45, "status": "active"},
]


def clean_and_validate_products(products):
    result = []
    pattern = re.compile(r"^[A-Z]\d{2,}$")

    for product in products:
        item = product.copy()
        sku = str(item.get("sku", "")).strip().upper()

        if pattern.fullmatch(sku):
            item["sku"] = sku
            result.append(item)

    return result


def search_products(products, max_price, status=None):
    result = []

    for product in products:
        if product["price"] <= max_price:
            if status is None or product["status"] == status:
                result.append(product)

    return result


def sort_products_by_stock_asc(products):
    result = products.copy()

    for i in range(len(result) - 1):
        for j in range(len(result) - 1 - i):
            if result[j]["stock"] > result[j + 1]["stock"]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


if __name__ == "__main__":
    products = clean_and_validate_products(raw_products)

    print("Dữ liệu sau chuẩn hóa:")
    print(products)

    print("\nTìm kiếm:")
    print(search_products(products, 500000, "active"))

    print("\nBubble Sort:")
    print(sort_products_by_stock_asc(products))
