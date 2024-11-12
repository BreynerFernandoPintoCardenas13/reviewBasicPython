calificacion = int(input("Ingresa la calificación (0-100): "))


match calificacion: 
    case calificacion if 90 <= calificacion <= 100:
        print("La calificación es: A")
    case calificacion if 80 <= calificacion < 90:
        print("La calificación es: B")
    case calificacion if 70 <= calificacion < 80:
        print("La calificación es: C")
    case calificacion if 60 <= calificacion < 70:
        print("La calificación es: D")
    case _ if 0 <= calificacion < 60:
        print("La calificación es: F")
    case _:
        print("Calificación inválida. Debe estar entre 0 y 100.")
