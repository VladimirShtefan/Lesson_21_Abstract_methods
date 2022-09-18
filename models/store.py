from models.base_storage import BaseStorage


class Store(BaseStorage):
    __storage_name__ = 'склад'

    def __init__(self, items: dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)
        self.__items = items
        self.__capacity = capacity

    def get_storage_name(self) -> str:
        return self.__storage_name__
