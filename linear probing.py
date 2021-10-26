class LinearProbing:
	def __init__(self, size):
		self.hashTable = [None for _ in range(size + 1)]
		self.size = size
	
	def hash(self, key):
		idx = key % self.size
		if not self.hashTable[idx]:
			return idx
		while self.hashTable[idx]:
			idx = (idx + 1) % self.size
		return idx

	def insert(self, key):
		idx = self.hash(key)
		self.hashTable[idx] = key

	def search(self, key):
		idx = key % self.size

		if self.hashTable[idx] != key:
			while self.hashTable[idx] != key & self.hashTable[idx]:
				idx = (idx + 1) % self.size
		
		if self.hashTable[idx] == key:
			return idx
		else: 
			return None


if __name__ == "__main__":
	hT = LinearProbing(10)
	hT.insert(10)
	hT.insert(20)

	while True:
		try:
			x = int(input("Enter value : "))
			y = hT.search(x)
			if y is None: print(x, " is not in hashTable")
			else: print(x, " is in idex ", y)
		except: 
			break
