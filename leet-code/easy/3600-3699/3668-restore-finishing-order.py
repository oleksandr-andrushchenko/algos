# You are given an integer array order of length n and an integer array friends.
#
# order contains every integer from 1 to n exactly once, representing the IDs of the participants of a race in their
# finishing order.
# friends contains the IDs of your friends in the race sorted in strictly increasing order. Each ID in friends is
# guaranteed to appear in the order array.
# Return an array containing your friends' IDs in their finishing order.


from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        return [person for person in order if person in friends_set]
