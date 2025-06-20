# Importações necessárias da SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

# Criação da base para os modelos ORM
Base = declarative_base()

# Definição da tabela 'fornecedores'
class Fornecedores(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)                      # Chave primária
    nome = Column(String(50), nullable=False)                   # Nome do fornecedor (obrigatório)
    telefone = Column(String(20))                               # Telefone do fornecedor
    email = Column(String(50))                                  # Email do fornecedor
    endereco = Column(String(100))                              # Endereço completo

# Definição da tabela 'produtos'
class Produtos(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)                      # Chave primária
    nome = Column(String(50), nullable=False)                   # Nome do produto (obrigatório)
    descricao = Column(String(200))                             # Descrição do produto
    preco = Column(Integer)                                     # Preço do produto
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))  # Chave estrangeira para fornecedores

    # Estabelece o relacionamento com a tabela 'fornecedores'
    fornecedor = relationship("Fornecedores")

# Criação da engine de conexão com o banco de dados SQLite
engine = create_engine('sqlite:///desafio.db')  # echo=True habilita logs da SQL gerada

# Criação física das tabelas no banco de dados
Base.metadata.create_all(engine)

# Criação da sessão de comunicação com o banco
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de dados na tabela de fornecedores
try:
    with Session() as session:  # Uso do gerenciador de contexto para garantir fechamento automático
        fornecedores = [
            Fornecedores(nome="Fornecedor A", telefone="12345678", email="contato@a.com", endereco="Endereço A"),
            Fornecedores(nome="Fornecedor B", telefone="87654321", email="contato@b.com", endereco="Endereço B"),
            Fornecedores(nome="Fornecedor C", telefone="12348765", email="contato@c.com", endereco="Endereço C"),
            Fornecedores(nome="Fornecedor D", telefone="56781234", email="contato@d.com", endereco="Endereço D"),
            Fornecedores(nome="Fornecedor E", telefone="43217865", email="contato@e.com", endereco="Endereço E")
        ]
        session.add_all(fornecedores)  # Adiciona todos os objetos na sessão
        session.commit()               # Confirma a transação no banco
except SQLAlchemyError as e:          # Captura e exibe erros de inserção
    print(f"Erro ao inserir fornecedores: {e}")

# Inserção de dados na tabela de produtos
try:
    with Session() as session:  # Nova sessão para inserção de produtos
        produtos = [
            Produtos(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
            Produtos(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
            Produtos(nome="Produto 3", descricao="Descrição do Produto 3", preco=300, fornecedor_id=3),
            Produtos(nome="Produto 4", descricao="Descrição do Produto 4", preco=400, fornecedor_id=4),
            Produtos(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5)
        ]
        session.add_all(produtos)  # Adiciona todos os produtos
        session.commit()           # Confirma no banco
except SQLAlchemyError as e:
    print(f"Erro ao inserir produtos: {e}")

# Consulta agregada: soma dos preços dos produtos por fornecedor
resultado = session.query(
    Fornecedores.nome,
    func.sum(Produtos.preco).label('total_preco')  # Soma do preço por fornecedor
).join(
    Produtos, Fornecedores.id == Produtos.fornecedor_id  # Faz o join entre as tabelas
).group_by(
    Fornecedores.nome  # Agrupa pelo nome do fornecedor
).all()  # Executa a consulta e retorna os resultados

# Exibe o resultado da consulta
for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")
