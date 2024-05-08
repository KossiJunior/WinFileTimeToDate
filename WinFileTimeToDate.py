#!/usr/bin/env python3
# Convert Windows filetime (An Unsigned 64 bits value stored as
# an 8 bytes Hexadecimal value) to an human-readable date

from struct import unpack
from datetime import datetime, timedelta
from argparse import ArgumentParser, ArgumentTypeError, RawDescriptionHelpFormatter

def filetime_hex_to_dec(filetime_hex_value:str, filetime_hex_ordering:str) -> int:
    """Convert a 8 bytes filetime hexadecimal value to a filetime decimal
    value representing the number of 100-nanosecond intervals that have
    elapsed since 12:00 A.M. January 1, 1601 UTC

    :param filetime_hex_value: The filetime hexadecimal value
    :type filetime_hex_value: str
    :param filetime_hex_ordering: The filetime hexadecimal value ordering
    :type filetime_hex_ordering: str
    :returns filetime_dec_value: The filetime value in decimal
    :rtype: int
    """

    ordering_list={
        "le":"<Q", # A 8 bytes value in little endian
        "ge":">Q" # A 8 bytes value in big endian
    }

    filetime_b_hex_value=bytes.fromhex(filetime_hex_value)
    filetime_dec_value=unpack(ordering_list[filetime_hex_ordering], filetime_b_hex_value)[0]

    return filetime_dec_value

def filetime_dec_to_hrdate(filetime_dec_value:int) -> str:
    """Convert filetime decimal value to human-readable date

    :param filetime_dec_value: The filetime value in decimal
    representing the number of 100-nanosecond intervals that
    have elapsed since 12:00 A.M. January 1, 1601 UTC
    :type filetime_dec_value: int
    :returns filetime_hr_datetime_value: The human-readable date of the filetime
    :rtype: str
    """

    filetime_microseconds=filetime_dec_value / 10
    filetime_datetime_obj=datetime(1601,1,1) + timedelta(microseconds=filetime_microseconds)
    filetime_hr_datetime_value=filetime_datetime_obj.strftime('%Y-%m-%d %H:%M:%S.%f')

    return filetime_hr_datetime_value

if __name__ == "__main__":

    example_text = '''example:

    Convert the filetime "01d7de4190a788eb" stored as an 8 Bytes hexadecimal big-endian value to a human-readable date
    python3 %(prog)s -o be -v "01d7de4190a788eb"

    Convert the filetime "01d7de4190a788eb" stored as an 8 Bytes hexadecimal little-endian value to a human-readable date
    python3 %(prog)s -o le -v "eb88a79041ded701"

    Convert the filetime "01d7de4190a788eb" stored as an 8 Bytes hexadecimal big-endian value to a human-readable date
    python3 %(prog)s -v "01d7de4190a788eb"
    '''

    parser=ArgumentParser(description="Convert Windows filetime (Unsigned 8 Bytes value stored as an little/big endian hexadecimal value) to a human-readable date",
                                     epilog=example_text,
                                     formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--value", type=str, help="The 8 Bytes hexadecimal value", required=True)
    parser.add_argument("-o", "--ordering", type=str, help="The hexadecimal value ordering, 'le' for little-endian or 'be' for big-endian",default="be", choices=['le', 'be'])

    args=parser.parse_args()

    if len(args.value) != 16:
        raise ArgumentTypeError('The provided hexadecimal value must be of 8 bytes')

    filetime_dec_value=filetime_hex_to_dec(args.value, args.ordering)
    filetime_hr_datetime_value=filetime_dec_to_hrdate(filetime_dec_value)
    print(filetime_hr_datetime_value)
