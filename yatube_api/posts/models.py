from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()


class Group(models.Model):
    """Модель групп публикаций."""
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы'
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name='Слаг'
    )
    description = models.TextField(
        verbose_name='Описание группы'
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    """Модель публикаций пользователей."""
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Текст нового поста'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
        db_index=True
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост',
        db_index=True
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.text[:15]

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'post_id': self.pk})


class Comment(models.Model):
    """Модель комментариев пользователей."""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        db_index=True
    )
    text = models.TextField(
        verbose_name='Текст комментария'
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.text[:15]


class Follow(models.Model):
    """Модель подписок пользователей."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
        db_index=True
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        db_index=True
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='user_following_unique'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='user_folowing_different'),
        )
        index_together = ('user', 'following')
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self) -> str:
        return (
            f'relation: {self.user.get_username()} '
            f'- {self.following.get_username()}'
        )
