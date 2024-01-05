from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название разделала")
    slug = models.CharField(max_length=127, unique=True, null=True)
    

    def __str__(self):
        return f"Название раздела: {self.name}"
    

    def get_absolute_url(self):
        return reverse("topic", kwargs={"topic_id":self.pk})
    

    # class Meta:
    #     verbose_name = "Задания"
    #     verbose_name_plural = "Задания"
    #     ordering = ["name"]


class EconomicIndex(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=127, unique=True, null=True)
    macro_topic = models.ForeignKey("Topic", on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Название экономического показателя: {self.name}"
    
    
    # def get_absolute_url(self):
    #     return reverse("", kwargs={"topic_id":self.pk})


class Table(models.Model):
    path = models.CharField(max_length=255, null=True)
    macro_economic_index = models.ForeignKey("EconomicIndex", on_delete=models.PROTECT)

    def __str__(self):
        return f"Название экономического показателя: {self.macro_economic_index.name}, название файла: {self.path}"
