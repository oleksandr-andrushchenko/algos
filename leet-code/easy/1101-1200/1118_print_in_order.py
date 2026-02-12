# Suppose we have a class:
#
# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call
# second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed
# after first(), and third() is executed after second().
#
# Note:
#
# We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem
# to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

import threading


class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_done.set()  # signal that first() is done

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.wait()  # wait until first() finishes
        printSecond()
        self.second_done.set()  # signal that second() is done

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.wait()  # wait until second() finishes
        printThird()
