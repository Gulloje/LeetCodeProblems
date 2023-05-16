"""
You are given an m x n integer grid accounts where accounts[i][j] is the 
amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
"""

class Solution(object):
    def maximumWealth(self, accounts):
        largest = 0
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
                if sum > largest:
                    largest = sum
        return largest
    #test
    accounts = [[1,5],[7,3],[3,5]]
    wealth = maximumWealth(list, accounts)
    print(wealth)

