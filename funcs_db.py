from msilib.schema import ControlEvent
import sqlite3

conexao = sqlite3.connect("id.db")
cursor = conexao.cursor()

# if conexao.total_changes == 0:
#     cursor.execute("CREATE TABLE id (chat_id INTEGER)")

# def verifica_cria_db():
#     conexao = sqlite3.connect("id.db")
#     cursor = conexao.cursor()
#     cursor.execute("CREATE TABLE id (chat_id INTEGER)")


def salvar_id(id_user):
    # primeiro ver se já tem um banco criado
    # verifica_cria_db()
    cursor.execute(f"INSERT INTO id VALUES ({id_user})")

# salvar_id(124)
# salvar_id(123)

print(cursor.execute("SELECT chat_id FROM id").fetchall())