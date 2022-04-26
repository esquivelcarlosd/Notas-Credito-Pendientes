import cv2

#To get user name
import getpass
#To tabulate

#To read files on directory
from operator import index
import os
from os.path import isfile, join
import errno
#Globales
user=getpass.getuser()
archivos = ""
nombre = ""
lista = []

#Ruta global

ruta = "C:/Users/"
#Carpetas globales
carpeta2019 = "NCPO 2019/"
carpeta2020 = "NCPO 2020/"
carpeta2021 = "NCPO 2021/"
carpeta2022 = "NCPO 2022/"
#fechas 2019
julio2019 = "julio 2019/Pending accounts"
septiembre2019 = "septiembre 2019/Pending accounts"
octubre2019 = "octubre 2019/Pending"
noviembre2019 = "noviembre 2019/Pending accounts"
diciembre2019 = "diciembre 2019/Pending"
#Fechas 2020
enero2020 = "enero 2020/Pending"
febrero2020 = "febrero 2020/Pending"
marzo2020 = "marzo 2020/1 Pending"
abril2020 = "abril 2020/1 Pending"
mayo2020 = "mayo 2020/1 Pending"
junio2020 = "junio 2020/1 Pending"
julio2020 = "julio 2020/1 Pending"
agosto2020 = "agosto 2020/1 Pending"
septiembre2020 = "septiembre 2020/1 Pending"
octubre2020 = "octubre 2020/1 Pending"
noviembre2020 = "Noviembre 2020/1 Pending"
diciembre2020 = "diciembre 2020/1 Pending"
#Fechas 2021
enero2021 = "TPCM enero 2021/1 Pending"
febrero2021 = "TPCM febrero 2021/1 Pending"
marzo2021 = "TPCM marzo 2021/1 Pending"
abril2021 = "TPCM abril 2021 BHP/1 Pending"
mayo2021 = "TPCM mayo 2021/1 Pending"
junio2021 = "TPCM junio 2021/1 Pending"
julio2021 = "TPCM julio 2021/1 Pending"
agosto2021 = "TPCM Agosto 2021/1 Pending"
septiembre2021 = "TPCM septiembre 2021/1 Pending"
octubre2021 = "TPCM octubre 2021/1 Pending"
noviembre2021 = "TPCM noviembre 2021/1 Pending"
diciembre2021 = "TPCM diciembre 2021/1 Pending"
#Fechas 2022
enero2022 = "TPCM enero 2022/1 Pending"
febrero2022 = "TPCM febrero 2022/1 Pending"
marzo2022 = "TPCM marzo 2022/1 Pending"
abril2022 = "TPCM abril 2022/1 Pending"
mayo2022 = "TPCM mayo 2022/1 Pending"
junio2022 = "TPCM junio 2022/1 Pending"
julio2022 = "TPCM julio 2022/1 Pending"
agosto2022 = "TPCM agosto 2022/1 Pending"
septiembre2022 = "TPCM septiembre 2022/1 Pending"
octubre2022 = "TPCM octubre 2022/1 Pending"
noviembre2022 = "TPCM noviembre 2022/1 Pending"
diciembre2022 = "TPCM diciembre 2022/1 Pending"


#CLIENTES

empleadoUno = []
empleadoDos = []
empleadoTres = []
empleadoCuatro = []
empleadoCinco = []

"""f = open('temp.txt')
t = open('tempT.txt','w+')
t.write(f.read().replace('.xlsx','.xlsx \n'))
f.close()
t.close()"""


def obtener_nombres(ano, mes):
    global archivo
   
    
    rutaDos = ruta + ano + mes
    contenido = os.listdir(rutaDos)
    archivos = [nombre for nombre in contenido if isfile(join(rutaDos,nombre))]
    print("---------------------------------------------------------------\n")
    print("Cliente\t CSS\t Mes\t Año")
    
    if ano == carpeta2019:
        mesDos = mes[0:3]
    elif ano == carpeta2020:
        mesDos = mes[0:3]
    elif ano == carpeta2021:
         mesDos = mes[5:8]
    elif ano == carpeta2022:
        mesDos = mes[5:8]
          

    
    #Hacemos que la lista se le quite la extensión xlsx
    for i in archivos:
        archivo = i.replace(".xlsx", "")
        numbers = archivo[0:8]
        #mesDos = mes[0:8]
        anoDos = ano[5:9]
        #print(type(numbers))
        if numbers in empleadoUno:
            archivo = archivo + "\templeadoUno\t" + mesDos + "\t" + anoDos
            print(archivo)
            lista.append(archivo)
            continue
        elif numbers in empleadoDos:
            archivo = archivo + "\templeadoDos\t" + mesDos + "\t" + anoDos
            print(archivo)
            lista.append(archivo)
            continue
        elif numbers in empleadoTres:
            archivo = archivo + "\templeadoTres\t" + mesDos + "\t" + anoDos
            print(archivo)
            lista.append(archivo)
            continue
        elif numbers in empleadoCuatro:
            archivo = archivo + "\templeadoCuatro\t" + mesDos + "\t" + anoDos
            print(archivo)
            lista.append(archivo)
            continue       
        elif numbers in clientesNancy:
            archivo = archivo + "\tNancy Cardoso\t" + mesDos + "\t" + anoDos
            print(archivo)
            lista.append(archivo)            
            continue
           
        elif numbers in empleadoCinco:
            archivo = archivo + "\templeadoCinco\t" + mesDos + "\t" + anoDos
            print(archivo)
            lista.append(archivo)
            continue        
        else:
            archivo = archivo + "\tNA\t" + mesDos + "\t" + anoDos      
            print(archivo)
            lista.append(archivo)
            continue
        
    
    
    with open('temp.txt', 'w') as f:
        for elemento in lista:
            f.write(elemento)
            f.write('\n')
            

    
    print("")
    
   
    
def ano_2019():
    obtener_nombres(carpeta2019, julio2019)
    obtener_nombres(carpeta2019, septiembre2019)
    obtener_nombres(carpeta2019, octubre2019)
    obtener_nombres(carpeta2019, noviembre2019)
    obtener_nombres(carpeta2019, diciembre2019)
    
        
def ano_2020():
    obtener_nombres(carpeta2020, enero2020)
    obtener_nombres(carpeta2020, febrero2020)
    obtener_nombres(carpeta2020, marzo2020)
    obtener_nombres(carpeta2020, abril2020)
    obtener_nombres(carpeta2020, mayo2020)
    obtener_nombres(carpeta2020, junio2020)
    obtener_nombres(carpeta2020, julio2020)
    obtener_nombres(carpeta2020, agosto2020)
    obtener_nombres(carpeta2020, septiembre2020)
    obtener_nombres(carpeta2020, octubre2020)
    obtener_nombres(carpeta2020, noviembre2020)
    #obtener_nombres(carpeta2020, diciembre2020)

def ano_2021():
    obtener_nombres(carpeta2021, enero2021)
    obtener_nombres(carpeta2021, febrero2021)
    obtener_nombres(carpeta2021, marzo2021)
    obtener_nombres(carpeta2021, abril2021)
    obtener_nombres(carpeta2021, mayo2021)
    obtener_nombres(carpeta2021, junio2021)
    obtener_nombres(carpeta2021, julio2021)
    obtener_nombres(carpeta2021, agosto2021)
    obtener_nombres(carpeta2021, septiembre2021)
    obtener_nombres(carpeta2021, octubre2021)
    obtener_nombres(carpeta2021, noviembre2021)
    obtener_nombres(carpeta2021, diciembre2021)

def ano_2022():
    obtener_nombres(carpeta2022, enero2022)
    obtener_nombres(carpeta2022, febrero2022)
    """obtener_nombres(carpeta2022, marzo2022)
    obtener_nombres(carpeta2022, abril2022)
    obtener_nombres(carpeta2022, mayo2022)
    obtener_nombres(carpeta2022, junio2022)
    obtener_nombres(carpeta2022, julio2022)
    obtener_nombres(carpeta2022, agosto2022)
    obtener_nombres(carpeta2022, septiembre2022)
    obtener_nombres(carpeta2022, octubre2022)
    obtener_nombres(carpeta2022, noviembre2022)
    obtener_nombres(carpeta2022, diciembre2022)"""


    

def main():
    clear_screen()
    header()
    print('Available tasks:\n')
    print('1) Run complete process')
    print('2) 2019')
    print('3) 2020')
    print('4) 2021')
    print('5) 2022\n')
    try:
        option = ((input('Write your option (in numbers) and then, press enter: ')).upper())[0]
    except:
        option = 'X'
    task(option)
        
def task(option):
    if option == '1':
        complete_process()
        wait()
    elif option == '2':
        ano_2019()
        wait()
    elif option == '3':
        ano_2020()
        wait()
    elif option == '4':
        ano_2021()
        wait()
    elif option == '5':
        ano_2022()
        wait()
    else:
        print('Selected option is not recognized.')
        print('Please try again.')

def complete_process():
    ano_2019()
    ano_2020()
    ano_2021()
    ano_2022()
    


def header():

    print("     PROGRAMA PARA MOSTRAR LAS NCPO'S PENDIENTES\n\n\n")
    
def clear_screen():
    os.system('cls')
    
def wait():
    print(input("Press any number to exit and then, press enter: "))


if __name__ == "__main__":
    main()
