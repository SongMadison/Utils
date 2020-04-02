#!/bin/bash
echo ">>>>> test how to use 'eval' to handle complicated command"
i=5 
command='echo $i' 
eval "$command"

echo ">>>>> Testing the how to take parameters in shell, need 2 parameters"
first_input=$1
second_input=$2
echo "first input:" $1
echo "second input:" $2
echo $1$2
