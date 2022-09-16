class BaseError(Exception):
    def __init__(self):
        self.message = 'Упс, все сломалось'


class ErrorDeleteItem(BaseError):
    def __init__(self, store: str):
        self.message = f'Данного товара нет в базе {store}'


class ErrorOverload(BaseError):
    def __init__(self, store: str):
        self.message = f'{store} переполнен'


class ErrorNotAvailable(BaseError):
    def __init__(self, store: str):
        self.message = f'В {store} нет нужного кол-ва'


class ErrorBadRequest(BaseError):
    def __init__(self):
        self.message = 'Не верный запрос'
