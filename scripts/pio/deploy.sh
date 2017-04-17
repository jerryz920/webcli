#!/bin/bash
echo deploy script

cd ${1:-/pioapp}
pio deploy
