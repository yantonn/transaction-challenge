import inject

from environment import get_type_file_loader
from service.file_loader.base import FileLoader
from service.file_loader.file_resolve_provider import FileResolveProvider


def configure(binder):
    configure_file_loader(binder)


def configure_file_loader(binder):
    type_loader = get_type_file_loader()

    provider = FileResolveProvider(type_loader)

    binder.bind(FileLoader, provider.get_loader())


inject.configure(configure)
