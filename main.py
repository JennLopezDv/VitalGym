from usuarios import validar_usuario

def login():
    print(">>> LOGIN <<<")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    valido, rol = validar_usuario(usuario, contraseña)
    
    if valido:
        print(f"¡Bienvenido, {usuario}!\n--{rol}--")
        return True
    else:
        print("¡Error en credenciales!")
        return False     
    
        
    
login()