# You are given an integer money denoting the amount of money (in dollars) that you have and another integer children
# denoting the number of children that you must distribute the money to.
#
# You have to distribute the money according to the following rules:
#
# All money must be distributed.
# Everyone must receive at least 1 dollar.
# Nobody receives 4 dollars.
# Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the
# aforementioned rules. If there is no way to distribute the money, return -1.

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money -= children
        answer = min(money // 7, children)
        money -= answer * 7
        children -= answer

        if children == 0 and money > 0:
            answer -= 1
        elif children == 1 and money == 3:
            answer -= 1

        return answer
