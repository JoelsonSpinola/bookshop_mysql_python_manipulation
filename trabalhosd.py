
import mysql.connector as msql#importando o mysql.connector
from mysql.connector import Error#importando o Error

try:
    #dar acesso a base de dados, com o usuario root, senha do usuario, host localhost, database Livraria
    conn = msql.connect(user='root', password='add root password',
                        host='localhost', database='Livraria',
                        auth_plugin='mysql_native_password')
    
    #escolher biblioteca para usar
    select_livraria=input("Digite 1 para livro e 2 para cd: ")
    if select_livraria == "1":
        id =input("Digite qual id de autor: ")
        select_action = input("Digite o que deseja fazer: \n 1 - Listar Livros de um Autor\n 2 - Listar Livro com Preco Menor\n 3 - Listar Livro com Preco Maior\n 4 - Quantidade de Livros\n 5 - Eliminar Livro\n")
        
        #definir o que o usuario quer fazer
        def livro_autor():#listar livros de um autor
            cursor = conn.cursor()#cursor para executar comandos sql
            comando=f"""select titulo as Nome_Livro,price as Preco,isbn as ISBN,first_name as Primeiro_Nome,last_name as Ultimo_Nome from Livro
                            inner join Autor
                            on (Livro.autor_id)=(Autor.id_autor)
                            where id_autor ={id};"""
            cursor.execute(comando)
            for i in cursor:
                    print(i)

        def livro_Menor():#listar livro com preco menor
            cursor = conn.cursor()#cursor para executar comandos sql
            comando="""select titulo, price from Livro
                        where price=(select MIN(price) from Livro);"""
            cursor.execute(comando)
            for i in cursor:
                    print(i[0],' ',i[1])

        def livro_Maior():#listar livro com preco maior
            cursor = conn.cursor()#cursor para executar comandos sql
            comando="""select titulo, price from Livro
                        where price=(select MAX(price) from Livro);"""
            cursor.execute(comando)
            for i in cursor:
                    print(i[0],' ',i[1])
        def quantia_Livros():#quantidade de livros
            cursor = conn.cursor()#cursor para executar comandos sql
            comando="""select count(*) from Livro;"""
            cursor.execute(comando)
            record = cursor.fetchone()#pega o primeiro registro da query
            print("Temos",record[0], "livros")#imprime o resultado da query
        def eleminar_Livro():
            cursor = conn.cursor()#cursor para executar comandos sql
            comando=f"""delete Livro from Livro
                        inner join Autor
                        on (Livro.autor_id)=(Autor.id_autor)
                        where id_autor={id};"""
            cursor.execute(comando)

        if select_action == "1":    #listar livros de um autor
            livro_autor()
        elif select_action == "2":  #listar livro com preco menor
            livro_Menor()
        elif select_action == "3":  #listar livro com preco maior
            livro_Maior()
        elif select_action == "4":  #quantidade de livros
            quantia_Livros()
        elif select_action == "5":  #eliminar livro
            eleminar_Livro()
        else:
            print("Opcao invalida")
            conn.close()    
        #criar um cursor que vai permitir usar as funcoes do mysql em python
        if conn.is_connected():#se estiver conectado
            cursor = conn.cursor()#cursor para executar comandos sql
            comando="use Livraria;"
            cursor.execute(comando)#executa a query
    
    elif select_livraria == "2":
        id =input("Digite qual id de artista: ")
        select_action = input("Digite o que deseja fazer: \n 1 - Listar Cds de um Autor\n 2 - Listar Cd com Preco Menor\n 3 - Listar Cd com Preco Maior\n 4 - Quantidade de Cds\n 5 - Eliminar Cd\n")
        def cd_autor():#listar cds de um autor
            cursor = conn.cursor()#cursor para executar comandos sql
            comando=f"""select titulo_album as Nome,genero as Genero_Musical,ano_lancamento as Ano,numero_disco as Numero,duracao as Tempo,
                        first_name as Primeiro_Nome,last_name as Apelido from CD_DVD
                        inner join Artist
                        on (CD_DVD.artist_id)=(Artist.id_Artist)
                        where id_Artist={id};"""
            cursor.execute(comando)
            for i in cursor:
                    print(i)    
        def cd_Menor():#listar cd com preco menor  
            cursor = conn.cursor()#cursor para executar comandos sql
            comando="""select titulo_album, preco_album from CD_DVD
                        where preco_album=(select MIN(preco_album) from CD_DVD);"""
            cursor.execute(comando)
            for i in cursor:
                    print(i)
        def cd_Maior():#listar cd com preco maior
            cursor = conn.cursor()#cursor para executar comandos sql
            comando="""select titulo_album, preco_album from CD_DVD
                        where preco_album=(select MAX(preco_album) from CD_DVD);"""
            cursor.execute(comando)
            for i in cursor:
                    print(i)
        def quantia_Cds():#quantidade de cds
            cursor = conn.cursor()#cursor para executar comandos sql
            comando="""select count(titulo_album) from CD_DVD;"""
            cursor.execute(comando)
            record = cursor.fetchone()#pega o primeiro registro da query
            print("Temos ",record, "cds")#imprime o resultado da query
        def eleminar_Cd():
            cursor = conn.cursor()
            comando="""delete CD_DVD from CD_DVD
                        inner join Artist
                        on (CD_DVD.artist_id)=(Artist.id_Artist)
                        where id_Artist=2;"""
            cursor.execute(comando)
        if select_action == "1":    #listar cds de um autor
            cd_autor()
        elif select_action == "2":  #listar cd com preco menor
            cd_Menor()
        elif select_action == "3":  #listar cd com preco maior  
            cd_Maior()
        elif select_action == "4":  #quantidade de cds
            quantia_Cds()
        elif select_action == "5":  #eliminar cd
            eleminar_Cd()
        else:
            print("Opcao invalida")
            conn.close()

except Error as e:#se ocorrer erro
    print("Error while connecting to MySQL", e)#imprime mensagem de erro

