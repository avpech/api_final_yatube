# Generated by Django 3.2.16 on 2023-03-04 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20230304_1131'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_author_unique',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_author_different',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AlterIndexTogether(
            name='follow',
            index_together={('user', 'following')},
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='user_following_unique'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', django.db.models.expressions.F('following')), _negated=True), name='user_folowing_different'),
        ),
    ]
