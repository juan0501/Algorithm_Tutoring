class QuadraticProbing():
	def __init__(self, size):
		self.size = size
		self.hashTable = [None for _ in range(size + 1)]

	def hash(self, key):
		idx = key % self.size

		if self.hashTable[idx] is None:
			return idx
	
		point = 0
		while self.hashTable[(idx + (point**2)) % self.size] != None:
			point += 1
		return (idx + (point * point)) % self.size

	def insert(self, key):
		idx = self.hash(key)
		self.hashTable[idx] = key

	def search(self, key):
		idx = key % self.size
		point = 0

		if self.hashTable[idx] != key:
			while self.hashTable[(idx + (point**2)) % self.size] != key and self.hashTable[(idx + (point**2)) % self.size] != None:
				point += 1

		if self.hashTable[(idx + (point**2)) % self.size] == key:
			return (idx + (point**2)) % self.size
		else: return None


if __name__ == "__main__":
	hT = QuadraticProbing(10)
	hT.insert(10)
	hT.insert(20)

	while True:
		try:
			x = int(input("Enter value : "))
			y = hT.search(x)
			if y is None: print(x, " is not in hashTable", end="\n")
			else: print(x, " is in idex ", y, end="\n")
		except: 
			break