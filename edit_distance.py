# Uses python3
import numpy as np
import sys

#s - first line of letters (first string), t - second line of letters from s (second string)
def edit_distance(s, t):
    #create a s * t array of data type - int
    arr = np.zeros(shape=(len(s) + 1, len(t) + 1), dtype=int)
    
    for i in range(len(s) + 1):
     #construct rows from first string
     arr[i, 0] = i

    for i in range(len(t) + 1):
        arr[0, i] = i    

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            # compare row[i] and column[i]    
            if s[ i - 1] == t[ j - 1]: #there is a match
            #Reduce array, arr
                arr[i, j] = arr[i - 1, j - 1]
            else:
                #No match
                #Update array, arr due to insertion, mismatch or deletion 
                arr[i, j] = 1 + min( arr[i - 1, j], arr[i - 1, j - 1], arr[i, j - 1])

    return( arr[len(s), len(t)])            

    

if __name__ == '__main__':
   print(edit_distance(input(), input()))