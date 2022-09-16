from models.request import Request
from models.shop import Shop
from models.storage_enum import StorageEnum
from models.store import Store
from models.transaction import Transaction

shop = Shop({'печеньки': 15,
             'фасоль': 0,
             'колбаса': 0,
             'молоко': 0
             })

store = Store({'печеньки': 20,
               'фасоль': 30,
               'колбаса': 20,
               'драники': 16
               })

if __name__ == '__main__':
    while True:
        user_request = input('Введите запрос:\nОбразец: Доставить 3 печеньки из склад в магазин\nДля выхода введите '
                             'стоп\n')
        if user_request == 'стоп':
            break
        req = Request(user_request, [StorageEnum.Shop.value, StorageEnum.Store.value])
        data = req.parse_data()
        if data:
            transaction = Transaction(**data)
            transaction.start_transaction((shop, store))

