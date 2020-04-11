from models import Pessoas

def insere_pessoas():
   pessoa = Pessoas(nome='Pavini', idade=36)
   print(pessoa)
   pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Carla').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Carla') .first()
    pessoa.nome = 35
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

if __name__ == '__main__':
    insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()




