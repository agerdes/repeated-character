require_relative 'lib/frequency_finder'
require 'highline'

def ask_for_a_string(cli)
  str = cli.ask("Please type a string, I'll find the repeating characters.")

  if str.nil? || str.empty?
    ask_for_a_string(cli)
  else
    puts "Thanks! The answer is #{FrequencyFinder.new.find(str)}"
    return
  end
end

ask_for_a_string(HighLine.new)