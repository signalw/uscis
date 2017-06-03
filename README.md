NOTE: frequent usage of this script might get your IP address locked out by
USCIS for a certain period of time.

File `check_status.py` prints out the status of each case that is supposed to be checked.

```
Usage:
    $ python check_status.py -c CASE_NUM [-d DEVIATION]

Options:
    -c, --case_num
        The unique USCIS case number with 3 letters and 10 digits.
    -d, --deviation
        The number of cases ahead of and after the CASE_NUM.
```

File `run.sh` writes the status of each case into a log file and summarizes the approval rate.

```
Usage:
    $ bash run.sh -c CASE_NUM [-d DEVIATION] -o OUTPUT_FILE

Options:
    -c
        The unique USCIS case number with 3 letters and 10 digits.
    -d
        The number of cases ahead of and after the CASE_NUM.
    -o
        The output file that saves the status of all cases.
```
