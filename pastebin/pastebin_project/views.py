from django.shortcuts import render


def question_view(request, i):
    paste_title = 'questao_%s' % i
    ctx = {
        'number': i,
        'text': questions[i]['text'],
        'title': questions[i]['title'],
        'paste_title': paste_title,
    }
    try:
        from pastebin.models import Paste
        paste = Paste.objects.get(title=paste_title)
        ctx['paste_data'] = paste.title
    except:
        ctx['paste_data'] = ('Seu model deve se chamar Paste e você deve fazer '
                             'um paste com o título %r.' % paste_title)
    return render(request, 'static.jinja2', ctx)


questions = {
    3: {
        'title': 'CSS',
        'text': '''
(a) Discuta o que significa a filosofia de desenvolvimento "Mobile First".
Discuta os aspectos técnicos com relação às implicações no HTML, CSS e
Javascript.

R: Significa fazer o design do site primeiramente para telas de celulares, e depois ir adicionando regras e códigos que adaptem o design da aplicação para telas maiores.

(b) Nosso site possui um footer responsivo. Ele é mobile first? Justifique.

R: Não é, pois primeiro foi feito o CSS pensando em telas grandes e depois foi adicionado a regra "@media only screen and (max-width: 500px)" que adapta o design para telas pequenas. Para corrigir isso deveria-se ter feito o contrário, usando "@media only screen and (min-width: 500px)" para criar o comportamento diferenciado em telas grandes (que exibiria o footer).

Caso não seja, explique como consertaríamos o problema.
''',
    },

    4: {
        'title': 'Problema N + 1',
        'text': '''
(a) O que é o problema N + 1 que aparece comumente em ORMs? Todos os ORMs estão
necessariamente sujeitos a este problema ou existem meios de contorná-los?



(b) Nosso app não está vulnerável ao problema porque não utiliza de nenhuma
chave estrangeira. Suponha que o modelo de Paste possua uma referência para
User. Como o problema apareceria e como poderíamos contorná-lo?



''',
    },


    5: {
        'title': 'Converta de Python para Javascript',
        'text': '''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

people = [Person('Joao', 21), Person('Maria', 20), Person('Zé', 8)]
adults = [x for x in people if x.is_adult()]
mean_age = sum(x.age for x in adults) / len(adults)


R:

function
''',
    },
}
