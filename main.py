import numpy as np
import lab2
from krylov import krylov

def main():
    np.set_printoptions(precision=5, suppress=True)
    A = np.array([
        [6.26, 1.11, 0.78, 1.21],
        [1.11, 4.16, 1.30, 0.16],
        [0.78, 1.30, 6.44, 2.00],
        [1.21, 0.16, 2.10, 6.10]
    ])

if __name__ == '__main__':
    main()