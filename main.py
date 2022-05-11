from good_info import Goods


if __name__ == '__main__':
    file_name = input('Введите путь к файлу:')
    goods = Goods()
    goods.get_from_file(file_name)
    print(goods)

# def get_good_info(file_name):
#     with open(file_name, 'r', encoding='utf-8') as data_file:
#         goods = data_file.readlines()
#     result = []
#     for good in goods:
#         good.replace('\n', '')
#         good_list = good.split(':')
#         good_name = good_list[0]
#         good_price = float(good_list[1])
#         good_count = int(good_list[2])
#         good_dict = {
#             'name': good_name,
#             'price': good_price,
#             'count': good_count
#         }
#         result.append(good_dict)
#
#     return result
#
#
# file_name = input('Введите путь к файлу:')
# good_info = get_good_info(file_name)
# print(good_info)

# good_info = f'Товар:{good_name}. Цена:{good_price:.02f}. Количество:{good_count}\n'
# print(good_info)




