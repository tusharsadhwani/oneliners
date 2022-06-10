LIMIT = 1000; print([2] + [i for i in range(3, LIMIT+1, 2) if all(i % 3 != 0 and i % x != 0 and i % (x+2) != 0 for x in range(5, int(i**0.5)+3, 6))])
