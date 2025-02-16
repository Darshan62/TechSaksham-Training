#!/bin/bash

while [ true ]
do
echo -n Enter the count:
read count
if [ $count -eq 42 ]
then
echo "42 is correct"
break
elif [ $count -gt 42 ]
then
echo "Too much"
else
echo "Not enough"
fi
done
echo "Completed



