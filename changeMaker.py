# change = [1, 5, 10, 25]
change = [20, 6, 1]

def makeChange(amount, memo):
	if memo == None:
		memo = dict()
	if amount in memo.keys():
		return memo[amount]
	# print ("single iteration")
	if amount == 0:
		# print("change made")
		return 0
	minChange = 1000
	for item in change:
		if item <= amount:
			coins = 1 + makeChange(amount - item, memo)
			minChange = min(coins, minChange)
			memo[amount] = minChange
		
	return minChange
	
print (makeChange(36, None))
		
			
		
		