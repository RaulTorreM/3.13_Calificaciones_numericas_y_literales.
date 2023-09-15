from Lib.Calificacion import Calificacion


if __name__ == '__main__':
    nIngresada = float(input("Ingrese la Nota a Calificar: "))
    calificacion = Calificacion()
    calificacion.Calificar(nIngresada)
