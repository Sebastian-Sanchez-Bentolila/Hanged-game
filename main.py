# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

#Modules
from colorama import Fore, init
import os
import random

#To change the text color in the cmd
init()

#To clean the screen
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


#Dictionary with drawings
dibujos = {
    0 : '''
    ╔ -------╗
    |        |
    |        
    |        
    |         
    |        
    |
    ╚-- ''',
    1 : '''
    ╔ -------╗
    |        |
    |        O       
    |        
    |         
    |        
    |
    ╚-- ''',
    2 : '''
    ╔ -------╗
    |        |
    |        O       
    |        |       
    |         
    |        
    |
    ╚-- ''',
    3 : '''
    ╔ -------╗
    |        |
    |        O       
    |       \|       
    |         
    |        
    |
    ╚-- ''',
    4 : '''
    ╔ -------╗
    |        |
    |        O       
    |       \|/       
    |         
    |        
    |
    ╚-- ''',
    5 : '''
    ╔ -------╗
    |        |
    |        O       
    |       \|/       
    |        |      
    |        
    |
    ╚-- ''',
    6 : '''
    ╔ -------╗
    |        |
    |        O       
    |       \|/       
    |        |      
    |       /       
    |
    ╚-- ''',
    7 : '''
    ╔ -------╗
    |        |
    |        O       
    |       \|/       
    |        |      
    |       / \      
    |
    ╚-- '''
}


#Main Class - Game
class Juego():
    def __init__(self):
        self.Adivinar_Palabra = ['argentina', 
                                'peru', 
                                'brasil', 
                                'lego', 
                                'pepsi', 
                                'ford',
                                'python',
                                'batman',
                                'ojota',
                                'pato'] #words to guess
        self.Palabra_Secreta = random.choice(self.Adivinar_Palabra) #the random word
        self.Lista_Letras_Adivinadas = [] #Lists with the guessed letters
        self.vidas = 0 #user lives
        self.estatus = ''  #{'----'}
    
    #Hangman function       
    def Ahorcado(self):
        while True:
            
            while True:
                global dibujos
                clearConsole()
                
                print(dibujos[self.vidas])
                print("\nLa palabra contiene ", len(self.Palabra_Secreta), " letras")
                
                self.estatus = ''
                
                for letra in self.Palabra_Secreta:
                
                    if letra in self.Lista_Letras_Adivinadas:
                        self.estatus += letra
                    else:
                        self.estatus += '-'
                    
                #Print the letters that the user guessed and the letters that are missing        
                print("\n", self.estatus)
                
                if self.estatus == self.Palabra_Secreta:
                    print("¡Has ganado!, felicidades :)")
                    input("\nPresiona ENTER para continuar...")
                    break
                
                self.Letra_Usuario = input("¡Adivine una letra! : ")
                
                if len(self.Letra_Usuario) != 1 or self.Letra_Usuario.isnumeric():
                    print("\n--> Esa no es una letra")
                    
                else:
                    if self.Letra_Usuario in self.Lista_Letras_Adivinadas:
                        print("\n--> Ya intentaste con esa letra")
                        
                    else:
                        self.Lista_Letras_Adivinadas.append(self.Letra_Usuario)
                        
                        if self.Letra_Usuario.lower() in self.Palabra_Secreta:
                            print("\nFelicidades! , has acertado una letra")
                        
                        else:
                            self.vidas += 1
                            print("\nTe equivocaste, te quedan {} vidas". format(7-self.vidas))
                        
            
                if self.vidas == 7:
                    print("\nHas perdido, la palabra secreta era : {}".format(self.Palabra_Secreta))
                    input("\nPresiona ENTER para continuar...")
                    break
                
                input("\nPresiona ENTER para continuar...")
            
            break
                        

        
#Option menu
menu = '''**********
*AHORCADO*
**********

El objetivo del juego es adivinar la palabra.
¡Tienes tan solo 7 vidas!

'''


#Main Program
flag = True
while flag:
    clearConsole()
    print(Fore.CYAN + menu)
    opcion = input("¿Queres Jugar (y: yes, n: no)? : ")
    opcion = opcion.upper()
    
    #Game  
    if opcion == 'Y':
        juego = Juego().Ahorcado()
     
    #Exit   
    elif opcion == 'N':
        print("\n--> Saliendo del sistema")
        flag = False
        
    #Invalid option
    else:
        print("\n--> Esa opciòn no existe.")
        input("\nPresiona ENTER para continuar...")     