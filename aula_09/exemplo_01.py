from loguru import logger

logger.add("meu_log.log", level = "CRITICAL")

def soma(x,y):
    try:
        soma = x + y
        logger.info(f"Você digitou valores corretos, {soma}")
        return soma
    except:
        logger.critical("Você tem que digitar valores corretos")
    
    #logger.info(x)
    #logger.info(y)
    #logger.info(x+y)
    #return x + y

soma(2,"2")

