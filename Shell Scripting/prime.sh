#!/bin/bash

read -p "Enter number :" num

c=0;

for ((i=2;i<$num;i++))
do
	n1=$(expr $num % $i )
	if [ $n1 -eq 0 ]
	then
		c=$(($c+1))
	fi
done
if [ $c -eq 0 ]
then
	echo "Number is prime"
else
	echo "Not prime"
fi
