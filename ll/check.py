from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username)
    print(user.password)
    print(user.id)