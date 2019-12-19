import datetime


class BirthDay:
    @staticmethod
    def get_birth_days():
        curr_date = datetime.datetime.now()
        message = []
        with open('dates.csv', 'r') as f:
            for s in f:
                arr = s.split(';')
                birth_date = arr[0][1:-1].split('.')
                print(birth_date)
                print(int(birth_date[0]), int(curr_date.day))
                print(int(birth_date[1]), int(curr_date.month))
                if int(birth_date[0]) == int(curr_date.day) and int(birth_date[1]) == int(curr_date.month):
                    message.append(arr[1])

        return f'На {curr_date.day}.{curr_date.month}.{curr_date.year}: {",".join(message) if message else "Сегодня никаких уведомлений."}'


if __name__ == '__main__':
    BirthDay.get_birth_days()