Requirements
============
you need `libjpeg-dev` and `zlib1g-dev` packages to be installed on your computer, before installing. You should insert the token you got from Telegram Botfather in `etehadiran_bot.py` in line 20.

Install
=======
To make it work, do the following:

    $ git clone https://github.com/Mr0Null/etehadiran_bot.git
    $ cd etehadiran_bot
    $ virtualenv -p python3 --no-site-packages --distribute env
    $ source env/bin/activate
    $ pip3 install -r requirements.txt

Run
===
To run the bot just run:

    $ nohup ./run.sh &

Contributors
============
Thanks to Danial Behzadi who wrote the [main bot](https://gitlab.com/danialbehzadi/rouhani96_bot), however as the repo wasn't in the github, I just copied it in my own created repo :)
