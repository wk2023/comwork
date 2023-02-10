'''
def describe_pet(animal_type,pet_name):
    print( '\n你拥有的动物 ' + animal_type + '.')
    print('我有一只' + animal_type + '他的名字是'+ pet_name)
describe_pet('小狗','豆豆')
describe_pet('xiaomao','米米')
describe_pet('花花','老虎')
describe_pet(pet_name = '花花',animal_type = '老虎')

def describe_pet(pet_name,animal_type = '小狗'):
    print('\n我有一只' + animal_type + '.')
    print('我的' +animal_type + '它的名字是' + pet_name + '.')
describe_pet(pet_name = '明明')
describe_pet('爱怜','仓鼠')
describe_pet(pet_name = '爱怜',animal_type = '仓鼠')
describe_pet(animal_type = '仓鼠',pet_name = '爱怜')


def get_formatted_name(first_name,last_name):
    full_name = first_name + ' '+ last_name
    return full_name
musician = get_formatted_name('jimi','hendrix')
print (musician)

#结合使用函数和while循环
def get_formatted_name(frist_name,last_name):
    full_name = frist_name + '  ' + last_name
    return full_name.title()
while True :
    print('\n please tell me your name:')
    print('\n enter "q" at any time tu quit')
    f_name = input('first name:')
    if f_name == 'q':
        break
    l_name = input('last name:')
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print('\nhello, ' + formatted_name + '!')


# 传递列表
def greet_users(names):
    for name in names:
        msg = 'hello ' + name.title() + ' !'
        print(msg)
users_names = ['hannah','ty','margot']
greet_users(users_names)
 '''
# 函数中修改类别

