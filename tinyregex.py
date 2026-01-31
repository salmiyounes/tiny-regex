from typing import (
    Set,
    List
)

class State(object):
    def __init__(self, label: str | None = None) -> None:
        self.label = label
        self.edge1 = None
        self.edge2 = None

class NFA(object):
    def __init__(self, start: State, accept: Set[State], states: Set[State]) -> None:
        self.states = states
        self.start  = start
        self.accept = accept
        self._stack: List[State] = []
    
    def append(self, s: State) -> None:
        self._stack.append(s)

    def pop(self) -> State | None:
        if self._stack:
            return self._stack.pop()
        return None

    def transition_function(self, s: State) -> None:
        pass         

def shunt(infix: str) -> str:
    specials = {
        '*': 60,
        '+': 55,
        '?': 50,
        '.': 40,
        '|': 20
    }

    postfix: str = '' 
    stack: List[str] = []

    for c in infix:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack:
                stack.pop() 
        elif c in specials:
            while stack and stack[-1] in specials and specials[c] <= specials[stack[-1]]:
                postfix += stack.pop()
            stack.append(c)
        else:
            postfix += c

    while stack:
        postfix += stack.pop()

    return postfix

def compile():
    return 

def match(pattern: str, text: str) -> bool:
    return False

if __name__ == "__main__":
    pass