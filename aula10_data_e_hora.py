from datetime import date, time, timedelta, datetime

def trabalhando_com_data():
    # trazer a data atual da função date
    data_atual = date.today()
    print(data_atual)


    # formatando a data para o padrão brasileiro
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%d-%m-%y'))
    print(data_atual.strftime('%d %m %y'))
    print(data_atual.strftime('%d/%m/%Y'))

    # dia da semana(%A)
    print(data_atual.strftime('%A'))
    # dia do mês (%B)
    print(data_atual.strftime('%B'))


    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)

    print(type(data_atual))
    print(type(data_atual_str))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    #print(horario)
    print(horario.strftime('%H:%M:%S'))

    horario_str = horario.strftime('%H:%M:%S')
    
    print(type(horario))
    print(type(horario_str))
    
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    
    # somente o minuto
    print(data_atual.minute)

    # somente a hora
    print(data_atual.hour)

    # somente dia
    print(data_atual.day)

    # somente mês
    print(data_atual.month)

    # somente ano
    print(data_atual.year)

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))


    data_string = '01/01/2019 12:20:22'

    # prestar atenção!!! foi usado str_P_time. Se usar strftime vai dar erro
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)

    # subtração de data: data_convertida MENOS um ano
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_data()
    #trabalhando_com_time()
    trabalhando_com_datetime()