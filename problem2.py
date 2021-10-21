import sys

def binary_search(arr, low, high, s):
 
    if high < low:
        return -1
           
    mid = int((low + high)/2)
     
    if s == arr[mid]:
        upper = binary_search(arr, low, mid -1, s)
        lower = binary_search(arr, mid+1, high, s)
        if upper > mid:
            return upper
        elif lower > mid:
            return lower
        else:
            return mid
        
    if s > arr[mid]:
        return binary_search(arr, (mid + 1), high,
                                            s);
    return binary_search(arr, low, (mid -1), s)


def pivoted_binary_search(arr, n, s):
 
    pivot = find_pivot(arr, 0, n-1);
 
  
    if pivot == -1:
        return binary_search(arr, 0, n-1, s);
 

    if arr[pivot] == s:
        return pivot
    if arr[0] <= s:
        return binary_search(arr, 0, pivot-1, s);
    return binary_search(arr, pivot+1, n-1, s);
 
 

def find_pivot(arr, low, high):
     

    if high < low:
        return -1
    if high == low:
        return low
     

    mid = int((low + high)/2)
     
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    return find_pivot(arr, mid + 1, high)



def problem2(s1, s2):
    out = []
    for s in s2:
        result = pivoted_binary_search(s1, len(s1), s)
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
    for out in problem2(s1,s2):
        print(out)
main()
