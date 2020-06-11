# inheritance

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"


class Sneaker(Product):
    def __init__(self, name, price, shoe_size, brand):
        super().__init__(name, price)
        # ^ What we get from Product ^
        self.shoe_size = shoe_size
        self.brand = brand
        self.discount = 0


class SoccerBall(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} WILSONN'

    def kick(self):
        print("The ball is gone")


generic_product = Product("Generic", "99.99")
print(generic_product)

nike_free = Sneaker("Nike Free", "100", "10", "Nike")
soccer_ball = SoccerBall("Wilson", "20", "Rubber")
# soccer_ball.discount = 10

print(nike_free)
print(soccer_ball)
print(soccer_ball.kick())

# print(nike_free.name)
# print(nike_free.price)
# print(nike_free.brand)
# print(soccer_ball.name)
# print(soccer_ball.price)
# print(soccer_ball.material)
# print(soccer_ball.discount)
