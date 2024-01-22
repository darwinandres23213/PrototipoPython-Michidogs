ususarios= []
datos_usuarios=[]
captura=" "
posicion=0
def crearUsuario():
    n=0
    n2=2
    print("")
    print("Bienvenido al registro de Michidogs")
    print("")
    tipo_usuario = input("Ingrese tipo de usuario (EMPRESA O PERSONA NATURAL): ")
    nombre = input("Ingrese el nombre de usuario: ")
    correo = input("Ingrese correo: ")
    contrasena = input("Ingrese contraseña: ")
    telefono=input("ingrese su numero de telefono")
    print(" ")
   

    
    while n<len(ususarios):
        if correo in ususarios[n]:
            n2=0
        n+=1
    z=2
    while z>0:
        aceptar_terminos=input("Aceptar terminos y condiciones (si/no)")
        print(" ")
        if aceptar_terminos =="si" and n2==2:
            ususarios.append( [correo,contrasena])
            datos_usuarios.append({"tipo_usuario":tipo_usuario,"nombre":nombre,"correo":correo,"contraseñas":contrasena,"telefono":telefono})
            nombre=" "
            correo=" "
            print("Su cuenta se creo exitosamente")
            print(" ")
            ingresarSistema()
            z=0

        elif aceptar_terminos=="no" and n2==2:
            print("Debe aceptar Terminos y condiciones")
            print(" ")
        elif n2==0:
            print("el usuario ya se encuentra registrado")
            print(" ")
            sesion=input("Desea iniciar sesión (si/no)")
            if sesion=="si":
                ingresarSistema()
            z=0

   


def ingresarSistema():
    n=0
    global captura
    global posicion
    print(" ")
    print("Inicio de sesión")
    print(" ")
    z=2
    n=0
    while z>0:
        correo = input("Ingrese el correo: ")
        contrasena = input("Ingrese contraseña: ")
        n=0
        n2=3
        while n<(len(ususarios)):
            if correo in ususarios[n] and contrasena in ususarios[n]:
                n2=0
                z=0
                captura=datos_usuarios[n]
                posicion=n
                inicioSesion()
                break
            elif correo in ususarios[n] and  contrasena != ususarios[n]:
                n2=2
            
            n+=1
        if n2==2:
            print("contraseña incorrecta")
            print(" ")
            opcion=input("Desea recuperar la contraseña (si/no) ")
            if opcion=="si":
                RecuperarContrasena()

        elif n2==3:
            print("usuario no encontrado")
            print("")
            opcion=input("Desea Registrarse (si/no) ")
            if opcion=="si":
                crearUsuario()


            z=0
        

def RecuperarContrasena():
    n=2
    n2=2
    z=2
    z1=0

       
    while z>0:
        global captura
        correo=input("Por favor digite el correo: ")
        print("")
        print("Continuar")
        print("si")
        print("no")
        continuar=(input(""))
        while z1<len(ususarios):
            if correo in ususarios[z1]:
                n2=0
                break
        n+=1

        if continuar=="si" and n2==0:
            print("")
            print("Enviar Codigo de verficación")
            print(" ")
            while n>0:
                newContrasena=input("Digite nueva contraseña: ")
                conContrasena=input("Confirmar Contraseña: ")
                if (newContrasena==conContrasena):
                    del ususarios[z1][1]
                    ususarios[z1].insert(1,newContrasena)
                    print("")
                    print("Su contraseña se cambió correctamente")
                    n=0
                    z=0
                else:
                    print("La confirmación de la contraseña no corresponde")
                    print("Vuelva a digitar nueva contraseña")
        
        else:
         print("")
         print("Correo no registrado")
         print("")
         z=0

def  cambiarDatos():
    global posicion
    global captura
    n=2
    n2=2
    print("Cambiar Datos Cuenta")
    
    while n>0:
         print("1. Nombre")
         print("2. Tipo de usuario")
         print("3. Telefono")
         print("4. correo")
         print("5. contraseña")
         opcion=int(input("Elija el dato que desea cambiar"))
         if opcion==1:
             print("")
             new_Nombre=input("ingrese Nuevo_Nombre")
             print("")
             captura["nombre"]=new_Nombre
         elif opcion==2:
             print("")
             new_Tipo=input("Ingrese el tipo de usuario")
             print("")
             captura["tipo_usuario"]=new_Tipo
         elif opcion==3:
             print("")
             new_Telef=input("digite el nuevo Numero teléfonico")
             print("")
             captura["telefono"]=new_Telef
         elif opcion==4:
             print("")
             new_Correo=input("Por favor ingrese el nuevo correo eléctronico")
             print("")
             captura["correo"]=new_Correo
             del ususarios[posicion][0]
             ususarios[posicion].insert(0,new_Correo)

         elif opcion==5:
             RecuperarContrasena()
         else:
             print("")
             print("Opcion Invalida")
             print("")
         while n2>0:
            print("")
            print("Desea cambiar otro dato ")
            print("si")
            print("no")
            opcion2=input("")
            if opcion2=="si":
                n2=0
            else:
                n2=0
                n=0
def mostrar_Usuarios():
    global captura

    for clave, valor in captura.items():
        print(clave)
        print(valor)
        print( " ")

def inicioSesion():
       global captura
       global posicion
       
       print(" ")
       print("------Bienvenido " + captura["nombre"]+" a MichisandDogs-------")
       print("")
     
       z=2
       while z>0:
        print(" ")
        print("MENU-USUARIO")
        print(" ")
        print("1- cambiar datos")
        print("2- Mostrar datos de usuario")
        print("3- ver productos")
        print("6- salir")
        opcion=int(input(""))

        if  opcion==1:
            cambiarDatos()
        elif opcion==2:
            mostrar_Usuarios()
        elif opcion==3:
            Productos()
        elif opcion==6:
            z=0
            captura=" "
        else:
            print("")
            print("opcion incorrecta")
            print("")
def informacion_michidogs():
    n=2
    while n>0:
        print("")
        print("1-Terminos y condiciones michidogs")
        print("2-Politica y privacidad")
        print("3-Quienés somos")
        print("4-volver menu_principal")
        print(" ")
        opcion=int(input(""))

        if opcion==1:
            print("Todo el contenido presente en esta página web, incluyendo pero no limitado a texto, gráficos, logotipos es propiedad exclusiva de los propietarios de la página web y está protegido por las leyes de propiedad intelectual. ")
            print(" ")
        elif opcion==2:
            print("Nos comprometemos a proteger su privacidad y a cumplir con todas las leyes y regulaciones aplicables en materia de protección de datos.")
            print("")
        elif opcion==3:
            print("Somos una sitio  web en donde podrás encotrar muchos articulos para tu mascota. ")
            print(" ")
        elif opcion==4:
            n=0
def Productos():
    n=2
    while n>0:
        print("")
        print("1-productos para perro")
        print("2-productos para gatos")
        print("3-productos para conejos")
        print("4-volver")
        opcion=int(input(""))
        if opcion==1:
            n2=2
            while n2>0:
                print("1-dogchao-comida=20.000")
                print("2-Kit limpieza dogs=15.000")
                print("3-juguete_hueso==6.000")
                print("4-pañoleta=4.000")
                print("")
                compra=input("Desea reservar algún artículo (si/no): ")
                print(" ")
                if compra=="si":
                    opcion2=int (input(" opción del artículo: "))
                    if opcion2==1:
                        print(" ")
                        print("Reservaste el producto dogchao-comida")
                        print(" ")
                    elif opcion2==2:
                        print(" ")
                        print("Reservaste el producto kit limpieza dogs")
                        print(" ")
                    elif opcion2==3:
                        print(" ")
                        print("Reservaste el producto juguete_Hueso")
                        print(" ")
                    elif opcion2==4:
                        print(" ")
                        print("Reservaste el producto pañoleta")
                        print(" ")
                else:
                    n2=0
        elif opcion==2:
            n2=2
            while n2>0:
                print("1-catchao-comida=10.000")
                print("2-Kit limpieza cats=11.000")
                print("3-juguete_ratón==6.000")
                print("4-puntero láser=4.000")
                print("")
                compra=input("Desea reservar algún artículo (si/no): ")
                print(" ")
                if compra=="si":
                    opcion2=int (input(" opción del artículo: "))
                    if opcion2==1:
                        print("Reservaste el producto catchao-comida")
                        print(" ")
                    elif opcion2==2:
                        print("Reservaste el producto kit limpieza cats")
                        print(" ")
                    elif opcion2==3:
                        print("Reservaste el producto juguete_ratón")
                        print(" ")
                    elif opcion2==4:
                        print("Reservaste el producto puntero laser")
                else:
                    n2=0

        elif opcion==3:
            n2=2
            while n2>0:
                print("1-conejo-comida=40.000")
                print("2-juguete zanahoria =11.000")
                print("3-kit medicina conejo==6.000")
                print("")
                compra=input("Desea reservar algún artículo (si/no): ")
                print(" ")
                if compra=="si":
                    opcion2=int (input(" opción del artículo: "))
                    if opcion2==1:
                        print("Reservaste el producto conejo-comida")
                        print(" ")
                    elif opcion2==2:
                        print("Reservaste el producto juguete zanahoria")
                        print(" ")
                    elif opcion2==3:
                        print("Reservaste el producto kit medicina")
                        print(" ")
                else:
                    n2=0
        elif opcion==4:
            n=0


       
n=1
while n>0:
    print(" ")
    print("Menu_Principal Michidogs ")
    print(" ")
    print("1- Crear Usuario") 
    print("2- Ingresar al sistema")
    print("3- Recuperar Contraseña")
    print("4-Saber más de michidogs")
    opc = int(input("Seleccione una opcion"))

    if opc == 1:
        crearUsuario()
    elif opc ==2:
        ingresarSistema()
    elif opc==3:
        RecuperarContrasena()
    elif opc==4:
        informacion_michidogs()
    