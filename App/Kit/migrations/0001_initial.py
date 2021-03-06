# Generated by Django 3.1.1 on 2020-09-07 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitProduto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_kit', models.CharField(max_length=150)),
                ('sku_kit', models.CharField(max_length=100)),
                ('produtos_kit', models.ManyToManyField(to='Produto.Produto')),
            ],
            options={
                'db_table': 'kits',
            },
        ),
    ]
