"""Un script de multiplication.
"""

import os

def Multiplie_nombres(nombre1,nombre2 ):
    """Multiplication de deux nombres entiers
    Cette fonction ne sert pas à grand chose.

    Parameters
    ----------
    nombre1 : int
        Le premier nombre entier.
    nombre2 : int
        Le second nombre entier.
        Très utile.

    Returns
    -------
    int
        Le produit des deux nombres.

    """
    return nombre1 *nombre2


if __name__ == "__main__":
    print(f"2 x 3 = {Multiplie_nombres(2, 3)}")
    print (f"4 x 5 = {Multiplie_nombres(4, 5)}")
