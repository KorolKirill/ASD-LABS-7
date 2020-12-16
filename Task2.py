def SelectionSort(itemsList):
	n = len( itemsList )
	for i in range( n - 1 ): 
		minValueIndex = i
		for j in range( i + 1, n ):
			if itemsList[j] < itemsList[minValueIndex] :
				minValueIndex = j
		if minValueIndex != i :
			temp = itemsList[i]
			itemsList[i] = itemsList[minValueIndex]
			itemsList[minValueIndex] = temp
	return itemsList

def corruption (table, comission):
	newTable = SelectionSort(table)

	while len(newTable) > 1:
		newAccountMoney = ((newTable[0] + newTable[1]) - (newTable[0] + newTable[1]) * comission)
		newTable.pop(0)
		newTable.pop(0)
		if len(newTable) == 0: return newAccountMoney

		if newAccountMoney <= newTable[0]:
			newTable.insert(0, newAccountMoney)
		elif (newAccountMoney >= newTable[len(newTable) - 1]):
			newTable.append(newAccountMoney)
		else:
			i = 0
			j = len(newTable)
			while True:
				k = (i + j) / 2
				if newTable[k] == newAccountMoney:
					newTable.insert(k, newAccountMoney)
					break
				elif newTable[k] > newAccountMoney:
					j = k
				elif newTable[k] < newAccountMoney:
					i = k
				if j - i == 1:
					newTable.insert(i, newAccountMoney)
					break

	return newTable[0]