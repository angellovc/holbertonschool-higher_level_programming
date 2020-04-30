#!/usr/bin/python3
""" list the modules inside hidden_without those that start at """
if __name__ == "__main__":
    import hidden_4
    modules = dir(hidden_4)
    list.sort(modules)
    for mod in modules:
        if mod[0] == '_':
            continue
        print(mod)
