class IdadeInvalidaError(Exception):
    pass

class Pessoa:

    def __init__(self, nome='', idade=0, profissao='') -> None:
        self._nome = nome
        self.idade = idade
        self._profissao = profissao

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @property
    def profissao(self):
        return self._profissao
    
    @idade.setter
    def idade(self, value):
        if value >= 0:
            self._idade = value
        else:
            raise IdadeInvalidaError(f'Idade não pode ser negativa: {value}')

    def __str__(self) -> str:
        return f'Saudacoes para {self.nome}, {self.idade}, {self.profissao}'
    
    def aniversario(self) -> None:
        self.idade += 1
    


try:
    p1 = Pessoa("Thiago", -4, "QA")
    print(p1)
except IdadeInvalidaError as e:
    print(f'Erro ao criar pessoa: {e}')

