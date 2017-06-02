"""
This script is meant to check USCIS case status
through command line. You can either check one
case or several neighboring cases together.

Inspired by Haoran Wang's code from
https://github.com/georgewhr/uscis
it simplifies the request processure.

Usage:
    $ python check_status.py -c CASE_NUM [-d DEVIATION]

Options:
    -c, --case_num
        The unique USCIS case number with 3 letters and 10 digits.
    -d, --deviation
        The number of cases ahead of and after the CASE_NUM.
"""

import argparse, requests, sys, warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore")
URL="https://egov.uscis.gov/casestatus/mycasestatus.do"

def make_request(case_num):
    response = requests.post(URL, data={"appReceiptNum": case_num})
    if response.status_code == 200:
        return response.content

def extract_status(raw):
    soup = BeautifulSoup(raw)
    status_secs = soup.find_all("div", {"class": "current-status-sec"})
    for s in status_secs:
        status = s.get_text()
        if "Your Current Status" in status:
            status = status.replace("Your Current Status:", "") \
            .strip("\n\r\t+ ")
            return status

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--case_num', required=True,
                        type=str, help='Case Number')
    parser.add_argument('-d', '--deviation', required=False, default=0,
                        type=int, help='Number of Cases Ahead and After')
    args = parser.parse_args()
    return args

def calc_cases(case_num, deviation):
    letters, digits = case_num[:3], int(case_num[3:])
    digits_all = range(digits-deviation, digits+deviation+1)
    case_nums = ["%s%d" % (letters.upper(), digits) for digits in digits_all]
    return case_nums

def main():
    args = arg_parser()
    case_nums = calc_cases(args.case_num, args.deviation)
    for case_num in case_nums:
        status = extract_status(make_request(case_num))
        print "%s %s" % (case_num, status or "unknown")

if __name__ == '__main__':
    main()
