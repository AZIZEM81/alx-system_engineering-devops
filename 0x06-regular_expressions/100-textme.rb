#!/usr/bin/env ruby

log_line = ARGV[0]
regex = /\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/
matches = log_line.match(regex)

if matches
  puts "#{matches[:sender]},#{matches[:receiver]},#{matches[:flags]}"
else
  puts "No match"
end
