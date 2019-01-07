from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Post(models.Model):
    """Model for user publications"""
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title')
    )
    text = models.TextField(
        verbose_name=_('Title')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )

    def __str__(self):
        """Model 'hint'"""
        return self.title


LIKE_TYPE_CHOICES = (
    ('positive', _('Positive')),
    ('negative', _('Negative'))
)


class Like(models.Model):
    """Model for Post likes.
    Post may have many likes and dislikes from one user
    """
    author = models.ForeignKey(
        User,
        related_name='likes',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )
    value = models.CharField(
        max_length=8,
        verbose_name=_('Value'),
        default=LIKE_TYPE_CHOICES[0][0],
        choices=LIKE_TYPE_CHOICES
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    def __str__(self):
        """Model 'hint'"""
        return _('{post} from {user}').format(
            post=self.post.title,
            user=self.user.username
        )
