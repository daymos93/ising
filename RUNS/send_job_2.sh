#!/bin/bash 
# Bash script for running njobs time the same physics and saving each run in a directory
 
change_temp()
{
awk  -v tt=$1 'NF!=2 {print $0} NF==2 {$1=tt;print $0}' input.dat > out
mv out input.dat

}


for temp in 2.30 1.00 4.00 

do
    dir=${temp}_temp 
    if [ ! -e $dir ] ; then
        mkdir $dir
    fi

    cp input.dat  $dir
    cp RUN_1 $dir
    cp send_job.sh $dir
    
    cd $dir
    change_temp $temp

    

    ./send_job.sh  # acá va el ejecutable
    cd ../


done
