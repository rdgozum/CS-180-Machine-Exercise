class Node(object):
    def __init__(self):
    	self.elem = []			#list of integers
    	self.child = []			#list of objects
    	self.parent= None
        self.sign = None		# 1 or -1
        self.cat = None	

gpath=[]
ugpath=[]
possibility=[]
winList=[]
def div(node):
	for i in range(len(node.elem)):					#traverse list (elem) of int from obj
		for j in range(1, (node.elem[i]+1)/2):		#find addends
			new = Node()#
			new.parent = node#
			node.child.append(new)
			copy = node.elem[:]
			copy.remove(node.elem[i])
			el = copy + [j, node.elem[i] - j]
			#el.sort()
			new.elem.extend(el)#
			if(new.parent.cat=='max'):#
				new.cat='min'
			else:
				new.cat='max'
			div(new)

	if(isLeaf(node)):
		if(node.cat=='min'):
			node.sign=1
			winList.insert(0, node)
		else:
			node.sign=-1

	if(len(node.parent.child)>1):
		if(node.parent.cat=='max'):
			node.parent.sign=getMax(node.parent)
		else:
			node.parent.sign=getMin(node.parent)
	else:
		node.parent.sign=node.parent.child[0].sign

	insert = str(node.elem) + '  ' + node.cat + '  ' + str(node.sign)
	possibility.insert(0, insert)

def isLeaf(node):
	for i in range(len(node.elem)):
		if(node.elem[i]>2):
			return False
	return True

def getMax(node):
	temp1=[]
	for i in range(len(node.child)):
		temp1.append(node.child[i].sign)
	return max(temp1)

def getMin(node):
	temp2=[]
	for i in range(len(node.child)):
		temp2.append(node.child[i].sign)
	return min(temp2)

def winning(node):
	guaranteed=0
	tempPath=[]
	traverse=node
	if(traverse.sign==1):
		guaranteed=1
	tempPath.insert(0, traverse.elem)
	while(traverse != root):
		traverse=traverse.parent
		if(traverse.sign==-1):
			guaranteed=0
		tempPath.insert(0, traverse.elem)

	if(guaranteed==0):
		if(tempPath not in ugpath):
			ugpath.insert(0, tempPath)
	else:
		if(tempPath not in gpath):
			gpath.insert(0, tempPath)

start=input('ROOT: ')
pointer=Node()
root=Node()
pointer.child.append(root)
root.parent=pointer
root.cat='max'
root.elem.append(start)

div(root)

for i in range(len(winList)):
	winning(winList[i])

print '\nPATHS'
for i in range(len(possibility)):
	print possibility[i]

print '\nGuaranteed Winning Path/s'
for i in range(len(gpath)):
	print gpath[i]

print '\nUnguaranteed Winning Path/s'
for i in range(len(ugpath)):
	print ugpath[i]



