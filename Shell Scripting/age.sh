#!/bin/bash

read -p "Enter age :" age

if [ $age -gt 18 ]
then
	read -p "Do you have voter id ?" voter
	if [ $voter -eq 1 ]
	then
		echo "Eligible to vote "
	else
		echo "Please issue a card"
	fi
else
	n=$((expr 18 - $age))
	echo "You will be eligible after $n years"
fi
