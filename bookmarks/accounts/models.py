from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class Contact(models.Model):
    """
    A model representing relationship between
    two users.
    """
    user_from = models.ForeignKey('auth.User',
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


"""
When you need additional fields in a many-to-many relationship,
create a custom model with a ForeignKey for each side of the 
relationship. A a ManyToManyField in one of the related models
and indicate to Django that your intermediary model should be
used by including it in the through parameter.
"""
"""
If the User model was part of the application, we could add the
previous field to the model. However we can't alter the User class
directly because it belongs to the django.contrib.auth application.
We will therefore take a slightly different approach by adding this
field dynamically to the User model
"""
"""
Monkey patching like below is not recommended.
Symmetrical is set to False. When you define a ManyToManyField in the model
creating a relationship with itself, Django forces the relationship to be
symmetrical. In this case you are setting symmetrical to False to define
a non-symmetrical relationship(if I follow you, it doesn't mean that you
automatically follow me).

When you use an intermediary model for many-to-many relationships, some of
the related manager's methods are disabled, such as add(), create(), or
remove(). You need to create, or delete instances of the intermediary 
model instead.
"""

user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                                               through=Contact,
                                               related_name='followers',
                                               symmetrical=False))
