"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be printed out one per line in lexicographic order with no duplicates.
"""


def main():
    """
    Time Estimate: O(3n+m) - worst case estimate - where n is the number of calls recorded and m is the number of texts
    """
    #  first identify all numbers that make outgoing calls
    outgoing_calls = set()
    for call in calls:
        if call[0] not in outgoing_calls:
            outgoing_calls.add(call[0])
    # remove all numbers that receive incoming calls
    for call in calls:
        if call[1] in outgoing_calls:
            outgoing_calls.remove(call[1])
    # remove all numbers that send or receive texts
    for text in texts:
        if text[0] in outgoing_calls:
            outgoing_calls.remove(text[0])
        if text[1] in outgoing_calls:
            outgoing_calls.remove(text[1])
    print('These numbers could be telemarketers: ')
    for code in sorted(outgoing_calls):
        print(f'{code}')


if __name__ == '__main__':
    main()
