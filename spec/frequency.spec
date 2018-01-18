require  'frequency_finder'

RSpec.describe FrequencyFinder, "#most_repeated" do
  let(:finder) { FrequencyFinder.new }
  context "with varied input" do
    let(:input) { "aaabbcc" }
    let(:answer) { "a" }

    it "returns the most frequent character" do
      expect(finder.most_repeated(input)).to eq answer
    end
  end
end