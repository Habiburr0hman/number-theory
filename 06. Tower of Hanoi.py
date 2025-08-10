def hanoi(n, source, destination, auxiliary):
    if n <= 0:
        return
    hanoi(n-1, source, auxiliary, destination)
    print("{}. Move disk {} from {} to {}".format(hanoi.counter, n, source, destination))
    hanoi.counter += 1
    hanoi(n-1, auxiliary, destination, source)

hanoi.counter = 1
hanoi(3, "A", "C", "B")
