#!/usr/bin/env python3

import piecash
import argparse
import sys
import csv
from collections import defaultdict
import logging

logging.basicConfig(format='==> %(module)s, %(funcName)s %(message)s', level=logging.ERROR)

class debug:
    pass

def sort_extra_fields(rows, extra_fields):
    field_size = defaultdict(lambda :0)
    for r in rows:
        for f in r:
            field_size[f] += 1
    sorted_fields = [ y[0] for y in sorted(field_size.items(), key=lambda x:x[1], reverse=True) ]
    sorted_fields = [ x for x in sorted_fields if x in extra_fields ]
    return sorted_fields

def transaction_to_list(gnucash_file):
    rows = list()
    fields = ['Date', 'Description',]
    extra_fields = list()
    book = piecash.open_book(gnucash_file, readonly=True)
    debug.book = book ####
    transactions = book.transactions
    for t in transactions:
        r = dict()
        r['Date'] = t.post_date
        r['Description'] = t.description
        for s in t.splits:
            account = s.account.commodity.mnemonic + ' ' + s.account.name
            if account not in extra_fields:
                extra_fields.append(account)
            r[account] = s.value
        rows.append(r)
    rows.sort(key=lambda x: x['Date'])
    extra_fields = sort_extra_fields(rows, extra_fields)
    fields.extend(extra_fields)
    return rows, fields

def write_csv(csv_file, rows, fieldnames):
    with open(csv_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

print('\n\n') # Because of the warning about importing request
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('gnucash_file',
                        help='GnuCash sqlite3 file',
                       )
    parser.add_argument('csv_file',
                        help='Output csv file',
                       )
    parser.add_argument('--debug', '-d',
                        action='store_true',
                        help='Debug mode (very verbose)',
                       )
    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    rows, fields = transaction_to_list(args.gnucash_file)
    write_csv(args.csv_file, rows, fields)
    print('Transactions saved in "{}"'.format(args.csv_file))



