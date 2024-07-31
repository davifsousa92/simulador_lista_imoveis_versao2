from modelos.lista_imoveis import Imovel

import random

imovel_1 = Imovel('Avenida Novo Horizonte','Santo André','Vila Sacadura Cabral', 174 ,'09060820','apt1')
numero_aleatorio = random.randint(1,1000)
imovel_1.receber_codigo('São Paulo',numero_aleatorio)

imovel_2 = Imovel('Rua Tibiriçá','Teresopólis','Centro', 200 ,'09060000','nenhum')
numero_aleatorio = random.randint(1,1000)
imovel_2.receber_codigo('Rio de Janeiro',numero_aleatorio)

def main():
    Imovel.listar_imoveis()

if __name__ == '__main__':
    main()
