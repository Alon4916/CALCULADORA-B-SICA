#ÁREAS.py
#Programa de datos: Calculadora básica
#Autor: Alonso Valdespino López Araiza
#Grupo: 6010

print("Calculadora de Áreas")
print("Figuras disponibles:")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Círculo")
print("4. Triángulo")
print("5. Trapecio")
print("6. Rombo")
print("7. Paralelogramo")
print("8. Pentágono")

opcion = input("Elige una figura (1-8): ")

if opcion == "1":
    lado = float(input("Lado del cuadrado: "))
    lado2 = float(input("Lado 2 del cuadrado:"))
    area = lado * lado2
    print("Área del cuadrado:", area)

elif opcion == "2":
    base = float(input("Base del rectángulo: "))
    altura = float(input("Altura del rectángulo: "))
    area = base * altura
    print("Área del rectángulo:", area)

elif opcion == "3":
    radio = float(input("Radio del círculo: "))
    area = 3.1416 * radio * radio
    print("Área del círculo:", area)

elif opcion == "4":
    base = float(input("Base del triángulo: "))
    altura = float(input("Altura del triángulo: "))
    area = (base * altura) / 2
    print("Área del triángulo:", area)

elif opcion == "5":
    base_mayor = float(input("Base mayor del trapecio: "))
    base_menor = float(input("Base menor del trapecio: "))
    altura = float(input("Altura del trapecio: "))
    area = ((base_mayor + base_menor) * altura) / 2
    print("Área del trapecio:", area)

elif opcion == "6":
    d_mayor = float(input("Diagonal mayor del rombo: "))
    d_menor = float(input("Diagonal menor del rombo: "))
    area = (d_mayor * d_menor) / 2
    print("Área del rombo:", area)

elif opcion == "7":
    base = float(input("Base del paralelogramo: "))
    altura = float(input("Altura del paralelogramo: "))
    area = base * altura
    print("Área del paralelogramo:", area)

elif opcion == "8":
    perimetro = float(input("Perímetro del pentágono: "))
    apotema = float(input("Apotema del pentágono: "))
    area = (perimetro * apotema) / 2
    print("Área del pentágono:", area)

else:
    print("Opción no válida")