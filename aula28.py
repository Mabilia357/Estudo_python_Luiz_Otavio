"""
Exercício
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou nao) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite agora a sua idade: ')
if nome and idade != '':
    print(f'Seu nome é: {nome} e sua idade é: {idade} anos')
    print(f'Seu nome invertido é: {nome[::-1]}')
else:
    print('Digite um nome e uma idade válida!')    
