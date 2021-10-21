import sys


def problem0(s1, s2):
    n1 = len(s1)
    out = []
    for s in s2:
        out.append(n1+s)
    return out

def filter(states):
    s1 = []
    s2 = []
    for state in states:
        count = 0
        for st in state:
            st.strip()
            sr = st.split(" ")
            for s in sr:
                if s != "\n":
                    if count == 0:
                        s1.append(int(s))
                        
                    else:
                        s2.append(int(s))
            count+= 1
                
    return (s1, s2)

def aggregateLines(inputlines):
    states = []
    states.append(inputlines.readlines())
    newState = filter(states)
    return newState
        

def main():
    s1, s2 = aggregateLines(sys.stdin);
    for out in problem0(s1,s2):
        print(out)
main()
