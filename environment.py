#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

__PYTHON_ENV = os.getenv('PYTHON_ENV', 'prod')
__TYPE_FILE_LOADER = os.getenv('TYPE_FILE_LOADER', 'txt')
__TYPE_FILE_WRITER= os.getenv('TYPE_FILE_WRITER', 'txt')
__OPERATIONS_PATH = os.getenv('OPERATIONS_PATH', '/tmp/operations')
__AUTHORIZED_OPERATIONS_PATH = os.getenv('AUTHORIZED_OPERATIONS_PATH', '/temp/authorized')
__FILE_OPERATIONS_NAME = os.getenv('FILE_OPERATIONS_NAME', 'operations.txt')
__FILE_AUTHORIZED_NAME = os.getenv('FILE_AUTHORIZED_NAME', 'authorized.txt')


def get_python_env() -> str:
    """
    Retorna o valor da variável __PYTHON_ENV ou seu default 'prod'
    """
    return __PYTHON_ENV


def get_type_file_loader() -> str:
    """
    Retorna o valor da variável __TYPE_FILE_LOADER ou seu default: 'txt'
    """
    return __TYPE_FILE_LOADER


def get_type_file_writer() -> str:
    """
    Retorna o valor da variável __TYPE_FILE_WRITER ou seu default: 'txt'
    """
    return __TYPE_FILE_WRITER


def get_read_operations_path() -> str:
    """
    Retorna o valor da variável __READ_OPERATIONS_PATH ou seu default '/temp/operations'
    """
    return __OPERATIONS_PATH


def get_authorized_path() -> str:
    """
    Retorna o valor da variável __AUTHORIZED_OPERATIONS_PATH ou seu default: '/temp/authorized'
    """
    return __AUTHORIZED_OPERATIONS_PATH


def get_file_operations_name() -> str:
    """
    Retorna o valor da variável __FILE_OPERATIONS_NAME ou seu default: 'operations.txt'
    """
    return __FILE_OPERATIONS_NAME


def get_file_authorized_name() -> str:
    """
    Retorna o valor da variável __FILE_AUTHORIZED_NAME ou seu default: 'authorized.txt'
    """
    return __FILE_AUTHORIZED_NAME
