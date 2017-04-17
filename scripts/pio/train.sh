#!/bin/bash
cd ${1:-/pioapp}
#pio train

if [ -f /spark-discovery ]; then
  addr=`cat /spark-discovery`
  pio train -- --master=spark://$addr
else
  echo "training failure"
  exit 1
fi
