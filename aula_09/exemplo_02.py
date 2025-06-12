from utils_log import log_decorator

@log_decorator

def soma(x,y):
    soma = x + y
    return soma
    
    #logger.info(x)
    #logger.info(y)
    #logger.info(x+y)
    #return x + y

soma(2,"2")