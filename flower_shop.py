class Flower:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class FlowerShop:
    def __init__(self, flowers):
        self.flowers = flowers

    def get_flower_names(self):
        return [flower.name for flower in self.flowers]

    def get_flower_prices(self):
        return [flower.price for flower in self.flowers]

    def get_flower_price(self, name):
        for flower in self.flowers:
            if flower.name == name:
                return flower.price

        return None

if __name__ == "__main__":
    roses = Flower("roses", 1.50)
    lilies = Flower("lilies", 2.00)
    orchids = Flower("orchids", 2.50)

    flowers = [roses, lilies, orchids]
    flower_shop = FlowerShop(flowers)

    print("Available Flowers:", flower_shop.get_flower_names())
    print("Flower Prices:", flower_shop.get_flower_prices())
    print("Price of Roses:", flower_shop.get_flower_price("roses"))
