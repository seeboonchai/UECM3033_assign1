import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.cos(x*x), (x,0,1))
    return ans

def my_solution():
    A = np.array( [[1,1,2,2,3,4,5,6,6,7], [1,2,4,5,6,7,4,5,7,8]
                    ,[1,2,3,4,5,6,7,8,8,9],[4,6,7,8,9,4,3,2,3,2],
                        [4,6,7,8,7,4,3,8,3,2],[4,6,7,7,9,8,7,6,3,2],
                       [8,5,7,7,9,4,3,6,3,2],[5,6,4,8,4,4,3,5,7,2],
                      [4,6,7,8,9,4,3,2,3,2],[5,7,9,7,7,4,8,2,4,2]])
    b = np.array([9,8,4,5,6,7,4,5,6,7])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1300400
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
