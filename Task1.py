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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def main():
    unique_tel_nums = set()
    for t in texts:
        if not t[0] in unique_tel_nums:
            unique_tel_nums.add(t[0])
        if not t[1] in unique_tel_nums:
            unique_tel_nums.add(t[1])
    for c in calls:
        if not c[0] in unique_tel_nums:
            unique_tel_nums.add(c[0])
        if not c[1] in unique_tel_nums:
            unique_tel_nums.add(c[1])
    print(f'There are {len(unique_tel_nums)} different telephone numbers in the records.')


if __name__ == '__main__':
    main()
