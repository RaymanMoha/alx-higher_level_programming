#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all names defined by the compiled module hidden_4"""
    import hidden_4

    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
