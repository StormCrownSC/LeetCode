class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        maximise = 0
        if x < y:
            maximize = y
        else:
            maximize = x
        count = 1
        while True:
            if maximize < 2**count:
                maximize = 2**count
                break
            count += 1
        x = self.transform(x, count)
        y = self.transform(y, count)
        answer = 0
        for i in range(count):
            if x[i] != y[i]:
                answer += 1
        return answer
        
        
    def transform(self, n, count):
        answer = ""
        while n >= 1:
            answer += str(n % 2)
            n //= 2
        while len(answer) < count:
            answer += "0"
        return answer[::-1]

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

"""