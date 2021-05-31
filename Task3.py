"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from typing import AnyStr

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be printed out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def is_bangalore_number(telephone_number: AnyStr) -> bool:
    """Determine if the telephone number is a Bangalore one

    :arg telephone_number: telephone number
    :ret: True if the telephone number is a Bangalore one, otherwise False
    """
    return telephone_number.startswith('(080)')


def is_telemarketers_number(telephone_number: AnyStr) -> bool:
    """Determine if the telephone number is a Telemarketer's one

    :arg telephone_number: telephone number
    :ret: True if the telephone number is a Telemarketer's one, otherwise False
    """
    return telephone_number.startswith('140')


def is_fixed_line(telephone_number: AnyStr) -> bool:
    """Determine if the telephone number is a fixed line

    :arg telephone_number: telephone number
    :ret: True if the telephone number is a fixed line, otherwise False
    """
    # must start with a left parenthesis
    if not telephone_number[0] == '(':
        return False
    # fixed line area codes always begin with '0'
    if not telephone_number[1] == '0':
        return False
    # should only have one left parenthesis
    if telephone_number.rfind('(') != 0:
        return False
    # should only have one right parenthesis
    if telephone_number.find(')') != telephone_number.rfind(')'):
        return False
    return True


def is_mobile_phone_number(telephone_number: AnyStr) -> bool:
    """Determine if the telephone number is a mobile phone

    :arg telephone_number: telephone number
    :ret: True if the telephone number is a mobile phone, otherwise False
    """
    # number must start with a 7, 8 or 9
    if not telephone_number[0] in ['7', '8', '9']:
        return False
    # check the number does not include any parenthesis
    if any([x in telephone_number for x in ['(', ')']]):
        return False
    # check there is only one space
    parts = telephone_number.split(' ')
    if len(parts[0] + parts[1]) != len(telephone_number) - 1:
        return False
    return True


def test_mobile_phone_numbers():
    assert is_mobile_phone_number('78299 99223')
    assert not is_mobile_phone_number('78299  99223')  # too many spaces
    assert not is_mobile_phone_number('68299 99223')  # invalid starting number
    assert not is_mobile_phone_number('7543(080 20')  # contains left parenthesis
    assert not is_mobile_phone_number('854)3080 20')  # contains right parenthesis
    assert not is_mobile_phone_number('1408371942')  # Telemarketing number
    assert not is_mobile_phone_number('(022)47410783')  # landline number


def test_telemarketing_numbers():
    assert is_telemarketers_number('1408371942')  # Telemarketing number
    assert not is_telemarketers_number('78299 99223')  # mobile phone number
    assert not is_telemarketers_number('(022)47410783')  # landline number


def test_fixed_line_numbers():
    assert is_fixed_line('(022)47410783')  # landline number
    assert not is_fixed_line('1408371942')  # Telemarketing number
    assert not is_fixed_line('78299 99223')  # mobile phone number
    assert not is_fixed_line('(44)1234567')  # area code doesn't start with '0'
    assert not is_fixed_line('(044)(0)99223')  # invalid phone number


def run_tests():
    test_mobile_phone_numbers()
    test_telemarketing_numbers()
    test_fixed_line_numbers()


def part_a():
    """
    Find all of the area codes and mobile prefixes called by people
    in Bangalore. In other words, the calls were initiated by "(080)" area code
    to the following area codes and mobile prefixes:
    - Fixed lines start with an area code enclosed in brackets. The area
        codes vary in length but always begin with 0.
    - Mobile numbers have no parentheses, but have a space in the middle
        of the number to help readability. The prefix of a mobile number
        is its first four digits, and they always start with 7, 8 or 9.
    - Telemarketers' numbers have no parentheses or space, but they start
        with the area code 140.

    Print the answer as part of a message:
    "The numbers called by people in Bangalore have codes:"
        <list of codes>
    The list of codes should be printed out one per line in lexicographic order with no duplicates.
    """
    codes = set()
    for call in calls:
        if not is_bangalore_number(call[0]):
            continue
        # call was initiated from a Bangalore number
        if is_mobile_phone_number(call[1]):
            # store mobile phone prefix
            prefix = call[1][:4]
            if prefix not in codes:
                codes.add(prefix)
        if is_telemarketers_number(call[1]):
            if '140' not in codes:
                codes.add('140')
        if is_fixed_line(call[1]):
            end = call[1].find(')')
            prefix = call[1][1:end]
            if prefix not in codes:
                codes.add(prefix)
    print('The numbers called by people in Bangalore have codes:')
    for code in sorted(codes):
        print(f'{code}')


def part_b():
    """
    What percentage of calls from fixed lines in Bangalore are made
    to fixed lines also in Bangalore? In other words, of all the calls made
    from a number starting with "(080)", what percentage of these calls
    were made to a number also starting with "(080)"?

    Print the answer as a part of a message:
    "<percentage> percent of calls from fixed lines in Bangalore are calls
    to other fixed lines in Bangalore."
    The percentage should have 2 decimal digits
    """
    total_calls = len(calls)
    bangalore_calls = 0
    for call in calls:
        if not is_bangalore_number(call[0]):
            continue
        # this is from a Bangalore number
        if is_bangalore_number(call[1]):
            bangalore_calls += 1
    percent_calls = bangalore_calls / total_calls * 100.0
    print('{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(
        percent_calls))


def main():
    part_a()
    part_b()


if __name__ == '__main__':
    main()
