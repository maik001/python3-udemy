''' 
Desafio 2 - Duas pessoas terão dois trabalhos para apresentar em dois dias diferentes,
Um na terca-feira e outro na quinta-feira. Se os dois trabalhos derem certo,
a pessoa prometeu que vai no shopping comprar uma televisão de 50.
Se apenas um dos trabalhos der certo será uma de 32 polegadas.
Nos dois Cenários, a família vai no shopping tomar sorvete.
Agora se nenhum dos trabalhos derem certo, não haverá nada,
porém a família passa a ter mais saúde, que é a negação de tomar sorvete.
'''

trabalho_terca = True
trabalho_quinta = True

# Primeiro Cenário - Os dois trabalhos dão certo
tv_50 = trabalho_terca and trabalho_quinta

# Segundo Cenário - Somente um dos trabalhos dá certo
tv_32 = trabalho_terca != trabalho_quinta

# Quando qualquer um dos trabalhos dá certo
sorvete = trabalho_terca or trabalho_quinta

# Terceiro Cenário - Nenhum dos trabalhos dá certo
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudavel={}"
    .format(tv_50, tv_32, sorvete, mais_saudavel))
