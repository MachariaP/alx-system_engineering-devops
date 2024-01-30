#!/usr/bin/env ruby

# A regular expression to match the string "School"
regex = /School/

# Get the input argument from the command line
input = ARGV[0]

# Use the scan method with the regex to find matches in the input
matches = input.scan(regex)

# Join the matched results and print the output
puts matches.join
