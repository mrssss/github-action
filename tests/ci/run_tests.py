import os

if __name__ == '__main__':
    for (k, v) in os.environ.items():
        print(k, v)
