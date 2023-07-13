def converte(v1, v2):
    return (v1 * 60) + v2
def le_valor (x):
    valor = float(input(x))
    return valor
if __name__=='__main__':
    hora = int(input("Digite as horas: "))
    minuto = int(input("Digite os minutos: "))
    conv = converte(hora, minuto)
    hora2 = int(input("Digite as horas: "))
    minuto2 = int(input("Digite as horas: "))
    conv2 = converte(hora2, minuto2)
    print(f'A diferença é: {conv - conv2} minutos')