# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def list_data_structures():
    print("in-build data structures:\n"
          "1) lists:\n"
          "2) tuples\n"
          "3) dictionaries\n"
          "etc.\n")
    print("user-defined data structures:\n"
          "1) linked-lists\n"
          "2) trees\n"
          "3) graphs\n"
          "etc.\n")


def lists():
    print("Lists:")

    a = [1, 'a', 1.1, False]
    print('a = [1, "a", 1.1, False]:', a)

    a.append(2)
    print('a.append(2):', a)

    a.insert(1, 3)
    print('a.insert(1,3):', a)

    a.extend(["add", "to", "end"])
    print('a.extend(["add","to","end"]):', a)

    a.remove(2)
    print('a.remove(2):', a)

    a = list((1, 2, 'a', 3.14, True))
    print('a = list((1,2,"a",3.14,True)):', a)

    a = list('1aTrue')
    print('a = list("1aTrue"):', a)

    a = list([1, 2])
    print('a = list([1,2]):', a)

    a = [2] * 3
    print('a = [2] * 3:', a)

    a = [1, "a", 1.3, True]
    print('a = [1,"a",1.3,True]:', a)

    print('3 in a:', 2 in a)

    popped = a.pop(1)
    print('popped = a.pop(1):', a)
    print('popped:', popped)

    del a[1]
    print('del a[1]:', a)

    print('for idx, item in enumerate(a):')
    for idx, item in enumerate(a):
        print(f'a[{idx}]:', item)

    a = [1, 2, 3, 4]
    print('a = [1, 2, 3, 4]:', a)

    a = [n ** 2 for n in a]
    print('a = [n**2 for n in a]:', a)

    a = list(map(lambda n: n ** 2, a))
    print('a = list(map(lambda n: n**2, a)):', a)

    a = list(n ** 2 for n in a)
    print('a = list(n**2 for n in a)', a)

    print('a,count(1):', a.count(1))

    # todo: zip, Counter, 


def main():
    list_data_structures()
    lists()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
