class FrequencyFinder

  def most_repeated(sequence)
    count = {}
    arr = sequence.split('')
    arr.each do |char|
       if count.has_key?(char)
         count[char] += 1
       else
         count[char] = 1
       end
    end

    return arr.max_by do |char|
      count[char]
    end
  end
end