#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lists = dir(hidden_4)
    no = "__"
    for i in range(0, len(lists)):
        if no not in lists[i]:
            print(lists[i])
