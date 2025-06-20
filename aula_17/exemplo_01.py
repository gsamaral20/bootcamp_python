from sqlalchemy import create_engine

# Criar uma engine de conexão com o banco SQLite 'meubanco.db'
# echo=True mostra no console os comandos SQL executados (útil para debug)
engine = create_engine('sqlite:///meubanco.db', echo=True)

# Exemplo de URI para conexão com banco PostgreSQL (não usada aqui)
# URI = "postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase"
# Formato: dialect+driver://username:password@host:port/database

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Criar uma classe base para definição dos modelos (tabelas)
Base = declarative_base()

# Definição da tabela 'usuarios' como classe Python
class Usuario(Base):
    __tablename__ = 'usuarios'  # nome da tabela no banco

    # Definição das colunas da tabela
    id = Column(Integer, primary_key=True)  # chave primária auto incremental
    nome = Column(String)                   # coluna para nome do usuário
    idade = Column(Integer)                 # coluna para idade do usuário

# Criar as tabelas no banco, de acordo com os modelos definidos acima
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

# Criar uma fábrica de sessões vinculada à engine do banco
Session = sessionmaker(bind=engine)

# Criar uma sessão (conexão temporária com o banco para operações)
session = Session()

# Exemplo de inserção (comentado)
# novo_usuario = Usuario(nome='João', idade=28)
# session.add(novo_usuario)  # adiciona o objeto na sessão (pendente)
# session.commit()           # confirma e salva no banco

# Consulta no banco: pegar o primeiro usuário com nome 'João'
usuario = session.query(Usuario).filter_by(nome='João').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")

# Exemplo de inserção com tratamento de erros (comentado)
# try:
#     novo_usuario = Usuario(nome='Ana', idade=25)
#     session.add(novo_usuario)
#     session.commit()
# except:
#     session.rollback()  # desfaz alterações se der erro
# finally:
#     session.close()     # fecha a sessão sempre

# Forma mais simples e segura de usar a sessão com 'with'
with Session() as session:
    novo_usuario = Usuario(nome="Gabriel", idade=27)  # criar objeto usuário
    session.add(novo_usuario)                         # adicionar na sessão
    session.commit()                                  # salvar no banco

print("Conexão com SQLite estabelecida.")
