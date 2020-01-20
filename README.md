# gnucash_general_journal
* Extract a [General Journal](https://en.wikipedia.org/wiki/General_journal)
* output a CSV file
* **one line per transaction**, all debits and credits spread through columns
* **one column per account**
* The first numeric column, "TRANSACTION AMOUNT", is the absolute value of the "raw" transaction (like in a classic General Ledger)
* account names are preppended with the currencey symbol

The "one column per account, one line per transaction" model captures details of every transaction including all [splits](https://www.gnucash.org/docs/v3/C/gnucash-guide/txns-registers-txntypes.html) and allows for a third party not using GnuCash to have an overview of all transactions and accounts, and work directly in a spreadsheet, for example calculating and account balance by doing a sum of that column.

## Example
|Date|Description|TRANSACTION AMOUNT|CAD Big Bank|CAD GST collected|CAD GST Paid|CAD Revenue|CAD Prof dev|CAD openning balances|
|:---|:---|:---|:---|:---|:---|:--|:---|:---|
|2038-01-01|Opening Balance bank accnt|500|500|||||-500|
|2038-02-28|Work|105|105|-5||-100|||
|2038-04-01|Accounting 101 book|21|-21||1||20||

## Install
```bash
sudo pip3 install virtualenv
cd gnucash_general_journal
virtualenv .
. ./bin/activate
pip3 install -r ./requirements.txt
```

## Notes
* There is now an additional column, "TRANSACTION AMOUNT" which is the absolute value of the transaction. This makes it easier to import as a General Ledger.
* [piecash](https://github.com/sdementen/piecash) is set at version 0.19.0 in order to work with GnuCash versions 2.x.
* this script works with GnuCash SQLite3 files only. If your data is saved in XML format, you can convert it by opening it GnuCash and "Save as" in SQLITE format (You will need `libdbd-sqlite3` to be installed).

## Usage
    ./t2csv.py accounting-sqlite3.gnucash general_journal.csv

## Questions / issues
###### Message about requests and yahoo
It prints the message "You need to install requests to use the 'yahoo' import". This comes from importing piecash, you can safely ignore.

## Dependencies
* [piecash](https://github.com/sdementen/piecash)

## TODO
* add simple sqlite3 file and simple tests
* eliminate the Requests/yahoo warning

