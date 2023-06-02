#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    just_names = []
    for i in names:
        if i[0] != '_' and i[1] != '_':
            just_names.append(i)
    just_names.sort()
    for i in just_names:
        print(i)
