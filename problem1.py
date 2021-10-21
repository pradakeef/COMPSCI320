import sys

def binary_search(arr, low, high, x):
 

    if high >=low:
 
        mid = (high + low) // 2
 
   
        if arr[mid] == x:
            upper = binary_search(arr, low, mid -1, x)
            lower = binary_search(arr, mid+1, high, x)
            if upper > mid:
                return upper
            elif lower > mid:
                return lower
            else:
                return mid
            
 

        elif arr[mid] > x:
            return binary_search(arr, low, mid-1 , x)
 

        else:
            return binary_search(arr, mid+1 , high, x)
 
    else:

        return -1



def problem1(s1, s2):
    out = []
    for s in s2:
        result = binary_search(s1, 0, len(s1), s)
        out.append(result)
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
    for out in problem1(s1,s2):
        print(out)
main()
