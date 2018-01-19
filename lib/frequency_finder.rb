class FrequencyFinder
  def character_frequency(sequence)
    sequence.split('').inject(Hash.new(0)) do |total, e|
      total[e] += 1 ; total
    end
  end

  def max_frequency(sequence)
    character_frequency(sequence).values.max
  end

  def most_frequent_characters(sequence)
    character_frequency(sequence).select do |key, val|
      val == max_frequency(sequence)
    end
  end

  def find(sequence)
    if sequence.nil? || sequence.empty?
      return "Please enter a valid string"
    else
      most_frequent_characters(sequence).keys.join(', ')
    end
  end
end