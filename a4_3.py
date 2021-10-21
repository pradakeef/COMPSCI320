import sys
def getMax(arr,start,end):

   if(start == end):
       return arr[start]

   sd = [0]*len(arr)
   sd[start] = arr[start]
   sd[start+1] = max(arr[start+1],sd[start])

   for i in range(start+2,end+1):
       sd[i] = max(sd[i-1],sd[i-2]+arr[i])

   return sd[end]

def a4(arr):
   if(not arr or len(arr)==0):
       print(0, 0)

   elif(len(arr) == 1):
       print(arr[0], 0)
   elif(len(arr) == 2):
       print(max(arr), min(arr))


   else:

       x = getMax(arr,0,len(arr)-2)
       y = getMax(arr,1,len(arr)-1)
       first = max(x,y)
       second = sum(arr) - first

       print(first,second)

def main():
   for inputLine in sys.stdin:
       
       try:
           arr = [int(p) for p in inputLine.strip().split(" ")]
          
           a4(arr)
       except ValueError as ve:
           print(0, 0)

if __name__ == '__main__':
   main()
