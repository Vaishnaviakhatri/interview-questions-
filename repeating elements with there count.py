def findRepeating(arr, size): 

    frequency = {} 

    for i in range (0, size): 

        frequency[arr[i]] = \ 

        frequency.get(arr[i], 0) + 1 

    return frequency 

if __name__ == "__main__": 

    arr = [4, 4, 5, 5, 6] 

    arr_size = len(arr) 

    frequency = findRepeating(arr, arr_size) 

    print("Below is the frequency\ 

    of repeated elements -") 

    for i in frequency: 

        if frequency[i] > 1: 

            print(i, " --> ", frequency[i])
