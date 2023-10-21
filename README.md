# WinFileTimeToDate
Convert Windows file time to human readable date
# Windows FILETIME
Windows FILETIME format represents the number of 100-nanosecond intervals that have elapsed since 12:00 A.M. January 1, 1601 Coordinated Universal Time (UTC). File times are recorded when files, directories are created, accessed, modified and are stored in NTFS metadata files like the $MFT, $USNJrnl, $I30 index records as an 8 bytes length hexadecimal value
# Usage 
This script aims to convert an 8 bytes length file time hexadecimal value to a human readable date.

2 arguments need to be provided when executing it:

- The 8 bytes length file time hexadecimal value ordering (Little endian or Big endian)
- The 8 bytes length file time hexadecimal value

This instance convert the big endian file time hexadecimal value "eb88a79041ded701" to a human-readable date:

`python3 WinFileTimeToDate.py -o be -v "eb88a79041ded701"`

Giving the following result:

`2021-11-20 19:05:21.185816`

# References
https://learn.microsoft.com/en-us/windows/win32/sysinfo/file-times
https://docs.python.org/3/library/struct.html
https://en.wikipedia.org/wiki/Endianness