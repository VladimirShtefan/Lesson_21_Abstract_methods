import re

from exceptions import ErrorBadRequest


class Request:
    def __init__(self, request: str, storages: list):
        self._to_storage = None
        self._from_storage = None
        self._amount = None
        self._product = None
        self._request = request
        self._storages = storages

    def _get_data_for_order(self) -> tuple[list, list, str]:
        pattern = '|'.join(self._storages)
        storage = re.findall(f'{pattern}', self._request.lower())
        amount = re.findall('[0-9]+', self._request)
        request = self._request.lower().split()
        if len(request) < 3 or not amount:
            raise ErrorBadRequest()
        product = request[2]
        if len(amount) > 1 or len(storage) != 2 or not amount[0] or len(request) != 7:
            raise ErrorBadRequest()
        if storage[0] == storage[1]:
            raise ErrorBadRequest()
        return storage, amount, product

    def parse_data(self) -> dict:
        try:
            storage, amount, product = self._get_data_for_order()
        except ErrorBadRequest as e:
            print(e.message)
        else:
            self._amount = int(amount[0])
            self._from_storage = storage[0]
            self._to_storage = storage[1]
            self._product = product
            return {'from_store': self._from_storage,
                    'to_store': self._to_storage,
                    'amount': self._amount,
                    'product': self._product
                    }
