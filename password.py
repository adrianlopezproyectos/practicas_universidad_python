print("================")
print("== CONTRASEÑA ==")
print("================")



def verificar():

    contador=0

    while contador < 5:
      password = input('ingrese una contraseña de 8 o mas caracteres: ')
      contador+=1
      
      if contador == 5:
        print('su cuenta ha sido bloqueada, comuniquese con servicio.')
      else:
        caracteres=len(password)   
        
        if caracteres >= 8:

          def no_white():
            for espacio in password:
              if " " not in password:
                print("contraseña exitosa")
                break 
              else:
                print("introduzca nuevamente la contraseña sin espacios en blanco")
                break
          no_white()

          return 0
          break
        else:
          print('la contraseña es muy corta, vuelva a ingresar nuevamente')

verificacion = verificar()    
print(verificacion)
