import sqlite3
from typing import List, Optional

class Cliente:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

class Conexao:
    @staticmethod
    def getConnection():
        return sqlite3.connect('clientes.db')

class ClienteDAOImpl:
    def inserir(self, cliente: Cliente) -> None:
        sql = "INSERT INTO clientes (nome, email) VALUES (?, ?)"
        
        try:
            conn = Conexao.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql, (cliente.nome, cliente.email))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    
    def listar(self) -> List[Cliente]:
        lista = []
        sql = "SELECT * FROM clientes"
        
        try:
            conn = Conexao.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql)
            
            for row in cursor.fetchall():
                cliente = Cliente(row[0], row[1], row[2])
                lista.append(cliente)
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
        
        return lista
    
    def buscarPorId(self, id: int) -> Optional[Cliente]:
        sql = "SELECT * FROM clientes WHERE id = ?"
        cliente = None
        
        try:
            conn = Conexao.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            
            if row:
                cliente = Cliente(row[0], row[1], row[2])
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
        
        return cliente
    
    def atualizar(self, cliente: Cliente) -> None:
        sql = "UPDATE clientes SET nome = ?, email = ? WHERE id = ?"
        
        try:
            conn = Conexao.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql, (cliente.nome, cliente.email, cliente.id))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    
    def excluir(self, id: int) -> None:
        sql = "DELETE FROM clientes WHERE id = ?"
        
        try:
            conn = Conexao.getConnection()
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()