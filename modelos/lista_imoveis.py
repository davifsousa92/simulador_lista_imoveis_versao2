from modelos.codigo import Codigo

class Imovel:
    
    imoveis = []
    
    def __init__(self,endereco,cidade,bairro,numero,cep,complemento):
        self._endereco = endereco
        self._cidade = cidade
        self._bairro = bairro
        self._numero = numero
        self._cep = cep
        self._complemento = complemento
        self._ativo = False
        self._codigo = []
        Imovel.imoveis.append(self)

    def __str__(self):
        return f'{self._endereco} | {self._cidade} | {self._bairro} | {self._numero} | {self._cep} | {self._complemento} | {self._codigo}'

    @classmethod
    def listar_imoveis(cls):
        for imovel in cls.imoveis:
            print(f'Endereço: {imovel._endereco}')
            print(f'Cidade: {imovel._cidade}') 
            print(f'Bairro: {imovel._bairro}')
            print(f'Número: {imovel._numero}')
            print(f'CEP: {imovel._cep}')
            print(f'Complemento: {imovel._complemento}')
            print(f'Status: {imovel.ativo}\n')
            codigos_string = ', '.join(str(codigo) for codigo in imovel._codigo) 
            print(f'Código: {codigos_string}\n')
    @property
    def ativo(self):
        return 'disponivel pra venda' if self._ativo else 'indisponível'
    
    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_codigo(self,local,num_codigo):
        codigo = Codigo(local,num_codigo)
        self._codigo.append(codigo)