#!/bin/bash
source env/bin/activate
until ./etehadiran_bot.py; do
    echo "'etehadiran_bot.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
