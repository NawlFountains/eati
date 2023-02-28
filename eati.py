import sys

#Si hay dos o mas argumentos , aparte del nombre, no falla
if len(sys.argv) >= 3 :
    print(sys.argv[1] +" "+sys.argv[2])
else:
    print('A lo sumo se necesitan 2 arguemtos')