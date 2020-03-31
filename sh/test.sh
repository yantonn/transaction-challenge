#!/usr/bin/env bash
export SRC_PATH="$( dirname "${BASH_SOURCE[0]}" )"

. $SRC_PATH/setenv.sh && export PYTHON_ENV=unittest && pytest $SRC_PATH/../test/unit
error=$?

if [ $error -ne 0 ] ; then 
  echo "Unit test fail, check log in console for more information" 
  exit 1 
fi
