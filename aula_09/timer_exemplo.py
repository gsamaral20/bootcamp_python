import time
from loguru import logger
from functools import wraps

# Decorador para medir e registrar o tempo de execução de uma função
def time_measure_decorator(func):
    @wraps(func)  # Mantém o nome e docstring da função original
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Marca o tempo antes da execução
        result = func(*args, **kwargs)  # Executa a função original
        end_time = time.time()  # Marca o tempo após a execução
        
        # Calcula e registra o tempo total de execução no log
        logger.info(f"Função '{func.__name__}' executada em {end_time - start_time:.4f} segundos")
        
        return result  # Retorna o resultado original da função
    return wrapper  # Retorna a função decorada
