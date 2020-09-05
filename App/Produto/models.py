from django.db import models

# Create your models here.
class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        max_length=150
    )
    sku = models.CharField(
        max_length=100
    )
    custo = models.FloatField()
    preco = models.FloatField()
    estoque = models.IntegerField()

    class Meta:
        db_table = 'produtos'

    def __str__(self):
        return self.nome