#!/usr/bin/env ruby

# A regular expression to match the string "School"
# Get the input argument from the command line
# Use the scan method with the regex to find matches in the input
# Join the matched results and print the output

puts ARGV[0].scan(/School/n).join
