def find_even_index(arr):
    i = 0
    answer = 0
    while(i <= len(arr)):
        if sum(arr[:i+1]) == sum(arr[i:]):
            answer = i
            break
        else:
            answer = -1
            i += 1
   
    return answer
   
find_even_index([1,2,3,4,3,2,1])