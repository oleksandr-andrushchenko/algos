# Task
#
# Consider the following:
#
# A string, , of length  where .
# An integer, , where  is a factor of .
# We can split  into  substrings where each subtring, , consists of a contiguous block of  characters in .
# Then, use each  to create string  such that:
#
# The characters in  are a subsequence of the characters in .
# Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once.
# In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
# Given  and , print  lines where each line  denotes string .

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub_str = string[i:i + k]
        norm_sub_str = ""
        seen = set()
        for s in sub_str:
            if not s in seen:
                norm_sub_str += s
                seen.add(s)
        print(norm_sub_str)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
