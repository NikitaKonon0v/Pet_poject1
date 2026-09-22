def tasck():
    spisok = []
    print("Напиши свои задачи:")
    while True:
        task = input()
        if task.lower() in ('всё', 'все', 'конец'):
            break
        spisok.append(task)
    return spisok

def dell(sp, stroka):
    if stroka in sp:
        ind = sp.index(stroka)
        sp.pop(ind)
        if not sp:
            sp.append('пусто')
            return sp
        return sp
    return False

def ad(sp, stroka):
    if stroka not in sp:
        sp.append(stroka)
        return sp
    return False



a = input('У тебя есть задачи на сегодня?')
flag = False
while True:
    if a == 'да':
        if not flag:
            sp = tasck()
            print('Вот твои задачи на сегодня:')
            for i in sp:
                print(i)
            flag = True
        shag1 = input()
        if shag1 == 'сделал':
            c = dell(sp, input())
            if c:
                print('Задача успешно удалена, вот что осталось:')
                for i in sp:
                    print(i)
            else:
                print('Задачи не было!')
        elif shag1 == 'на сегодня всё':
            break
        elif shag1 == 'ещё':
            d = ad(sp, input())
            if d:
                print('Задача успешно добавлена, вот весь список:')
                for i in sp:
                    print(i)
            else:
                print('Задача уже есть!')
    else:
        a = input('А сейчас?')