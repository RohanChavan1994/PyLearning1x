products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mobile", "price": 800},
    {"name": "Camera", "price": 600},
    {"name": "Headphones", "price": 400}
]


def is_affordable(item):
    return item["price"] <= 600


affordable_list = list(filter(is_affordable, products))
print(affordable_list)
