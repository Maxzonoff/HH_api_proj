import json
from abc import ABC, abstractmethod

class StorageException(Exception):
    pass


class Storage(ABC):

    @abstractmethod
    def get_data(self):
        pass


    @abstractmethod
    def add_data(self):
        pass

class JsonStorage(Storage):

    def __init__(self, file_name: str, ):
        self._file_name = file_name


    def get_data(self) -> dict[str, dict]:
        try:
            with open(self._file_name, 'r') as f:
                data = json.loads(f.read())
        except FileNotFoundError:
            return {}
        if not isinstance(data, dict):
            raise StorageException('Не корректные данные в файле')
        return data

    def add_data(self, data: dict[str, dict]) -> None:
        file_data = self.get_data()
        file_data |= data
        with open(self._file_name, 'w') as f:
            f.write(json.dumps(file_data))


