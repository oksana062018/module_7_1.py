class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file =  open(self.__file_name, 'r', encoding = 'utf 8')
        assortment = file.read()
        file.close()
        return assortment

    def add(self, *products: Product):
        lists = []  # список названий продуктов в файле
        file = open(self.__file_name, "x+")  #  'x' устанавливает курсор на конец файла
        file.seek(0)

        for line in file:
            list = line.split(',')[0]  # название прод
            lists.append(list)
        for product in products:
            if product.name in lists:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{product}\n')
                lists.append(product.name)
        file.close()

if __name__ == '__main__':

    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2) # __str__
    print(p1)
    print(p3)


    print(s1.get_products())