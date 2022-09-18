from abc import ABC, abstractmethod


class Storage(ABC):
    __storage_name__ = ''

    @property
    @abstractmethod
    def items(self) -> dict[str, int]:
        pass

    @property
    @abstractmethod
    def capacity(self) -> int:
        pass

    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass

    @abstractmethod
    def get_storage_name(self) -> str:
        pass
