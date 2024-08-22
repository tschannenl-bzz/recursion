from rekursion1 import *
import time

def main():
    path = "your path here"

    # opt 1: scanner     opt 2: scanner with filter
    option = 1

    start = time.time()
    scanner_programm(path,option)
    end = time.time()

    reader_time = end - start
    print(f"\n--------------------\n{reader_time:.9f} Sekunden")

if __name__ == '__main__':
    main()





