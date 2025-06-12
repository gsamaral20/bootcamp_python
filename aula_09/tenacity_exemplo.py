from tenacity import retry, stop_after_attempt, wait_fixed

# Aplica o decorador de retry:
# - Tenta no máximo 3 vezes
# - Espera 2 segundos entre cada tentativa
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_user_input():
    user_input = input("Digite 'ok' para continuar: ")
    
    # Verifica se o input é 'ok' (ignora maiúsculas/minúsculas)
    if user_input.lower() != 'ok':
        print("Input incorreto. Por favor, tente novamente.")
        raise ValueError("Input incorreto")  # Gatilho para o retry
    else:
        print("Input correto. Continuando...")

# Chama a função com tratamento de exceção final
try:
    get_user_input()
except Exception as e:
    print(f"Finalmente falhou após várias tentativas: {e}")
