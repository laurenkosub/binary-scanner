bscanner is an application that reports information about ELF x86-64 binaries. This analysis is displayed to the user through the command line interface and stored to a file for future retrieval and analysis.  The application only analyzes binaries built in the ELF64 format for an intel architecture, and files that are not ELF x86-64 files are not be analyzed beyond identifying that it is not an ELF64 file for an intel architecture. 

Usage: ./binscan [-u <username> | -a] -p <password> -f <file> -t <type>

Data displayed:
- SHA1 Hash of .init section
- Instructions and instruction counts
- Renyi Quadratic Entropy
- External functions and external function counts
- section names and section sizes in bytes
