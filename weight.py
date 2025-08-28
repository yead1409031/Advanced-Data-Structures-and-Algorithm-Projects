def prefix_average1(S):
   n = len(S)
# create new list of n zeros
   A = [0] * n
   for j in range(n):
# begin computing S[0]+...+S[j]
     total = 0
     for i in range(j + 1):
       total += S[i]
# record the average
     A[j] = total / (j+1)
   return A