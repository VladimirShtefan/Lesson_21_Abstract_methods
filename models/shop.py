from models.base_storage import BaseStorage
from exceptions import ErrorOverload


class Shop(BaseStorage):
    __storage_name__ = 'магазин'

    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)
        self.__items = items
        self.__capacity = capacity
        # self.__storage_name = 'магазин'

    def add(self, name: str, amount: int) -> None:
        if self.__items.get(name) not in self.__items.values() and self.get_unique_items_count() == 5:
            raise ErrorOverload(self.__storage_name__)
        super(Shop, self).add(name, amount)

    def get_storage_name(self) -> str:
        return self.__storage_name__
