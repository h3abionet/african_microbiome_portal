#!/usr/bin/env python

"""Convert string to tree which could be used for queries."""
from django.db.models import Q


def is_balanced(strng):
    """TO Check if string is balanced, check only '() and []'

    input: A+(B*C)+(D*E)
    output: True

    input: A+(B*C+(D*E)
    output: False
    """
    open_list = ["[", "("]
    close_list = ["]", ")"]
    stck = []
    for i, s_g in enumerate(strng):
        if s_g in open_list:
            if i != 0 and strng[i - 1] != "\\":
                stck.append(s_g)
        elif s_g in close_list:
            if i != 0 and strng[i - 1] != "\\":
                pos = close_list.index(s_g)
                if (len(stck) > 0) and (open_list[pos] == stck[len(stck) - 1]):
                    stck.pop()
                else:
                    return False
    return bool(not stck)


def val_type(vals):
    """
    Returns value and type.
    Input: "Malawi[country]"
    Output: ("Malawi", "country")

    Input: "Malawi"
    output:("Malawi", "all")
    """
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
        """__init__."""
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
        # NOTE: For the task in this program order is not important as the are
        # separated by ()
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}
        if self.peek() == "(":
            return False
        operand_a = precedence[operand]
        operand_b = precedence[self.peek()]
        return bool(operand_a <= operand_b)

    def infix2postfix(self, exp):
        """
        Convert infix expression to postfix expression.
        Input: A+(B*C)+(D*E)
        Output: ABC*+DE*+
        """
        output = ""

        for character in exp:

            if character.isalpha():  # check if operand add to output
                output = output + character

            # If the character is an '(', push it to stack
            elif character == "(":
                self.push(character)

            elif character == ")":  # if ')' pop till '('
                while not self.isempty() and self.peek() != "(":
                    output += self.pop()
                    # output = output + last
                if not self.isempty() and self.peek() != "(":
                    return -1
                _ = self.pop()
            else:
                while not self.isempty() and self.not_greater(character):
                    output += self.pop()
                self.push(character)

        # pop all the operator from the stack
        while not self.isempty():
            output += self.pop()
            # output = output + last
        return output


def str2eq(strng):
    """
    Converts a given string to mathematical equation and operand dictionanry.
    Input: "~amplicons | (South Africa[country] & cancer[disease]) | \
            (Malawi[country] & Illumina[platform])"
    output: A+(B*C)+(D*E) {'A': ('~amplicons', 'all'), \
            'B': ('South Africa', 'country'), 'C': ('cancer', 'disease'), \
            'D': ('Malawi', 'country'), 'E': ('Illumina', 'platform')}
    """

    init_chr = 65  # "A"
    qvalue = ""
    value_dict = {}
    my_equation = ""
    for character in strng:
        if character in "(&|)":
            if qvalue:
                vtype = val_type(qvalue)
                if vtype:
                    my_equation += chr(init_chr)
                    value_dict[chr(init_chr)] = vtype
                    init_chr += 1
                qvalue = ""
            if character == "&":
                my_equation += "*"
            elif character == "|":
                my_equation += "+"
            else:
                my_equation += character
        else:
            qvalue += character

    if qvalue:
        my_equation += chr(init_chr)
        value_dict[chr(init_chr)] = val_type(qvalue)

    return my_equation, value_dict


def query_Q(query):
    """Converts query and query type (i.e. ("Malawi","country")) to Django Q object."""
    if query[1] == "sampid":
        return (
            ~Q(sampid__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(sampid__icontains=query[0])
        )
    if query[1] == "avspotlen":
        return (
            ~Q(avspotlen__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(avspotlen__icontains=query[0])
        )
    if query[1] == "country":
        return (
            ~Q(l2loc_diet__country__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2loc_diet__country__icontains=query[0])
        )
    if query[1] == "region":
        return (
            ~Q(l2loc_diet__region__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2loc_diet__region__icontains=query[0])
        )
    if query[1] == "urbanization":
        return (
            ~Q(l2loc_diet__urbanization__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2loc_diet__urbanization__icontains=query[0])
        )
    if query[1] == "cityvillage":
        return (
            ~Q(l2loc_diet__cityvillage__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2loc_diet__cityvillage__icontains=query[0])
        )
    if query[1] == "urbanization":
        return (
            ~Q(l2loc_diet__urbanization__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2loc_diet__urbanization__icontains=query[0])
        )
    if query[1] == "platform":
        return (
            ~Q(l2platform__platform__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2platform__platform__icontains=query[0])
        )
    if query[1] == "amplicon":
        return (
            ~Q(l2platform__target_amplicon__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2platform__target_amplicon__icontains=query[0])
        )
    if query[1] == "assay":
        return (
            ~Q(l2platform__assay__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2platform__assay__icontains=query[0])
        )
    if query[1] == "ethinicity":
        return (
            ~Q(l2loc_diet__ethnicity__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2loc_diet__ethnicity__icontains=query[0])
        )
    if query[1] == "disease":
        return (
            ~Q(l2disease__disease__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2disease__disease__icontains=query[0])
        )
    if (
        query[1] == "bioproject"
    ):  # NOTE: This is hidden from rest, as only for sample query
        return (
            ~Q(l2disease__disease__icontains=query[0][1:])
            if query[0].startswith("~")
            else Q(l2bioproject__repoid__icontains=query[0])
        )

    if not query[0].startswith("~"):
        return (
            Q(sampid__icontains=query[0])
            | Q(avspotlen__icontains=query[0])
            | Q(l2loc_diet__country__icontains=query[0])
            | Q(l2loc_diet__region__icontains=query[0])
            | Q(l2loc_diet__urbanization__icontains=query[0])
            | Q(l2loc_diet__cityvillage__icontains=query[0])
            | Q(l2loc_diet__ethnicity__icontains=query[0])
            | Q(l2platform__platform__icontains=query[0])
            | Q(l2platform__target_amplicon__icontains=query[0])
            | Q(l2platform__assay__icontains=query[0])
            | Q(l2disease__disease__icontains=query[0])
        )
    return ~(
        Q(sampid__icontains=query[0][1:])
        | Q(avspotlen__icontains=query[0][1:])
        | Q(l2loc_diet__country__icontains=query[0][1:])
        | Q(l2loc_diet__region__icontains=query[0][1:])
        | Q(l2loc_diet__urbanization__icontains=query[0][1:])
        | Q(l2loc_diet__cityvillage__icontains=query[0][1:])
        | Q(l2loc_diet__ethnicity__icontains=query[0][1:])
        | Q(l2platform__platform__icontains=query[0][1:])
        | Q(l2platform__target_amplicon__icontains=query[0][1:])
        | Q(l2platform__assay__icontains=query[0][1:])
        | Q(l2disease__disease__icontains=query[0][1:])
    )


def eq2query(postfix, diction):
    """Convert of postfix to Query."""
    to_calculate = []
    to_operate = []
    postfix = list(postfix)
    query = None
    while postfix:
        current = postfix.pop()
        if current in "+*":
            to_operate.append(current)
        else:
            to_calculate.append(query_Q(diction[current]))
            if len(to_calculate) >= 2:
                first = to_calculate.pop()
                second = to_calculate.pop()
                operator = to_operate.pop()
                if operator == "*":
                    query = first | second
                to_calculate.append(query)
    if len(to_calculate) > 1:
        print("Something worng.")
    return to_calculate[0]


def query2sqlquery(qry):
    """TODO: Docstring for ppp.

    :qry: TODO
    :returns: TODO

    """
    infix_equation, diction = str2eq(qry)
    blnc = is_balanced(infix_equation)
    if not blnc:
        print("Given query is not balanced")
    postfix_equation = Stack().infix2postfix(infix_equation)
    print(infix_equation, blnc, postfix_equation)
    sql_query = eq2query(postfix_equation, diction)
    return sql_query


if __name__ == "__main__":
    infix_equation, diction = str2eq(
        "~amplicons | (South Africa[country] & cancer[disease]) | (Malawi[country] & Illumina[platform])"
        # "Malawi"
    )
    print(infix_equation, diction)
    blnc = is_balanced(infix_equation)
    postfix_eqaution = Stack().infix2postfix(infix_equation)
    sql_query = eq2query(postfix_eqaution, diction)
    print(infix_equation, blnc, postfix_eqaution, sql_query)
