# Stack and Queue

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    


# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutoial
def reverse_string(word):
    s = Stack()

    for char in word:
        s.push(char)

    rword = ""
    for c in range(s.size()):
        rword += s.pop()
    return rword

# print(reverse_string("We will conquere COVID-19"))

# Write a function in python that can reverse a string using stack data structure. Use stack class from the tutorial

# My interpretation
# The thought process
# possible false conditions:
# len should be an even number
# 
# if we take into account rstr at least have: '}{', ')(', ']['
# must have at least one but the problem is
#
# [](( -> ((][ -> evaluates to true but still false
#
# ][
#
# )), ((, 
#
# ))((}{
#
# {})())


def is_match(ch1, ch2):
    matching_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    return matching_dict[ch1] == ch2

def is_balanced(word):
    s = Stack()
    holdWord = Stack()


    for char in word:
        if char in '(){}[]':
            s.push(char)

    while s.size()!= 0:
        current_word = s.pop()
        # check if its closing bracket
        if current_word in ")}]":
            if s.size() == 0:
                return False
            if s.peek() in "({[":
                if is_match(current_word, s.peek()):
                    s.pop()
            else:
                holdWord.push(current_word)
        # here if its an opening bracket so it would check the holdWord stack
        else:
            # return false because there are no closing brackets in the stack for this opening bracket hence an inbalanced closure
            if holdWord.size() == 0:
                return False
            if not is_match(holdWord.pop(), current_word):
                return False
    # Unresolved Closed brackets, parentheses
    if holdWord.size()!=0:
        return False



    return True

print(is_balanced("({a+b})") )                  # True
print(is_balanced("))()a+b}{"))                 # False  
print(is_balanced("((a+b))"))                   # True
print(is_balanced("())"))                       # False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}") )     # True
print(is_balanced("[](){}}({[]})"))             # False

