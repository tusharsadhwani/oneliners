n = 2 * int(input()) - 1; print('\n'.join((''.join(map(str, (min(i+1, j+1, (n-i), (n-j)) for j in range(n))))) for i in range(n)))
