class ContaBancaria:

    def __init__(self, titular='', saldo=0.0) -> None:
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    def ativar_conta(self):
        self._ativo = True 
    
    def __str__(self) -> str:
        return f'Titular: {self.titular} | Saldo: {self.saldo} | {'Ativa' if self.ativo else 'Inativa'}'
    


cb1 = ContaBancaria("Amelia",1000.59)
cb1.ativar_conta()
print(cb1)
cb2 = ContaBancaria("Laura", 9999.98)
print(cb2)