# There is a list of  character heights aligned by index to their letters. For example, 'a' is at index  and 'z' is at index .
# There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in
# assuming all letters are  wide.


#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#
import string

letters = list(string.ascii_lowercase)


def designerPdfViewer(h, word):
    word_len = len(word)
    word_height = 0

    m = dict(zip(letters, h))

    for l in word:
        word_height = max(word_height, m[l])

    return word_len * word_height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
