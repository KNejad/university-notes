#!/usr/bin/env sh

if [ "$#" -ne 3 ]; then
  echo "3 arguments please!!!"
  exit 1
fi

echo "$1\n$2\n$3" | sort -n
