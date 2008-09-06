
class Converter(object):
    def __init__(self, source_language, target_language):
        self.source_language = source_language
        self.numeric_source_language = {}
        self.target_language = target_language
        self.numeric_target_language = {}
        self.source_base = len(self.source_language)
        self.target_base = len(self.target_language)
        self.initiate()

    def initiate(self):
        for i in range(len(self.source_language)):
            self.numeric_source_language[self.source_language[i]] = i

        for j in range(len(self.target_language)):
            self.numeric_target_language[j] = self.target_language[j]

    def convert(self, number):
        decimal_number = self.getDecimalNumber(number)
        return self.getTargetNumber(decimal_number)

    def getDecimalNumber(self, number):
        decimal_number = 0
        size = len(number)
        for k in range(size):
            decimal_number += (self.numeric_source_language[number[k]]) * pow(self.source_base,(size - k -1))
        return decimal_number

    def getTargetNumber(self, decimal_number):
        intermediate_number = []
        while (decimal_number >= self.target_base):
            intermediate_number.append(decimal_number % self.target_base)
            decimal_number = decimal_number / self.target_base
        intermediate_number.append(decimal_number)

        target_number = ""
        l =len(intermediate_number)
        while l > 0:
            l -= 1
            target_number += str(self.numeric_target_language[intermediate_number[l]])
        return target_number
