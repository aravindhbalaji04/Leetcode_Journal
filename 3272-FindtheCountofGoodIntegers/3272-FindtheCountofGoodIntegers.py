# Last updated: 12/4/2025, 8:54:41 am
from math import pow
from collections import defaultdict
class Solution:
    def __init__(self):
        self.factorialArr = [1] * 11
        for idx in range(1, 11):
            self.factorialArr[idx] = self.factorialArr[idx - 1] * idx
    def generatePalindromes(self, digitCount):
        palindromeList = []
        if digitCount == 0:
            return palindromeList
        halfLen = (digitCount + 1) // 2
        startNum = int(pow(10, halfLen - 1))
        endNum = int(pow(10, halfLen)) - 1
        if digitCount == 1:
            startNum = 0
        for firstHalf in range(startNum, endNum + 1):
            halfStr = str(firstHalf)
            if digitCount % 2 == 0:
                fullPalindrome = halfStr + halfStr[::-1]
            else:
                fullPalindrome = halfStr + halfStr[-2::-1]
            if len(fullPalindrome) == digitCount:
                palindromeNum = int(fullPalindrome)
                palindromeList.append(palindromeNum)
        return palindromeList
    def countDigits(self, number, digitCount):
        digitFreq = [0] * 10
        numStr = str(number).zfill(digitCount)
        for digit in numStr:
            digitFreq[int(digit)] += 1
        return digitFreq
    def calculatePermutations(self, digitFreq, digitCount):
        permutationCount = 0
        for digit in range(1, 10):
            if digitFreq[digit] == 0:
                continue
            adjustedFreq = digitFreq[:]
            adjustedFreq[digit] -= 1
            isValid = all(freq >= 0 for freq in adjustedFreq)
            if not isValid:
                continue
            validPermutations = self.factorialArr[digitCount - 1]
            for freq in adjustedFreq:
                validPermutations //= self.factorialArr[freq]
            permutationCount += validPermutations
        return permutationCount
    def countGoodIntegers(self, digitCount, divisor):
        palindromeList = self.generatePalindromes(digitCount)
        validPalindromes = [palindrome for palindrome in palindromeList if palindrome % divisor == 0]
        uniqueDigitFreq = set(tuple(self.countDigits(validPalindrome, digitCount)) for validPalindrome in validPalindromes)
        totalGoodIntegers = 0
        for digitFreq in uniqueDigitFreq:
            totalGoodIntegers += self.calculatePermutations(list(digitFreq), digitCount)
        return totalGoodIntegers