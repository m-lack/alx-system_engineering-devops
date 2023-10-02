#!/bin/bash

Script 1: List Top Web Server Hosts by Request Count (103-the_biggest_fan):

This script takes web server logs in TSV format as input.
It extracts host or IP addresses, excluding the header line.
Counts the number of requests made by each host or IP address.
Sorts the hosts or IP addresses by request count in descending order.
Displays the top 11 hosts or IP addresses that made the most requests.
Alternative Script 1: List Top Web Server Hosts by Request Count (Alternative without awk or sed):

An alternative version of the previous script that achieves the same goal without using awk or sed.
Extracts host or IP addresses, excludes the header line, and counts requests using standard Unix utilities.
Sorts and displays the top 11 hosts or IP addresses by request count.
Script 2: Decode Acrostics from Text (102-acrostic):

This script decodes acrostics, where the first letter of each line spells out a word.
Takes text input and identifies the word spelled by the acrostic.
The decoded word is displayed, followed by a newline.
Alternative Script 2: Decode Acrostics from Text (Alternative without awk or sed):

An alternative version of the acrostic decoding script that accomplishes the same task without using awk or sed.
Script 3: Find Most Active Web Servers (103-the_biggest_fan):

This script takes web server logs in TSV format as input.
Extracts host or IP addresses and counts the number of requests.
Sorts and displays the top 11 hosts or IP addresses with the most requests.
Alternative Script 3: Find Most Active Web Servers (Alternative without awk or sed):

An alternative version of the previous script that achieves the same goal without using awk or sed.
Script 4: List Empty Files and Directories (100-empty_casks):

This script finds and lists empty files and directories in the current directory and its subdirectories.
Displays the names of empty files and directories, including hidden ones, with one name per line.
Alternative Script 4: List Empty Files and Directories (Alternative without find):

An alternative version of the previous script that accomplishes the same task without using find.
Script 5: List .gif Files in Current and Subdirectories (101-gifs):

This script finds and lists all .gif files in the current directory and its subdirectories.
Sorts the file names by byte values in a case-insensitive manner and displays one name per line.
Alternative Script 5: List .gif Files in Current and Subdirectories (Alternative without find and sort):

An alternative version of the previous script that achieves the same goal without using find and sort.
Script 6: Display Users and Home Directories from /etc/passwd (22-users_and_homes):

Reads the /etc/passwd file to extract user names and their corresponding home directories.
Sorts and displays this information in the format username:home_directory.
Alternative Script 6: Display Users and Home Directories from /etc/passwd (Alternative without awk or sed):

An alternative version of the previous script that accomplishes the same task without using awk or sed.
Script 7: Reverse Input Text (21-reverse):

Takes input text and reverses it, displaying the reversed text.
Alternative Script 7: Reverse Input Text (Alternative without rev):

An alternative version of the reverse script that achieves the same result without using the rev command.
Script 8: Remove Specific Characters from Input (20-hiago):

Removes all occurrences of the characters 'c' and 'C' from the input text and displays the modified text.
Alternative Script 8: Remove Specific Characters from Input (Alternative without tr):

An alternative version of the previous script that accomplishes the same task without using the tr command.
Script 9: Replace Specific Characters in Input (19-AZ):

Replaces all occurrences of the character 'A' with 'Z' and 'c' with 'e' in the input text and displays the modified text.
Alternative Script 9: Replace Specific Characters in Input (Alternative without sed):

An alternative version of the previous script that achieves the same goal without using sed.
Script 10: Display Lines Containing a Pattern (17-hidethisword):

Displays all lines from a file (/etc/passwd) that do not contain the pattern "bin."
Alternative Script 10: Display Lines Containing a Pattern (Alternative without grep):

An alternative version of the previous script that accomplishes the same task without using grep.
Script 11: Display Lines Containing a Pattern and 3 Lines After (16-whatsnext):

Displays lines from a file (/etc/passwd) containing the pattern "root" and the three lines following each occurrence.
Alternative Script 11: Display Lines Containing a Pattern and 3 Lines After (Alternative without grep):

An alternative version of the previous script that achieves the same result without using grep.

