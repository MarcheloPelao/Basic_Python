#modulo para ejecutar argumentos por consola
#los argumentos se pasan como un string
# import sys
#
# print('soy el script argumento')
#
# print(sys.argv)
# #sumar argumentos
# print(int(sys.argv[1])+int(sys.argv[2]))
# #recorrer los arguemntos dentro de la aplicacion:
#
# for arg in sys.argv:
#     print(arg)
#ahora los argumentos se pasan como cadena de caracteres

#la forma anterior es la manera manal existe una más elgante que es argparse
#que permiten realizar aplicaciones de consola
# con -h se va a la ayuda
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('op1',help='primer operando',type=int)
parser.add_argument('op2',help='segundo operando',type=int)
parser.add_argument('-r','--resta',help='realiza la resta del operando 1 '
                                   'y el operando 2',action='store_true')
#--indica arguemntos opcional o -r que tambien puede pasar como resta
args=parser.parse_args()
print(args.op1)
print(args.op2)
if args.resta:
    print(args.op1-args.op2)
else:
    print(args.op1+args.op2)
