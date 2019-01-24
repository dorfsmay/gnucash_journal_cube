# gnucash_general_journal
* Extract a [General Journal](https://en.wikipedia.org/wiki/General_journal)
* output a CSV file
* one line per transaction, each debit and credit spread in columns
* one column per account
* account names are preppended with the currencey symbol

One column per account, one line per transaction captures deatils of every transaction including all [splits](https://www.gnucash.org/docs/v3/C/gnucash-guide/txns-registers-txntypes.html) and allows for a third party not using GnuCash to have an overview of all transactions and account, and letting them work per account directly in a spreadsheet, for example calculating and account balance by doing a sum of that column.

## Example
|Date|Description|CAD Big Bank|CAD GST collected|CAD GST Paid|CAD Revenue|CAD Prof dev|CAD openning balances|
|:--- |:---|:---|:---|:---|:--|:---|:---|
|2038-01-01|Opening Balance bank accnt|500|||||-500|
|2038-02-28|Work|105|-5||-100|||
|2038-04-01|Accounting 101 book|-21||1||20||

## Install
```bash
cd gnucash_general_journal
python3 -m venv .
. ./bin/activate
pip3 install -r ./requirements.txt
```

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

