#!/usr/bin/env python

"""Convert string to tree which could be used for queries."""


def is_balanced(strng):
    """TO Check if string is balanced, check only '() and []'

    :strng: TODO
    :returns: TODO

    """
    open_list = ["[", "("]
    close_list = ["]", ")"]
    stack = []
    for i, s in enumerate(strng):
        if s in open_list:
            if i != 0 and strng[i-1] != "\\":
                stack.append(s)
        elif s in close_list:
            if i != 0 and strng[i-1] != "\\":
                pos = close_list.index(s)
                if ((len(stack) > 0) and
                        (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False


def val_type(val):
    """Return value and type."""
    v, t = "", ""
    tt = False
    for x in val:
        if x == "[":
            tt = True
            continue
        if tt:
            if x == "]":
                continue
            t += x
        else:
            v += x
    if not(v.strip()):
        return
    if not t.strip():
        t = "all"
    return v.strip(), t.strip()


class stack:
    def __init__(self):
        self.item = []

    def push(self, it):
        self.item.append(it)

    def peek(self):
        if self.isempty():
            return 0
        return self.item[-1]

    def pop(self):
        if self.isempty():
            return 0
        return(self.item.pop())

    def length(self):
        return (len(self.item))

    def isempty(self):
        if self.item == []:
            return True
        else:
            return False

    def display(self):
        if self.isempty():
            return
        temps = stack()
        while not self.isempty():
            x = self.peek()
            print("~", x)
            temps.push(x)
            self.pop()
        while not temps.isempty():
            x = temps.peek()
            self.push(x)
            temps.pop()

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
        if self.peek() == '(':
            return False
        a = precedence[i]
        b = precedence[self.peek()]
        if a <= b:
            return True
        else:
            return False

    def infixToPostfix(self, exp):
        output = ""

        for i in exp:

            if self.isOperand(i):  # check if operand add to output
                #                 print(i,"~ Operand push to stack")
                output = output + i

            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)
#                 print(i," ~ Found ( push into stack")

            elif i == ')':  # if ')' pop till '('
                while (not self.isempty() and self.peek() != '('):
                    n = self.pop()
                    output = output + n
#                     print(n, "~ Operator popped from stack")
                if (not self.isempty() and self.peek() != '('):
                    #                     print("_________")
                    return -1
                else:
                    _ = self.pop()
            else:
                while (not self.isempty() and self.notGreater(i)):
                    c = self.pop()
                    output = output + c
                self.push(i)
#                 print(i,"Operator pushed to stack")

        # pop all the operator from the stack
        while not self.isempty():
            xx = self.pop()
            output = output + xx
#             print(xx,"~ pop at last")
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


st = stack()
st.infixToPostfix(my_equation)
