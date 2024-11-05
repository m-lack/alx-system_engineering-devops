#!/usr/bin/env ruby
log = ARGV[0]
sender = log.scan(/from:([^\]]+)/).join
receiver = log.scan(/to:([^\]]+)/).join
flags = log.scan(/flags:([^\]]+)/).join
puts "#{sender},#{receiver},#{flags}"

