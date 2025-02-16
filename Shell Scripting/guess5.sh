#!/bin/bash

echo "Enter Number"
read n
for((i=4;i>-1;i--))
do
	if [ $n -lt 69 ]
	then
		echo "less"
	elif [ $n -gt 69 ]
	then
		echo "Too much"
	else
		echo "69  is correct"
		exit
	fi
	echo "$i chances left "
	echo "Enter Number "
	read n
done
