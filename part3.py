class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        return f"{self.name}: {self.description}"


class Store:
    # attributes
    # name
    # categories (departments)

    # constructor
    # self referes to the current instance of the class(in JS is 'this')
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
        self.employees = []

    def __str__(self):
        # return a new string
        output = f"Welcome to {self.name}"
        for category in self.categories:
            output += f'\n {category}'
            return output

        # return f"Welcome to {self.name}: Here are the categories: {self.categories}"

    def __repr__(self):
        return f"self.name = {self.name}  ; self.categories = {self.categories}"


running_category = Category("Running", "All your runner needs", [])

sports_store = Store("Gander Mountain", [running_category])


print(sports_store)
# print(repr(sports_store))


# REPL - READ, Evalute, Print, Loop
