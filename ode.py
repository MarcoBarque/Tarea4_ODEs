def euler(f, x_n, y_n, h):
    '''Calculates a single point of \(y(x)\) through an aproximation using Euler's method.

    Args:
        f (function): The function f(x,y) that appears on the right side of the differential equation.
        x_n (float): The previous value of x, with this variable y_nph will be approximated.
        y_n (float): The previous value of y, with this variable y_nph will be approximated.
        h (float): The size of each step taken through the iteration that approximates the function \(y(x)\).

    Returns:
        y_nph (float): Value of the point y_nph, this value is \(y(x+h)\).
    '''
    return y_n + h*f(x_n,y_n)

def rk2(f, x_n, y_n, h): 
    '''Calculates a single point of \(y(x)\) through an aproximation using the Runge Kutta method of second order.
    
    Args:
        f (function): The function f(x,y) that appears on the right side of the differential equation.
        x_n (float): The previous value of x, with this variable y_nph will be approximated.
        y_n (float): The previous value of y, with this variable y_nph will be approximated.
        h (float): The size of each step taken through the iteration that approximates the function \(y(x)\).

    Returns:
        y_nph (float): Value of the point y_nph, this value is \(y(x+h)\).
    '''

    k1 = f(x_n, y_n)
    k2 = f(x_n + h/2, y_n + k1/2)
    return y_n + h*k2

def rk4(f, x_n, y_n, h):
    '''Calculates a single point of \(y(x)\) through an aproximation using the Runge Kutta method of fourth order.

    Args:
        f (function): The function f(x,y) that appears on the right side of the differential equation.
        x_n (float): The previous value of x, with this variable y_nph will be approximated.
        y_n (float): The previous value of y, with this variable y_nph will be approximated.
        h (float): The size of each step taken through the iteration that approximates the function \(y(x)\).

    Returns:
        y_nph (float): Value of the point y_nph, this value is \(y(x+h)\).
    '''

    k1 = f(x_n, y_n)
    k2 = f(x_n + h/2, y_n + h/2*k1)
    k3 = f(x_n + h/2, y_n + h/2*k2)
    k4 = f(x_n + h, y_n + h*k3)
    return y_n + h/6*(k1 + 2*k2 + 2*k3 + k4)

def step(a,b,N):
    '''Calculates the size of the step taken in a given interval \([a,b]\).

    Args:
        a (float): Point where the interval begins.
        b (float): Point where the interval ends.
        N (int): Number of steps wanted in the interval.

    Returns:
        h (float): Size of the steps that will be taken in the approximation of the function \(y(x)\).
    '''

    interval = linspace(a,b,N)
    return interval[2]-interval[1]
