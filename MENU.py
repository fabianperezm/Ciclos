print("seleccione una opcion: \n 1=personas \n 2=vehiculos \n 3=universidades \n 4=notas \n 5=salir")

while (True):

    opcion= int(input("Digite una opcion:1"))
    
    if opcion == 1:
        print("Usted eligiò la opcion personas")
        
    if opcion == 2:
        print("Usted eligiò la opcion vehiculos")
        
    if opcion == 3:
        print("Usted eligiò la opcion universidades")
        
    if opcion == 4:
        print("Usted eligiò la opcion notas")
        
    if opcion == 5:
        print("¡El programa ha finalizado!")
        break
    
    if opcion >=6:
        print("Opcion invalida,Elija una opcion valida")
        