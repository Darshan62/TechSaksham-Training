#!/bin/bash 

read -p "Enter number 1:" n1
read -p "Enter number 2:" n2
read -p "Enter number 3:" n3
if [ $n1 -gt $n2 ]
then
	if [ $n1 -gt $n3 ]
	then
		echo "$n1 is gretest"
		exit
	else
		echo "$n3 is greatest"
	fi
else
 	if [ $n2 -gt $n3 ]
	then
		echo "$n2 is greates"
		exit
	else
		echo"$n3 is greatest"
	fi
fi
