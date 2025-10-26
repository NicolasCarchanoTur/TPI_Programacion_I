from typing import Optional

def validar_int(valor: str) -> Optional[int]:
    try:
        valor = valor.replace(',', '').strip()
        n = int(valor)
        if n < 0:
            return None
        return n
    except Exception:
        return None

def formato_pais_valido(nombre: str, continente: str) -> bool:
    return bool(nombre and continente)

def pedir_entero(prompt: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        entrada = input(prompt).strip()
        if entrada == '':
            print("Entrada vacía. Intente nuevamente.")
            continue
        try:
            n = int(entrada)
            if minimo is not None and n < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue
            if maximo is not None and n > maximo:
                print(f"El valor debe ser <= {maximo}.")
                continue
            return n
        except ValueError:
            print("Por favor ingrese un número entero válido.")

def pedir_texto(prompt: str) -> str:
    while True:
        t = input(prompt).strip()
        if t == '':
            print("Entrada vacía. Intente nuevamente.")
            continue
        return t
