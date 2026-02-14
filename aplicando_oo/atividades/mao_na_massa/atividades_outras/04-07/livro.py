class Livro:

    livros :list = []

    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        self.livros.append(self)

    def __str__(self) -> str:
        return f'Titulo: {self._titulo.ljust(5)}|Autor: {self._autor.ljust(5)}|Ano Publi.: {str(self._ano_publicacao).ljust(5)}|Disponível: {'sim' if self._disponivel else 'não'}'
    
    def emprestar(self):
        self._disponivel = False

    @classmethod
    def verificar_disponibilidade(cls, ano):
        for livro in Livro.livros:
            if livro._ano_publicacao == ano and livro._disponivel == True:
                print(livro)

        


livro_1q84 = Livro("1Q84","Haruri",2026)
print(livro_1q84)
livro_1q84.emprestar()
print(livro_1q84)

livro_eragon = Livro("Eragon", "Fulanihno", 2026)
livro_eragon2 = Livro("Eragon2", "Fulanihno", 2026)
livro_eragon2.emprestar()

livro_eragon3 = Livro("Eragon3", "Fulanihno", 2026)

Livro.livros = [livro_1q84, livro_eragon, livro_eragon2, livro_eragon3]

print("Livro disponiveis para emprestimo:")
Livro.verificar_disponibilidade(2026)