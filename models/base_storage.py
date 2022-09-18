from models.abstract_storage import Storage
from exceptions import ErrorOverload, ErrorDeleteItem, ErrorNotAvailable


class BaseStorage(Storage):
    __storage_name__ = ''

    def __init__(self, items: dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    @property
    def items(self) -> dict[str, int]:
        return self.__items

    @property
    def capacity(self) -> int:
        return self.__capacity

    def add(self, name: str, amount: int) -> None:
        if amount > self.get_free_space():
            raise ErrorOverload(self.__storage_name__)
        self.__items[name] = amount if not self.__items.get(name) else self.__items[name] + amount

    def remove(self, name: str, amount: int) -> None:
        if self.__items.get(name) is None:
            raise ErrorDeleteItem(self.__storage_name__)
        if amount > self.__items[name]:
            raise ErrorNotAvailable(self.__storage_name__)
        self.__items[name] -= amount
        # if self.__items[name] == 0:
        #     del self.__items[name]

    def get_free_space(self) -> int:
        all_items = sum([item for item in self.__items.values()])
        return self.capacity - all_items

    def get_items(self) -> dict[str, int]:
        return self.__items

    def get_unique_items_count(self) -> int:
        return len(self.__items)

    def get_storage_name(self) -> str:
        return self.__storage_name__
