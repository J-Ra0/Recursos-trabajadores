'''
Este programa deberás reescribir la función genera según las restricciones de tu problema.
Por defecto, el primer test se introducirá en samples
'''

import subprocess
import shutil
import os

import random

def genera ():
    ans = str(random.randint(1, 20))
    return ans

def borrar_carpeta(ruta_carpeta):
    """Borra una carpeta y todo su contenido.

    Args:
        ruta_carpeta: La ruta de la carpeta a eliminar.
    """
    try:
        shutil.rmtree(ruta_carpeta)
        os.mkdir(ruta_carpeta)
        print(f"Carpeta '{ruta_carpeta}' eliminada exitosamente.")
    except OSError as e:
        print(f"Error al eliminar la carpeta '{ruta_carpeta}': {e}")
    
if __name__ == "__main__":
    borrar_carpeta("./Output/sample")
    borrar_carpeta("./Output/secret")
    try: 
        subprocess.run('g++ -std=c++17 -O3 -o main.exe "./Solver/solver.cpp"', capture_output=True, text=True)
    except:
        print("Error: There is no cpp file in Solver called 'solver.cpp'")
        exit()

    testcases = -1
    while testcases <= 0:
        try:
            testcases = int(input("Cuantos test quieres crear "))
        except:
            print("El número de test debe ser mayor a 0 y debe ser un número")
    for i in range(testcases):
        input = genera()
        with open("./Solver/input.in", "w") as f:
            f.write(input)
            
        resultado = subprocess.run(['./main.exe'], stdin=open('./Solver/input.in', "r"), capture_output=True, text=True, check=True)
        
        if (i == 0):
            with open(f"./Output/sample/1.in", "w") as f:
                f.write(input)
            with open(f"./Output/sample/1.ans", "w") as f:
                f.write(resultado.stdout)
        else:
            with open(f"./Output/secret/{i}.in", "w") as f:
                f.write(input)
            with open(f"./Output/secret/{i}.ans", "w") as f:
                f.write(resultado.stdout)
        