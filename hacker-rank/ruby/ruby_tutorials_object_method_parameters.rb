class Fixnum
    def range? a, b
        return self.between? a, b
    end
end

def range_call(a, b, c)
  low, high = [b, c].min, [b, c].max
  a.between?(low, high).to_s
end

(0...gets.to_i).each do |i|
    a, b, c = gets.strip.split(" ").map(&:to_i)
    puts range_call a, b, c
end