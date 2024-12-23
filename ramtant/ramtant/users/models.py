from django.db import models
from django.contrib.auth.models import User, Group, Permission, AbstractUser

# создание класса пользователя
class Usr(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(Usr, on_delete=models.CASCADE)

    img = models.ImageField(default='default.png', upload_to='prf_pics')

    is_online = models.BooleanField(default=False)

    bio = models.TextField(default='пустое описание')
    
    medal1 = models.BooleanField(default=False)
    medal2 = models.BooleanField(default=False)
    medal3 = models.BooleanField(default=False)

    follows = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)

    def __str__(self):
        return self.user.username