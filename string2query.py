#!/usr/bin/env python

"""Convert string to tree which could be used for queries."""


def is_balanced(strng):
    """TO Check if string is balanced, check only '() and []'

    :strng: TODO
    :returns: TODO

    """
    open_list = ["[", "("]
    close_list = ["]", ")"]
    stck = []
    for i, s_g in enumerate(strng):
        if s_g in open_list:
            if i != 0 and strng[i-1] != "\\":
                stck.append(s_g)
        elif s_g in close_list:
            if i != 0 and strng[i-1] != "\\":
                pos = close_list.index(s_g)
                if ((len(stck) > 0) and
                        (open_list[pos] == stck[len(stck)-1])):
                    stck.pop()
                else:
                    return False
    return bool(not stck)


def val_type(vals):
    """Return value and type."""
    value, typ = "", ""
    temp_type = False
    for val in vals:
        if val == "[":
            temp_type = True
            continue
        if temp_type:
            if val == "]":
                continue
            typ += val
        else:
            value += val
    if not value.strip():
        return None
    if not typ.strip():
        typ = "all"
    return value.strip(), typ.strip()


class Stack:
    """Stores information in stack."""

    def __init__(self):
        self.item = []

    def push(self, value):
        """Insert the givel value in the stack."""
        self.item.append(value)

    def peek(self):
        """Checks whether stack is empty. if not, return the last value of stack
        without removing the value from stack.
        """
        if self.isempty():
            return 0
        return self.item[-1]

    def pop(self):
        """Remove and return last value of the stack if stack in not empty."""
        if self.isempty():
            return 0
        return self.item.pop()

    def length(self):
        """Returns length of the stack at current point."""
        return len(self.item)

    def isempty(self):
        """Checks whether the stack is empty."""
        return bool(not self.item)

    def display(self):
        """Displays the values of the stack."""
        if self.isempty():
            return
        temps = Stack()
        while not self.isempty():
            last_val = self.peek()
            temps.push(last_val)
            self.pop()
        while not temps.isempty():
            last_val = temps.peek()
            self.push(last_val)
            temps.pop()

    def not_greater(self, operand):
        """Checks whether the role of operand is greater."""
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
        if self.peek() == '(':
            return False
        operand_a = precedence[operand]
        operand_b = precedence[self.peek()]
        return bool(operand_a <= operand_b)

    def infix2postfix(self, exp):
        """Convert infix expression to postfix expression."""
        output = ""

        for character in exp:

            if character.isalpha():  # check if operand add to output
                output = output + character

            # If the character is an '(', push it to stack
            elif character == '(':
                self.push(character)

            elif character == ')':  # if ')' pop till '('
                while (not self.isempty() and self.peek() != '('):
                    last = self.pop()
                    output = output + last
                if (not self.isempty() and self.peek() != '('):
                    return -1
                _ = self.pop()
            else:
                while (not self.isempty() and self.not_greater(character)):
                    c = self.pop()
                    output = output + c
                self.push(character)

        # pop all the operator from the stack
        while not self.isempty():
            last = self.pop()
            output = output + last
        return output


def str2eq(strng):
    """TODO: Docstring for str2eq.

    :strng: TODO
    :returns: TODO

    """

    init_chr = 65  # "A"
    qvalue = ""
    value_dict = {}
    my_equation = ""
    for x in strng:
        if x in "(&|)":
            if qvalue:
                # TODO: Rename here
                t = val_type(qvalue)
                if t:
                    my_equation += chr(init_chr)
                    value_dict[chr(init_chr)] = t
                    init_chr += 1
                qvalue = ""
            if x == '&':
                my_equation += "*"
            elif x == "|":
                my_equation += "+"
            else:
                my_equation += x
        else:
            qvalue += x

    if x != ")" and qvalue:
        # TODO: Rename here
        t = val_type(qvalue)
        if t:
            my_equation += chr(init_chr)
            value_dict[chr(init_chr)] = x
    return my_equation, value_dict


st = Stack()
# st.infixToPostfix(my_equation)
