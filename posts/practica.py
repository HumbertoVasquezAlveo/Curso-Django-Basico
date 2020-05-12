from datetime import date

users = [
    {
        'email': 'yinny@gmail.com',
        'first_name': 'Yinny',
        'last_name' : 'Muñoz',
        'password'  : '123ewqer'
    },
      {
        'email': 'vayolet@hotmail.com',
        'first_name': 'Vayolet',
        'last_name' : 'Markes',
        'password'  : '123asd'
    },
      {
        'email': 'luisa@outlook.com',
        'first_name': 'Luisa',
        'last_name' : 'Perez',
        'password'  : '12wwqed',
        'is_admin'  :  True
    }
]


from posts.models import User
for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)
