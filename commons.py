class Product:
    def __init__(self, name, space, price):
        self.name = name
        self.space = space
        self.price = price


products = [Product("Big Refrigerator", 0.870, 1199.89),
            Product('Medium Refrigerator', 0.751, 999.90),
            Product("Small Refrigerator", 0.635, 849.00),
            Product('Cell phone', 0.00000899, 2199.12),
            Product("Big Ceiling fan", 0.97, 199.00),
            Product("Small fan", 0.496, 199.90),
            Product('TV 55', 0.400, 4346.99),
            Product("TV 50' ", 0.290, 3999.90),
            Product("TV 42' ", 0.200, 2999.00),
            Product("TV 32'", 0.127, 999.00),
            Product("Microwave", 0.0424, 308.66),
            Product("Electric oven", 0.0544, 429.90),
            Product("Blender", 0.0319, 299.29),
            Product("Tablet", 0.00350, 2499.90),
            Product("Notebook 16'", 0.498, 1999.90),
            Product("Notebook 13'", 0.300, 1999.00),
            Product("Desktop Computer", 0.527, 3999.00),
            Product("Computer monitor", 0.597, 2999.00),
            Product("Matress", 0.27, 99.00),
            Product("2 Pillow pack", 0.27, 69.00)]

product_prices = []
for prod in products:
    product_prices.append(prod.price)
product_spaces = []
for prod in products:
    product_spaces.append(prod.space)
