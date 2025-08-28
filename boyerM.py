def boyer_moore(T, P):
    n = len(T)
    m = len(P)

    # Create a dictionary of last occurrences of characters in P
    last_occurrence = {}
    for i in range(m):
        last_occurrence[P[i]] = i

    # Align the right end of P with the character in T at index m-1
    i = m - 1
    j = m - 1

    while i < n:
        # If the characters match, continue comparing the previous characters in P and T
        if T[i] == P[j]:
            if j == 0:
                # If all characters match, return the index of the first character in T that aligns with the beginning of P
                return i
            else:
                i -= 1
                j -= 1
        else:
            # If a mismatch is found, check if the character is in P
            if T[i] in last_occurrence:
                last_index = last_occurrence[T[i]]
                # Align the text T appropriately and align P at index m-1
                i += m - min(j, 1 + last_index)
                j = m - 1
            else:
                # Shift P to the right by m positions
                i += m
                j = m - 1

    # If a match is not found, return -1
    return -1
def main():
    T="abacaabaccabacabaabb"
    P="abacab"
    idx=boyer_moore(T,P)
    print(f"Pattern \"{P}\" starts in text: \"{T}\" at index: {idx}")
main ()
