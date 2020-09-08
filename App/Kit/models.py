from django.db import models
from App.Produto.models import Produto


class KitProduto(models.Model):
    id = models.AutoField(primary_key=True)
    nome_kit = models.CharField(max_length=150)
    sku_kit = models.CharField(max_length=100)
    produtos_kit = models.ManyToManyField(
        Produto,
        related_name='produtos_kit'
    )

    class Meta:
        db_table = 'kits'

    def __str__(self):
        return self.nome_kit