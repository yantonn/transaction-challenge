from service.file_loader.txt.transaction import TransactionTXTLoader

DEFAULT_TYPE_RESOLVE_LOADER = 'txt'


class FileResolveProvider:

    def __init__(self, type_resolve_loader: str = DEFAULT_TYPE_RESOLVE_LOADER):
        self.__type_resolve_loader = type_resolve_loader

    def get_loader(self):
        if self.__type_resolve_loader == DEFAULT_TYPE_RESOLVE_LOADER:
            return TransactionTXTLoader()
