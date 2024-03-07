#! /bin/bash

LISTA=$1
CONV=$2
S0="DIREITO"
S1="NOTURNO"
S2="AMPLA"

if [ -f $LISTA ] 
then
    cat $1 | grep $S0 | grep $S1 | grep -c -i $S2  > $CONV
else
    echo "Não existe"
fi
