from ssl import ALERT_DESCRIPTION_NO_RENEGOTIATION


nome = input("digite_seu_nome.: ")
idade = int (input( "Digite sua idade.: "))
salario = float (input( "digite seu salario.: "))

print ( "Nome.: " ,nome, " - idade " ,idade, " - salario " ,salario ) 
# executar arquivo no terminal para preencher por aqui

print ( "nome.: %s - idade %i - salario R$ %5.2f " % (nome,idade,salario))
