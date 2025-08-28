def main():
    d = HashMap()
    print(len(d))

    d["dog"] = "cat"
    d["batman"] = "joker"
    d["superman"] = "lex luther"

    for key in d:
        print(key)

    for key in d:
        print(key, d[key])

main()


    