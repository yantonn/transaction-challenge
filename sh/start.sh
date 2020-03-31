#!/usr/bin/env bash
export SRC_PATH="$( dirname "${BASH_SOURCE[0]}" )"

. $SRC_PATH/setenv.sh && python $SRC_PATH/../main.py
