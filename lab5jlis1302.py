def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iteration = 0

    while left <= right:
        iteration += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            print(f"Target = {target}, Found at index = {mid}, Iterations = {iteration}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    
    print(f"Target = {target}, Not Found, Iterations = {iteration}")
    return -1


def linear_search(arr, target):
    iteration = 0
    for i, word in enumerate(arr):
        iteration += 1
        if word == target:
            print(f"Target = {target}, Found at index = {i}, Iterations = {iteration}")
            return i

    
    print(f"Target = {target}, Not Found, Iterations = {iteration}")
    return -1



file_path = 'C:\\Users\\jayju\\Downloads\\words.txt'  
with open(file_path, 'r') as file:
    words = file.read().splitlines()

print('Number of words read:', len(words))


target = input("Enter Search Key: ").lower()

while target != 'exit':
    print("\nBinary Search:")
    binary_search(words, target)

    print("\nLinear Search:")
    linear_search(words, target)

    target = input("Enter Search Key: ").lower()

    







