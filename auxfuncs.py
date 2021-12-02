# various helper functions for juypter notebooks
from IPython.display import display, Latex
import numpy as np


def pmatrix(a):
    """Returns a LaTeX pmatrix

    :a: numpy array
    :returns: LaTeX pmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('pmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{pmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{pmatrix}']
    return '\n'.join(rv)

# ab hier nix verändern


def gen_A_x_b(Anzahl=3, max_n=5, max_m=5, min_zahl=-5, max_zahl=+5, x_as_Matrix=False):
    # generates dict of triples: matrix A, vector x and r.h.s. vector b
    # for each value of dict, A*x=b holds true
    # keys are indices

    A_x_b_dict = {}

    for i in range(Anzahl):
        #print('Aufgabe Nr.', k+1)
        

        n = np.random.randint(2, max_n+1)
        m = np.random.randint(2, max_m+1)
        if x_as_Matrix:
            k = np.random.randint(2, max_m+1)
        else:
            k = 1

        A = np.random.randint(min_zahl,max_zahl,[n,m])
        x = np.random.randint(min_zahl,max_zahl,[m,k])
        
        b = np.matmul(A,x)

        A_x_b_dict[i+1]=(A,x,b)

    return A_x_b_dict

def print_A_x_b(A_x_b_dict, with_solution=False):
    # print A*x or, respectively, A*x=b in neat latex style

    for key in A_x_b_dict:
        if with_solution:
            print('Lösung zu Aufgabe Nr.', key)
        else:
            print('Aufgabe Nr.', key)

        # unpack A, x, b
        A, x, b = A_x_b_dict[key]
        
        latex_str = r'\begin{eqnarray}'
        latex_str += pmatrix(A)
        latex_str += '\cdot'
        latex_str += pmatrix(x)
        latex_str += '='
        if with_solution:
            latex_str += pmatrix(b)
        else:
            latex_str += '?'
        latex_str += '\end{eqnarray}'

        display(Latex(latex_str))