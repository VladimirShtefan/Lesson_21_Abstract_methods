from models.base_storage import BaseStorage
from exceptions import ErrorDeleteItem, ErrorNotAvailable, BaseError
from models.shop import Shop
from models.store import Store


class Transaction:
    def __init__(self, from_store: str, to_store: str, amount: int, product: str):
        self._from_store = from_store
        self._to_store = to_store
        self._amount = amount
        self._product = product

    def start_transaction(self, store_list: tuple[Shop, Store]) -> None:
        store_dict = {}
        for index, store in enumerate(store_list):
            store_dict[store.get_storage_name()] = index
        num_from_store = store_dict[self._from_store]
        num_to_store = store_dict[self._to_store]
        sender: BaseStorage = store_list[num_from_store]
        receiver: BaseStorage = store_list[num_to_store]
        try:
            self._remove_transaction(sender=sender)
            print(f'Нужное количество есть в {sender.get_storage_name()}')
            try:
                self._add_transaction(receiver=receiver)
                print(f'Курьер забрал {self._amount} {self._product} из {sender.get_storage_name()}')
                print(f'Курьер везет {self._amount} {self._product} из '
                      f'{sender.get_storage_name()} в {receiver.get_storage_name()}')
                print(f'Курьер доставил {self._amount} {self._product} в '
                      f'{receiver.get_storage_name()}')
            except BaseError as e:
                print(e.message)
                self._add_transaction(receiver=sender)
        except (ErrorDeleteItem, ErrorNotAvailable) as e:
            print(e.message)
        finally:
            print(f'В {sender.get_storage_name()} хранится:\n'
                  f'{sender.get_items()}\n'
                  f'Свободное место: {sender.get_free_space()}')
            print(f'В {receiver.get_storage_name()} хранится:\n'
                  f'{receiver.get_items()}\n'
                  f'Свободное место: {receiver.get_free_space()}')

    def _remove_transaction(self, sender: BaseStorage) -> None:
        sender.remove(amount=self._amount, name=self._product)

    def _add_transaction(self, receiver: BaseStorage) -> None:
        receiver.add(amount=self._amount, name=self._product)
