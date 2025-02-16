#!/bin/bash

read -p "Enter number :" n
sum =0;

while [ $n -ne 0 ];
do
	dig=$(($n%10))
	sum=$(($sum+$dig))
	n=$(($n/10))
done
echo "Sum=$sum"

