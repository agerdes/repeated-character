require 'frequency_finder'

RSpec.describe FrequencyFinder, "#most_repeated" do
  let(:finder) { FrequencyFinder.new }
  context "with varied input" do
    let(:input) { "aaabbcc" }
    let(:answer) { "a" }

    it "returns the most frequent character" do
      expect(finder.find(input)).to eq answer
    end
  end

  context "with the same character repeated" do
    let(:input) { "aaa" }
    let(:answer) { "a" }

    it "returns the most frequent character" do
      expect(finder.find(input)).to eq answer
    end
  end

  context "with no input" do
    let(:input) { "" }
    let(:reject_msg) { "Please enter a valid string" }

    it "returns a message that there was no correct input" do
      expect(finder.find(input)).to eq reject_msg
    end
  end

  context "equally frequent characters" do
    let(:input) { "abc" }
    let(:answer) { "a, b, c" }

    it "returns the  characters repeated equally" do
      expect(finder.find(input)).to eq answer
    end
  end
end