class PriorityQueue():
	def __init__(self):
		self.array=[]

	def insert(self, (item, node, savePath)):
		self.array.append((item, node, savePath))
		self.array.sort()

	def delete(self):
		return self.array.pop(0)

	def isEmpty(self):
		return not self.array

	def printAll(self):
		print self.array

	def clear(self):
		while(not self.isEmpty()):
			self.delete()


def isExplored(explored, node):
	for i in range(len(explored)):
		if node==explored[i]:
			return True

queue=PriorityQueue()
straight = {'a': 366, 'b': 0, 'c': 160, 'd': 242, 'e': 161, 'f': 178, 'g':77, 'h': 151, 'i': 226, 'l': 244, 'm': 241, 'n': 234, 'o': 380, 'p': 98, 'r': 193 , 's': 253, 't': 329, 'u': 80, 'v': 199, 'z': 374}
adj={'as': 140, 'at': 118, 'az': 75, 'oz': 71, 'os': 151, 'lt': 111, 'lm': 70, 'dm': 75, 'cd': 120, 'cr': 146, 'rs': 80, 'fs': 99, 'pr': 97, 'cp': 138, 'bp': 101, 'bf': 211, 'bg': 90, 'bu': 85, 'hu': 98, 'eh': 86, 'uv': 142, 'iv': 92, 'in': 87}
explored=[]
savePath=[]

init=raw_input('Enter initial position: ')
temp=init
out=[]
store=0
savePath.append(init)

while(True):
	explored.append(temp)
	if(temp=='b'):
 		break
	keyList=adj.keys()
	for i in range(len(keyList)):
		nextNodes=keyList[i].replace(temp, '')
		if(temp in keyList[i] and (not isExplored(explored, nextNodes))):
			currCost=adj[keyList[i]]
			currCost=currCost+store
			savePath=out[:]
			savePath.append(temp)
			queue.insert((currCost, nextNodes, savePath))

	popped=queue.delete()
	store, temp, out=popped

out.append('b')
print '\nSEQUENCE: ' + str(out)
print 'TOTAL COST: ' + str(store)