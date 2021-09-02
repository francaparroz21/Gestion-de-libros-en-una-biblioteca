from soporte import *
import random

print("=======================================================")
print("Trabajo Practico 3: Gestión de LIbros en una Biblioteca")
print("=======================================================")

menu = "1________ Generacion y carga\n" \
       "2________ Mostrar \n"\
       "3________ Conteo y género más popular \n"\
       "4________ Búsqueda del mayor \n"\
       "5________ Búsqueda por ISBN \n"\
       "6________ Consulta de un género \n"\
       "7________ Consulta de precio por grupo \n"\
       "8________ Salir\n" \

genero_menu = "0________ Autoayuda \n" \
              "1________ Arte\n" \
              "2________ Ficcion \n"\
              "3________ Computacion \n"\
              "4________ Economia \n"\
              "5________ Escolar \n"\
              "6________ Sociedad \n"\
              "7________ Gastronomia \n"\
              "8________ Infantil \n" \
              "9________ Otros \n"  \

idioma_menu = "1________ Español\n" \
              "2________ Ingles \n"\
              "3________ Frances \n"\
              "4________ Italiano \n"\
              "5________ Otros \n"\

def validar(mensaje):
    n = 0
    while n <= 0:
        n = int(input(mensaje))
        if n <= 0:
            print("Valor incorrecto, vuelva a intentar")
    return n

def validar_isbn():
    variable_anterior = ""
    variable_anterior_anterior = ""
    digitos = ("0","1","2","3","4","5","6","7","8","9")
    grupos = 0
    digitos_cont = 0
    vector = []
    mod11 = False
    resultado = 0
    valido = False
    while valido == False:
        isbn = str(input("Ingrese el codigo de identificacion (ISBN): "))
        for c in isbn:
            if c in digitos:
                digitos_cont += 1
                vector.append(c)
                if variable_anterior == "-" and variable_anterior_anterior in digitos:
                    grupos += 1
            variable_anterior_anterior = variable_anterior
            variable_anterior = c
        resultado = (int(vector[0])*10)+(int(vector[1])*9)+(int(vector[2])*8)+(int(vector[3])*7)+(int(vector[4])*6)+(int(vector[5])*5)+(int(vector[6])*4)+(int(vector[7])*3)+(int(vector[8])*2)+(int(vector[9])*1)
        if resultado % 11 == 0:
                mod11 = True
        if digitos_cont == 10 and grupos == 3 and mod11 == True:
            valido = True
        if valido == False:
            print("Valor incorrecto, vuelva a intentarlo")
        digitos_cont = 0
        grupos = 0
        mod11 = False
        vector = []

    return isbn

def pasar_genero(gen):
    genero = ["Autoayuda","Arte","Ficcion","Computacion","Economia","Escolar","Sociedad","Gastronomia","Infantil","Otros"]
    return genero[gen]

def pasar_idioma(id):
    idioma = ["Español","Ingles","Frances","Italiano","Otros"]
    return idioma[id - 1]

def cargar(libros):
    for v in range(len(libros)):
        tit = str(input("Ingrese el Titulo del libro: "))
        print(genero_menu)
        gen = int(input("Ingrese el genero: "))
        print(idioma_menu)
        id = int(input("Ingrese el idioma: "))
        prec = float(input("Ingrese el precio del libro: "))
        isbn = validar_isbn()
        libros[v] = Libro(tit,gen,id,prec,isbn)

def mostrar(libros):
    l = 0
    for i in range(len(libros)):
        l += 1
        print("Libro", l)
        write(libros[i])
    return l

def contar_genero(libros):
    vector = [0] * 10
    maximo = 0
    maximo_indice = 0
    for i in range(len(libros)):
        vector[libros[i].genero] += 1

    for j in range(10):
        print("Genero: ",pasar_genero(j)," - ","Cantidad: ",vector[j])
        if vector[j] > maximo:
            maximo = vector[j]
            maximo_indice = j
    print("El genero con mas libros fue: ", pasar_genero(maximo_indice))

def busqueda_mayorid(libros):
    idioma = str(input("Ingrese el idioma para buscar el libro de mayor precio: "))
    precio = 0
    precio_indice = 0
    for i in range(len(libros)):
        if libros[i].precio > precio and idioma == pasar_idioma(libros[i].idioma):
            precio = libros[i].precio
            precio_indice = i
    print("El precio mayor para", idioma, "es: ",precio)
    print("El libro con mayor precio en",idioma,"es: ", write(libros[precio_indice]))

def busqueda_isbn(libros):
    isbn_buscar = str(input("Ingrese el ISBN a buscar: "))

    for i in range(len(libros)):
        if libros[i].isbn == isbn_buscar:
            libros[i].precio += (10 * libros[i].precio) / 100
            write(libros[i])
            break

def consulta_genero(libros):
    vector = [0] * 10
    maximo = 0
    maximo_indice = 0
    for i in range(len(libros)):
        vector[libros[i].genero] += 1

    for j in range(10):
        if vector[j] > maximo:
            maximo = vector[j]
            maximo_indice = j

    for i in range(len(libros)):
        if libros[i].genero == maximo_indice:
            write(libros[i])

def automatico(libros):
    isbn_random =('61-3177-316-5','16-4330-155-1','53-2839-286-8','28-8545-602-7','42-5845-184-3','31-6792-236-2','31-7588-262-5','36-8087-484-7','67-8059-065-7','64-0544-620-4','48-6651-038-2','91-2471-184-5','87-8496-415-4','16-0293-656-0','92-1732-242-3','30-9630-660-5','89-0131-232-8','15-6157-955-6','31-2301-233-6','02-1829-551-0','78-2828-285-0','50-9880-787-5','02-5551-370-4','13-8922-728-6','20-9791-236-2','10-4889-576-9','03-4776-932-2','31-9700-596-1','96-9820-636-1','04-7475-885-0','33-5596-636-3','80-4698-183-4','90-1314-479-9','18-6572-539-0','73-4579-709-0','84-5126-788-2','19-0758-698-9','50-1358-072-2','03-1474-198-4','80-2305-844-4','88-0423-472-5','14-5005-138-3','03-2133-601-1','75-4790-522-6','09-8608-731-9','89-4468-962-8','12-3899-839-9','78-8086-046-0','19-9887-546-6','69-0824-652-3','12-5615-994-8','95-3205-769-2','40-2022-702-0','34-9220-703-0','43-6282-192-9','90-9442-965-9','04-2994-829-8','21-1122-441-3','73-9162-945-6','56-2228-775-8','22-3284-714-4','56-3028-313-8','35-3633-457-1','31-2897-939-1','54-7522-944-9','15-2312-179-3','00-0388-652-2','48-6607-489-2','64-0894-661-5','60-6459-607-4','38-1244-182-9','82-2634-052-7','25-6101-779-6','76-3191-541-5','97-8692-766-4','04-7720-608-5','89-6112-927-9','99-3605-322-2','22-6748-832-9','52-4947-632-5','85-5960-647-5','49-0694-286-5','66-2917-904-8','48-4778-671-8','32-7298-367-8','01-3369-315-5','31-7495-383-9','85-6607-373-8','26-9464-800-2')
    nomlibros = ("Don Quijote","Historia de dos ciudades","El Señor de los Anillos","Harry Potter y la piedra filosofal","El código Da Vinci","El principito","El infinito en un junco","Un cuento perfecto","Lo que la marea esconde","El arte de engañar al karma","Sin miedo","Nosotros en la luna","A través de mi ventana","El juego del alma","Todo lo que nunca fuimos","Reina roja","Hamnet","El paciente","Todo lo que somos juntos","Los Compas perdidos en el espacio","Feria","Loba negra","El olvido que seremos","La desaparición","Rey blanco","La anomalía","Sapiens. De animales a dioses","El poder del ahora","Tierra","Hay momentos que deberían ser eternos","Dime qué comes y te diré qué bacterias tienes","Panza de burro","El príncipe cruel","La cara norte del corazón","El día que se perdió la cordura","El día que se perdió el amor","En plena noche","Cuando no queden más estrellas que contar","Castellano","Los años extraordinarios","Hábitos atómicos","El hombre en busca de sentido","Invisible","Asesino de brujas","Independencia","Heist","Un amor","GUARDIANES DE LA NOCHE","Culpa nuestra (Culpables 3)","Una corte de rosas y espinas","Todo lo que sucedió con Miranda Huff","Los ingratos","Ética para Celia","Un lugar a donde ir","Biografía del silencio","Los Compas y la cámara del tiempo","Madre patria","Arsène Lupin, caballero ladrón","El reino")
    for i in range(len(libros)):
        tit = random.choice(nomlibros)
        gen = random.randint(0,9)
        id = random.randint(1,5)
        prec = random.randint(100,99999)
        isbn = random.choice(isbn_random)
        libros[i] = Libro(tit,gen,id,prec,isbn)

def consulta_preciogrupo(libros):
    n_isbn = int(input("Ingrese la cantidad de ISBN a ingresar: "))
    vector = [0] * n_isbn
    flagA = False
    for i in range(n_isbn):
        isbn = str(input("Ingrese el ISBN: "))
        vector[i] = isbn
    for j in range(len(vector)):
        for i in range(len(libros)):
            if vector[j] == libros[i].isbn:
                write(libros[i])
                flagA = True
                break

        if not flagA:
            print("El libro",vector[j],"No se encuentra en el catalogo")
        flagA = False

def principal():
    opcion = 0
    carga = False
    while opcion != 8:
        print(menu)
        opcion = int(input("Ingrese una opcion (8 para terminar): "))
        if opcion == 1:
            n = validar("Ingrese la cantidad de libros: ")
            libros = [None] * n
            manual_automatico = int(input("Ingrese si va a cargar los libros manualmente(1) o automaticamente(2): "))
            if manual_automatico == 1:
                cargar(libros)
                carga = True
            elif manual_automatico == 2:
                automatico(libros)
                carga = True
        elif opcion == 2:
            if carga == True:
                l = mostrar(libros)
            else:
                print("Cargue los datos para poder mostrarlos")
        elif opcion == 3:
            if carga:
                contar_genero(libros)
            else:
                print("Cargue los datos para poder mostrarlos")
        elif opcion == 4:
            if carga:
                busqueda_mayorid(libros)
            else:
                print("Cargue los datos para poder mostrarlos")
        elif opcion == 5:
            if carga:
                busqueda_isbn(libros)
            else:
                print("Cargue los datos para poder mostrarlos")
        elif opcion == 6:
            if carga:
                consulta_genero(libros)
            else:
                print("Cargue los datos para poder mostrarlos")
        elif opcion == 7:
            if carga:
                consulta_preciogrupo(libros)
            else:
                print("Cargue los datos para poder mostrarlos")

if __name__ == "__main__":
    principal()






