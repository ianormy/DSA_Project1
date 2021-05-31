"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

Time Estimate: O(n) - where n is the number of calls recorded
"""


def main():
    max_secs = 0
    max_secs_telno = None
    for c in calls:
        num_secs = int(c[3])
        if num_secs > max_secs:
            max_secs_telno = c[0]
            max_secs = num_secs
    print(f'{max_secs_telno} spent the longest time, {max_secs} seconds, on the phone during September 2016.')


if __name__ == '__main__':
    main()
