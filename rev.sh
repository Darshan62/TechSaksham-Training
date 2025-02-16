#!/bin/bash

read -p "Enter number :" num

rev =0
while [ $num -ne 0 ];
do
	dig=$((num%10))
	rev=$((rev*10))
	rev=$((rev+dig))
	num=$((num/10))
done
echo "Rev=$rev"
