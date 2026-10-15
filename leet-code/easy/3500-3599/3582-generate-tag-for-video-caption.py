# You are given a string caption representing the caption for a video.
#
# The following actions must be performed in order to generate a valid tag for the video:
#
# Combine all words in the string into a single camelCase string prefixed with '#'. A camelCase string is one where the
# first letter of all words except the first one is capitalized. All characters after the first character in each word
# must be lowercase.
#
# Remove all characters that are not an English letter, except the first '#'.
#
# Truncate the result to a maximum of 100 characters.
#
# Return the tag after performing the actions on caption.


class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()

        tag = "#"
        for i, word in enumerate(words):
            word = ''.join(c for c in word if c.isascii() and c.isalpha())

            if i == 0:
                tag += word.lower()
            else:
                tag += word.capitalize()

        return tag[:100]
