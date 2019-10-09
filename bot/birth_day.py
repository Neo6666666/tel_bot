import datetime


class BirthDay:
    @staticmethod
    def get_birth_days():
        curr_date = datetime.datetime.now()
        persons = {}
        with open('dates.csv', 'r') as f:
            for s in f:
                arr = s.split(',')
                birth_date = arr[-1].split(';')[0].split('.')
                if int(birth_date[0]) == int(curr_date.day) \
                        and int(birth_date[1]) == int(curr_date.month):
                    if len(birth_date) == 3:
                        persons[' '.join(arr[0:3])] = \
                            f'{int(curr_date.year) - int(birth_date[-1])} летие.'
                    else:
                        persons[' '.join(arr[0:3])] = '.'.join(birth_date)

        message = 'Сегодня никаких дней рождений.'
        if len(persons) != 0:
            message = f'На {curr_date.day}.{curr_date.month}.{curr_date.year} дни + \
                рождения празднуют:\n' + \
                      f'\n'.join([f'{key}: {value}' for key, value in persons.items()])

        return message
