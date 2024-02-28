#!/usr/bin/env ruby
sender = ARGV[0][/from:([^\]]+)/, 1]
receiver = ARGV[0][/to:([^\]]+)/, 1]
flags = ARGV[0][/flags:([^\]]+)/, 1]

# Output the extracted values
puts "#{sender},#{receiver},#{flags}"
  