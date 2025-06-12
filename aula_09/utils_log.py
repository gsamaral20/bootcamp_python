from loguru import logger
from sys import stderr
from functools import wraps

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO"
)

# Exemplo de uso do logger
logger.info("Este é um log de informação.")
logger.error("Este é um log de erro.")

from functools import wraps
import logging

logger = logging.getLogger(__name__)  # Define um logger nomeado com o nome do módulo

# Decorador para registrar logs de chamada e execução de funções
def log_decorator(func):
    @wraps(func)  # Preserva o nome e docstring da função original
    def wrapper(*args, **kwargs):
        # Loga o início da execução da função com seus argumentos
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)  # Executa a função original com os argumentos fornecidos
            # Loga o resultado retornado pela função
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result  # Retorna o resultado normalmente
        except Exception as e:
            # Em caso de erro, registra o traceback completo
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Repassa a exceção adiante, sem suprimir o erro
    return wrapper  # Retorna a função decorada
