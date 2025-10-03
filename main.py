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


def cadastra_livro():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()
        
        titulo = input("Digite o titulo do livro: ").lower().strip()
        autor = input("Digite o autor do livro: ").lower().strip()
        ano = int(input("Digite o ano de publicação do livro: ").strip())
        cadastra_livro(titulo, autor, ano)

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



def lista_livros():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        for livro in cursor.fetchall():
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Disponível: {livro[4]}")
    except sqlite3.Error as error:
        print("Erro ao listar livros:", error)
    finally:
        if conexao:
            conexao.close()


def uptade_disponibilidade():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()

        id_livro = int(input("Digite o ID do livro que deseja atualizar a disponibilidade: ").strip())
        nova_disponibilidade = input("Digite a nova disponibilidade (sim/não): ").lower().strip()

        cursor.execute("""
        UPDATE livros SET disponivel = ? WHERE id = ?
        """, (nova_disponibilidade, id_livro))

        conexao.commit()
        if cursor.rowcount > 0:
            print("Disponibilidade atualizada com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido.")
    except sqlite3.Error as error:
        print("Erro ao atualizar disponibilidade:", error)
    finally:
        if conexao:
            conexao.close()


def remove_livro():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()

        id_livro = int(input("Digite o ID do livro que deseja remover: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))

        conexao.commit()
        if cursor.rowcount > 0:
            print(f"Livro com ID {id_livro} removido com sucesso! ")
        else:
            print("Nenhum livro foi encontrado com o ID fornecido.")
    except sqlite3.Error as error:
        print("Erro ao remover livro:", error)
    finally:
        if conexao:
            conexao.close()

def menu():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()

        while True:
            print("\nMenu:")
            print("1. Cadastrar livro")
            print("2. Listar livros")
            print("3. Atualizar disponibilidade")
            print("4. Remover livro")
            print("5. Sair")
            opcao = input ("Escolha uma opção: ")
            match opcao:
                case "1": cadastra_livro()
                case "2": lista_livros()
                case "3": uptade_disponibilidade()
                case "4": remove_livro()
                case "5":
                    print("Acesso encerrado")
                    break
    except sqlite3.Error as error:
        print("Erro na operação do menu:", error)
    finally:
        if conexao:
            conexao.close()

menu()