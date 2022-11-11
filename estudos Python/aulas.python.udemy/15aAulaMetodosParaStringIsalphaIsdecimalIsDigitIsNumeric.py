nome = input ( " digite seu nome.: " )
print ( " capitalize ( primeiro caracter e maiusculo = " ,nome.capitalize ( ) )
print ( " center = centraliza com espacos em branco " ,nome.center (  30  ) )
print ( " quantas letras i tem no nome: " ,nome.count ( "i" ) )
print ( " retorna True se o nome terminar com ki" ,nome.endswith ( "ki" ) )

# inicio 14a aula

print ( " find retorna posicao de String " ,nome.find ( "a" ) )
print ( " find retorna posicao de String " ,nome.find ( "a" ,1 ) )
print ( " find retorna posicao de String " ,nome.find ( "a" ,1,4))
print ( " Index retorna posicao da primeira ocorrencia " ,nome.index ( "a" ))
print ( " Index retorna posicao da primeira ocorrencia " ,nome.index ("a",0,7 )) 
print ( " Index retorna posicao da primeira ocorrencia " ,nome.index ( "a" ) )
# o index retorna posicao da primeira ocorrencia

# 15a aula 16a aula e 17a aula 18a aula

print ( " isalpha = ",nome.isalpha () )
print ( " isdecimal = ",nome.isdecimal () )
print ( " isdigit = ",nome.isdigit () )
print ( " isnumeric = ",nome.isnumeric () ) 
print ( " lower = ", nome.lower () )
print ( " islower = ", nome.islower () )
print ( " isspace = ", nome.isspace () ) 

dados = ( 'adriano','geovana', 'maia', 'dent' )
print ( dados )
print ("\n" . join ( dados ) )
print ( " ---- ". join ( dados ) )


palavra = " adriano "
print ( "ljust = ", palavra.ljust (10) , "casa" )
print ( "rjust = ", palavra.rjust (10) , "casa" )
print ( "partition, divide a string em uma tupla com 3 elementos: " , "adrianolachovskijr". partition ( "lachovski" ) )
print ( "partition, divide a string em uma tupla com 3 elementos: " , "xyz". partition ( "y" ) )
 # partition da para usar com rpartition ou lpartition para ter feito da esquerda ou direita

palavra = " adriano lachovski junior "
print ( palavra.startswith ( "adriano" ) )
#strip elimina espacos em branco e a esquerda e direita com l ou r
#startswith = retorna verdadeiro se a string inicia com uma substring
