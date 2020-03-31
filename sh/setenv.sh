#!/usr/bin/env bash
PYTHON_ENV=dev
TYPE_FILE_LOADER=txt
TYPE_FILE_WRITER=txt
OPERATIONS_PATH=/tmp/operations
AUTHORIZED_OPERATIONS_PATH=/tmp/authorized
FILE_OPERATIONS_NAME=operations
FILE_AUTHORIZED_NAME=authorized

export SRC_PATH="$( dirname "${BASH_SOURCE[0]}" )"

export $(cat $SRC_PATH/../.environment | xargs)

echo ""
echo ""
echo "                       python env:" $PYTHON_ENV
echo "                 type file loader:" $TYPE_FILE_LOADER
echo "                 type file writer:" $TYPE_FILE_WRITER
echo "                  operations path:" $OPERATIONS_PATH
echo "       authorized operations path:" $AUTHORIZED_OPERATIONS_PATH
echo "             file operations name:" $FILE_OPERATIONS_NAME
echo "             file authorized name:" $FILE_AUTHORIZED_NAME
echo ""
