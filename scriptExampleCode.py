def test_fcn(*args):
    x, = args;
    for i in range(x):
        print(i)

if __name__ == "__main__":
    test_fcn(100)
