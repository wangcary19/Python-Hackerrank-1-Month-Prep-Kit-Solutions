# Do the following:
# 1) Declare a 2-dimensional array arr of n empty arrays and an empty answer array. All arrays are zero
#    indexed.
# 2) Declare an integer lastAnswer and initialize it to 0.
# 3) Create function that takes inputs of the format "1 x y" and "2 x y", do idx = (x XOR lastAnswer) % n
#       a) If "1 x y", do arr[idx].append(y)
#       b) Let "2 x y", do lastAnswer = arr[idx][y % size(arr[idx])] and answer.append(lastAnswer)
# 4) Return answer[]

# Solution: this is a reading comprehension problem, all we need to do is implement the above
#           without being lost in the details.
#           Time complexity: O(N)

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        print(query)
        if query[0] == 1:
            idx = (query[1] ^ lastAnswer) % n
            arr[idx].append(query[2])
        elif query[0] == 2:
            idx = (query[1] ^ lastAnswer) % n
            lastAnswer = arr[idx][query[2] % len(arr[idx])]
            answers.append(lastAnswer)

    return answers

