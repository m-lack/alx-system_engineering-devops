#!/usr/bin/env ruby
puts ARGV[0].scan(/([a-zA-Z])\1+/).join

