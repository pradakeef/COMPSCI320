"""Necklace Jewel Random Case Generator.

Randomly creates test cases for the necklace jewel problem presented in
Assignment 4. https://canvas.auckland.ac.nz/courses/60521/assignments/235863.

If you're not too familiar with your way around this generator, use the
randomcase() function as if it were stdin:

    `from a4randomcase import randomcase`
    `testcase = randomcase()`
    - `stdin.read()`: replace with `testcase.read()`
    - `stdin.readline()`: replace with `testcase.readline()`
    - `stdin.readlines(): replace with `testcase.readlines()`
    - `for line in stdin`: replace with `for line in testcase`

You can also run this program directly and follow the subsequent prompts to
save a test case to a file.

If you know what you're doing, feel free to just dismantle (or not even use)
this generator, I guess. I can't really cater to people better than me.


Best of luck on your assignment solution!
"""

import collections
import math
import random


class RandomCase:
    """Detailed random case generator."""

    def __init__(self, lines, minlength, maxlength, minvalue, maxvalue):
        """Create a new random test case.
        
        Parameters:
        - lines: the number of input lines to generate
        - minlength: the minimum number of jewels in a necklace
        - maxlength: the maximum number of jewels in a necklace
        - minvalue: the minimum value a jewel can have
        - maxvalue: the maximum value a jewel can have
        """
        if not isinstance(lines, int):
            raise TypeError(f"lines {lines} must be int")
        elif lines <= 0:
            raise ValueError(f"lines {lines} must be positive")
        elif not isinstance(minlength, int):
            raise TypeError(f"minlength {minlength} must be int")
        elif minlength <= 0:
            raise ValueError(f"minlength {minlength} must be positive")
        elif not isinstance(maxlength, int):
            raise TypeError(f"maxlength {maxlength} must be int")
        elif maxlength < minlength:
            raise ValueError(
                f"maxlength {maxlength} must be < minlength {minlength}"
            )
        elif not isinstance(minvalue, int):
            raise TypeError(f"minvalue {minvalue} must be int")
        elif minvalue <= 0:
            raise ValueError(f"minvalue {minvalue} must be positive")
        elif not isinstance(maxvalue, int):
            raise TypeError(f"maxvalue must be int, not {type(maxvalue)}")
        elif maxvalue < minvalue:
            raise ValueError(
                f"maxvalue {maxvalue} must be < minvalue {minvalue}"
            )
        self.__lines = lines
        self.__minlength = minlength
        self.__maxlength = maxlength
        self.__minvalue = minvalue
        self.__maxvalue = maxvalue
        self.__necklaces = collections.deque()
        for i in range(lines):
            self.__add_necklace()
    
    @property
    def lines(self):
        return self.__lines

    @property
    def minlength(self):
        return self.__minlength
    
    @property
    def maxlength(self):
        return self.__maxlength
    
    @property
    def minvalue(self):
        return self.__minvalue
    
    @property
    def maxvalue(self):
        return self.__maxvalue

    def __add_necklace(self):
        self.__necklaces.append(
            [
                random.randint(self.minvalue, self.maxvalue)
                for i in range(random.randint(self.minlength, self.maxlength))
            ]
        )
    
    def __necklace_to_inputline(necklace):
        return " ".join([str(jewel) for jewel in necklace]) + "\n"
    
    def __iter__(self):
        """Substitute `for line in stdin`."""
        return self

    def __next__(self):
        """Substitute `for line in stdin`."""
        if not self.__necklaces:
            raise StopIteration()
        else:
            return self.readline()
    
    def read(self):
        """Substitute `stdin.read()`."""
        return "".join(self.readlines())
    
    def readline(self):
        """Substitute `stdin.readline()`."""
        if not self.__necklaces:
            return ""
        else:
            return RandomCase.__necklace_to_inputline(
                self.__necklaces.popleft()
            )

    def readlines(self):
        """Substitute `stdin.readlines()`."""
        necklaces = self.__necklaces.copy()
        self.__necklaces.clear()
        return [
            RandomCase.__necklace_to_inputline(necklace)
            for necklace in necklaces
        ]
    
    def save(self, filename):
        """Save this case to a file."""
        with open(filename, "w") as file:
            file.write(self.read())


def randomcase(size=10):
    """Return a random test case.
    
    This method uses a single size parameter to derive all parameters of the
    actual random case generator, simplifying usage.
    """
    if not isinstance(size, int):
        raise TypeError(f"size must be int, not {type(size)}")
    elif size <= 0:
        raise ValueError(f"size must be positive, not {size}")
    return RandomCase(size, math.ceil(size*0.75), math.floor(size*1.25), 1, size**2)


if __name__ == "__main__":
    size = int(input("enter input size: "))
    filename = input("enter file to save to: ")
    randomcase(size).save(filename)
    print("done!")
