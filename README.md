# poll-bot
A discord bot for polls as a self hosted alternative to sites like strawpoll

# Installing dependencies
To start off you should have `python3` and `pip` installed. In case you don't have those, get them via your packet manager.
Any additional dependencies are listed in the `dependencies.txt` file, to install those simply run the command
```
pip install -r dependencies.txt
```
after making sure you have `pip` installed.

# Execution
There are different ways of executing the bot
* The most basic is to run it directly with python: `python3 src/main.py`
* For more convinience I suggest you use the shell script `deploy.sh` instead
  * This script will allow the bot to be restarted from discord, which might be faster than accessing the host machine
  * Running it using the flag `-u` will pull the newest version from github whenever the bot is restarted via the discord command
  * Running it using the flag `-d` will check if any new dependencies where added with newer updates
    * Since this flag invokes `pip` you should run this with `sudo` or as root
