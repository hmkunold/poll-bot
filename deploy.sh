#!/bin/bash

# initializing status variables, default is 0, i.e false
updates=0
dependencies=0

# checking flags
while getopts "hud" flags
do
	case $flags in
		h)
			echo "Script for bot deployment"
			echo "Allows the bot to restartd and potentially update just from discord commands"
			echo "-h	help, shows this page"
			echo "-u	pull updates from github"
			echo "-d	check dependencies when updating, will probably require root privileges"
			exit
			;;
		u)
			updates=1
			echo "Checking github for updates"
			;;
		d)
			dependencies=1
			echo "checking for new dependencies"
			;;
	esac
done

# deployment loop
while true; do
	if [ $updates == 1 ]
	then
		echo "Checking github for upodates"
		git pull
	fi

	if [ $dependencies == 1 ]
	then
		echo"Checking for new dependencies"
		pip install -r dependencies.txt
	fi

	python3 src/main.py --restart
done
