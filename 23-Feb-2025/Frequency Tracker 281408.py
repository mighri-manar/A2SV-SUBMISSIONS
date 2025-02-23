# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:
    def __init__(self):
        self.count = Counter()      
        self.frequencies = Counter() 

    def add(self, number):
        old_f = self.count[number]
        self.count[number] += 1
        new_f = self.count[number]

        if old_f > 0:
            self.frequencies[old_f] -= 1
        self.frequencies[new_f] += 1

    def deleteOne(self, number):
        if self.count[number] > 0:
            old_f = self.count[number]
            self.count[number] -= 1
            new_f = self.count[number]

            self.frequencies[old_f] -= 1
            if new_f > 0:
                self.frequencies[new_f] += 1
            else:
                del self.count[number]  

    def hasFrequency(self, frequency):
        return self.frequencies[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)