from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Question(models.Model):
    user_id = models.ForeignKey("account.user", verbose_name=_("user "), on_delete=models.CASCADE)
    content = models.TextField(_("content"))   
    created_at=models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question_id = models.ForeignKey("chatgpt.question", verbose_name=_("question"), on_delete=models.CASCADE)
    content = models.TextField(_("content"))   
    created_at=models.DateTimeField(auto_now_add=True)
