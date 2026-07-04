# Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return the deserialized NestedInteger.
#
# Each element is either an integer or a list whose elements may also be integers or other lists.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # If it's just an integer, return directly
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ''
        negative = False

        for ch in s:
            if ch == '-':
                negative = True
            elif ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(NestedInteger())
            elif ch in ',]':
                # if a number was collected before comma or closing bracket
                if num:
                    value = int(num) if not negative else -int(num)
                    stack[-1].add(NestedInteger(value))
                    num = ''
                    negative = False
                # if closing bracket, pop and add to parent
                if ch == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)

        return stack[0]
