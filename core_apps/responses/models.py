from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.articles.models import Article
from core_apps.common.models import TimeStampModel

User = get_user_model()


class Responses(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="responses"
    )
    parent_responses = (
        models.ForeignKey(
            "self",
            on_delete=models.CASCADE,
            related_name="replies",
            null=True,
            blank=True,
        ),
    )

    content = models.TextField(verbose_name=_("response content"))

    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.first_name} commented on {self.article.title}"
