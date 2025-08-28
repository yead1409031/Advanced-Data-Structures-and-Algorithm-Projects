DEBUG= True
def find_brute(T,P):
    n,m=len(T),len(P)

    for i in range(n-m+1):
        if DEBUG:
            print(f"Trying at index:   {i}...")
        
    
        k=0
        while (k<m) and (T[i+k]==P[k]):
            k+=1
        if k==m:
            #P->T[i:i+m]
            return i
    return -1

def main():
    T="abacaabaccabacabaabb"
    P="abacab"
    idx=find_brute(T,P)
    print(f"Pattern \"{P}\" starts in text: \"{T}\" at index: {idx}")
main ()