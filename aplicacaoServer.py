from enlace import *
import time
import numpy as np
import random
import binascii
from utils import Pack

def main():
    try:
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com4 = enlace('COM4')
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com4.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("ON")
        #aqui você deverá gerar os dados a serem transmitidos. 
        # imageR = "./imgs/image.png"
        # imageW = "./imgs/recebidaCopia.png"
        #seus dados a serem transmitidos são uma lista de bytes a serem transmitidos. Gere esta lista com o 
        #nome de txBuffer. Esla sempre irá armazenar os dados a serem enviados.
        #faça aqui uma conferência do tamanho do seu txBuffer, ou seja, quantos bytes serão enviados.
        #finalmente vamos transmitir os tados. Para isso usamos a funçao sendData que é um método da camada enlace.
        #faça um print para avisar que a transmissão vai começar.
        #tente entender como o método send funciona!
        #Cuidado! Apenas trasmitimos arrays de bytes! Nao listas!
       
        # A camada enlace possui uma camada inferior, TX possui um método para conhecermos o status da transmissão
        # Tente entender como esse método funciona e o que ele retorna
        #Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        #Observe o que faz a rotina dentro do thread RX
        #print um aviso de que a recepção vai começar.
        print("recebendo dados...")
        #Será que todos os bytes enviados estão realmente guardadas? Será que conseguimos verificar?
        #Veja o que faz a funcao do enlaceRX  getBufferLen
        #acesso aos bytes recebidos
        txLen, nRx = com4.getData(1)
        txLen = int.from_bytes(txLen, "big")
        print("Bytes a serem recebidos:",txLen)
        rxBuffer, nRx = com4.getData(txLen)
        comandos = rxBuffer.split(b'\x01')[0:-1]
        print("AAAAAAAAAAAAAAAa", Pack(rxBuffer))
        print("Tamanho do buffer de chegada:",com4.rx.getBufferLen())
        # print("Lista de comandos recebida:",comandos)
        # print("Quantidade de comandos:",len(comandos))
        print("Enviando comprovação...")
        lenBuffer =  (len(comandos)).to_bytes(1, byteorder='big')
        com4.sendData(np.asarray(lenBuffer))
        print("Bytes recebidos:",lenBuffer)
    
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com4.disable()        
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com4.disable()        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()