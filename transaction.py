from base_storage import BaseStorage
from exceptions import ErrorOverload, ErrorDeleteItem, ErrorNotAvailable, BaseError
from shop import Shop
from store import Store


class Transaction:
    def __init__(self, from_store: str, to_store: str, amount: int, product: str):
        self._from_store = from_store
        self._to_store = to_store
        self._amount = amount
        self._product = product

    def start_transaction(self, store_list: tuple[Shop, Store]):
        store_dict = {}
        for index, store in enumerate(store_list):
            store_dict[store.get_storage_name()] = index
        num_from_store = store_dict[self._from_store]
        num_to_store = store_dict[self._to_store]
        sender: BaseStorage = store_list[num_from_store]
        receiver: BaseStorage = store_list[num_to_store]
        try:
            self._remove_transaction(sender=sender)
            try:
                self._add_transaction(receiver=receiver)
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

    def _remove_transaction(self, sender: BaseStorage):
        sender.remove(amount=self._amount, name=self._product)

    def _add_transaction(self, receiver: BaseStorage):
        receiver.add(amount=self._amount, name=self._product)
