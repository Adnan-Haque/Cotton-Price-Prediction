# from django.db import models

# # Create your models here.
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class MyUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     state = models.CharField(max_length=100)

# @receiver(post_save, sender=User)
# def create_user_myuser(sender, instance, created, **kwargs):
#     if created:
#         MyUser.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_myuser(sender, instance, **kwargs):
#     instance.myuser.save()


from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager

class User_manager(BaseUserManager):
    def create_user(self, username, email, state, password):
        email = self.normalize_email(email)
        user = self.model(username=username, state=state, email=email)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, state, password):
        user = self.create_user(username=username, email=email, state=state, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user



class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32)
    state = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["email", "state"]
    USERNAME_FIELD = "username"
    objects = User_manager()

    def __str__(self):
        return self.username