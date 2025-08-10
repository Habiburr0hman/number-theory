def ulam():
    arr = [1, 2]
    for num in range(3, 5000):
        count = 0
        is_break = False
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == num:
                    count += 1
                if count > 1:
                    is_break = True
                    break
            if is_break:
                break
        if count == 1:
            arr.append(num)
    return arr

def fast_ulam():
    arr = [1, 2]
    for num in range(3, 5000):
        count = 0
        for i in range(len(arr)):
            if num - arr[i] in arr and arr[i] != num - arr[i]:
                count += 1
            if count > 2:
                break
        if count == 2:
            arr.append(num)
    return arr

# arr = ulam()
# print(arr)
# print(len(arr))
arr = fast_ulam()
print(arr)
print(len(arr))