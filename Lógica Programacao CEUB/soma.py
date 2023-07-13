#Contrua o programa contendo as funções main, soma, subtrai. O programa (funçao main) le dois valores inteiros, chama a funcao soma passando os dois valores lidos e depois chama a função subtrai passando os dois valores lidos. A função soma recebe dois valores inteiros, realiza a soma e retorna o resultado  do calculo. A função subtrai recebe dois valores inteiros, realiza a subtração deles e retorna o resultado do calculo. A função main recebe o valor retornado pelas funções soma e subtrai e gera a tela de saída com essas informações. 
def soma (a,b):
    return a + b
def subtrai (a,b):
    return a - b
#def recebe_inteiro ():
    #vl_inteiro = int(input("Digite um numero inteiro: "))
    #return vl_inteiro
def recebe_inteiro2 (m):
    vl_inteiro = int(input(m))
    return vl_inteiro
if __name__ == '__main__':
    num1 = recebe_inteiro2 ("Digite o primeiro valor: ")
    num2 = recebe_inteiro2 ("Digite o segundo valor: ")
    print("A soma é: ", soma(num1, num2))
    print("A subtração é: ", subtrai(num1, num2))