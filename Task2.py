"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

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
"""


def main():
    phone_durations = {}
    for c in calls:
        num_secs = int(c[3])
        # time spent calling
        if c[0] in phone_durations:
            phone_durations[c[0]] += num_secs
        else:
            phone_durations[c[0]] = num_secs
        # time spent answering
        if c[1] in phone_durations:
            phone_durations[c[1]] += num_secs
        else:
            phone_durations[c[1]] = num_secs
    # sort our dictionary by phone durations, highest first, then take the first item
    max_key = sorted(phone_durations, key=phone_durations.get, reverse=True)[0]
    print(f'{max_key} spent the longest time, {phone_durations[max_key]} seconds, on the phone during September 2016.')


if __name__ == '__main__':
    main()
