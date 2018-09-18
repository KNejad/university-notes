#!/usr/bin/env sh

i=1
for f in $(ls -t); do
  echo $f$i
  i=$(($i + 1))
done
