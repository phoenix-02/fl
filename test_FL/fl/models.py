from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    role_choices = (
        (1, 'fl'),
        (2, 'freelancer'),
        (3, 'anon'),
        (4, 'admin'),
    )
    about=models.CharField(max_length=300, null=True)
    role = models.PositiveIntegerField(choices=role_choices, default=1)
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_custom_user(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)


class Project(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    freelancers = models.ManyToManyField(CustomUser,related_name="+")
    title = models.CharField(default='', max_length=50)
    description = models.CharField(default='', max_length=500)
    price = models.IntegerField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
