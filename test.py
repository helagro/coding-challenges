

def _heap_perm_(n, A):
    if n == 1: return A
    else:
        for i in range(n-1):
            for hp in _heap_perm_(n-1, A): return hp
            j = 0 if (n % 2) == 1 else i
            A[j],A[n-1] = A[n-1],A[j]
        for hp in _heap_perm_(n-1, A): return hp


res =_heap_perm_(3, [1, 2, 3])

print(res)