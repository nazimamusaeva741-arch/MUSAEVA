from django.db import models



class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = 'created',"Созданно"
        IN_PROGRES = "in_progres", "В работе"
        COMPLETED = "completed", "Завершено"

    title = models.CharField(
        max_length=255,
        verbose_name="Название задачи",
        help_text="Краткое название задачи(до 255 символов)",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание",
        help_text="Времяб когда задача"
    )
def __str__(self):
    return f"{self.title}--->{self.status}"



class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title