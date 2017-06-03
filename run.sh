#!/bin/bash

cflag=''
dflag=0
oflag=''

while getopts ":c:d:o:" opt; do
  case $opt in
    c ) cflag=$OPTARG;;
    d ) dflag=$OPTARG;;
    o ) oflag=$OPTARG;;
    \?) echo "Invalid option: -$OPTARG" >&2; exit 1;;
    : ) echo "Option -$OPTARG requires an argument." >&2; exit 1;;
  esac
done

if [[ -z $cflag ]] || [[ -z $oflag ]]
then
    echo "usage: bash run.sh -c CASE_NUM [-d DEVIATION] -o OUTPUT_FILE" >&2
    exit 1
fi

python -u check_status.py -c $cflag -d $dflag > $oflag
python sort_log.py $oflag

approved="$(grep "Card" "$oflag" | wc -l)"
total="$(cat "$oflag" | wc -l)"

echo "$approved out of $total neighboring cases are approved.
Check output file for details."
