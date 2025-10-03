import sqlite3


conexao = sqlite3.connect('biblioteca.db')

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT                            
    )
""")

def cadastra_livro(titulo, autor, ano):
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()
        
        cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponivel) VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, "sim"))

        conexao.commit()
        if cursor.rowcount > 0:
            print("Livro cadastrado com sucesso!")
            print("Título:", titulo)
            print("Autor:", autor)
            print("Ano:", ano)
        else:
            print("Falha ao cadastrar o livro.")


    except sqlite3.Error as error:
        print("Erro ao cadastrar livro:", error)
    finally:
        if conexao:
            conexao.close()

titulo = input("Digite o titulo do livro: ").lower().strip()
autor = input("Digite o autor do livro: ").lower().strip()
ano = int(input("Digite o ano de publicação do livro: ").strip())
cadastra_livro(titulo, autor, ano)
