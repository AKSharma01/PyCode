from random import choice

def generateRandomNPairBracket(N):
	lis = []
	l1 = l2 = 0
	for i in range(N*2):
		b = choice('[]')
		if b == '[' and l1 < N:
			l1 = l1 + 1
			lis.append(b)
		elif b == ']' and l2 < N:
			l2 = l2 + 1
			lis.append(b)
		else:
			if l1 == N:
				lis.append(']')
			elif l2 == N : 
				lis.append('[')
	return lis
class balanceBracket:
    def __init__(self):
        self.bracket = []

    def add(self, b):
        self.bracket.append(b)
  
    def remove(self):
        if self.bracket:
            return self.bracket.pop()
    	return 


if __name__ == '__main__':        
	N = int(input("Enter the no of bracket '[]' pair:  "))
	bracket = generateRandomNPairBracket(N)
	print  ''.join(bracket)
	balanced = True
	balance_bracket = balanceBracket()
	for val in bracket:
		if val == '[' :
			balance_bracket.add(val)
		elif not (balance_bracket.remove()):
			balanced = False
			break
	print "Ok" if balanced else "Not Ok"