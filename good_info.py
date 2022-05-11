class Good:
    """Represent good."""
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        if self == other:
            self.count += other.count
        else:
            print("Different goods!")

    def __str__(self):
        return f'Товар: {self.name }, цена: {self.price}, количество: {self.count}'


class Goods:
    """Represents coection of goods."""
    def __init__(self):
        self.value = []

    def add(self, good):
        self.value.append(good)

    def get_from_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as data_file:
            data = data_file.readlines()
            for item in data:
                item.replace('\n', '')
                good_list = item.split(':')
                good_name = good_list[0]
                good_price = float(good_list[1])
                good_count = int(good_list[2])
                good = Good(good_name, good_price, good_count)
                self.add(good)

    def __str__(self):
        return '\n'.join([str(x) for x in self.value])


# goods = Goods()
# goods.get_from_file('goods.txt')
# print(goods)
