from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from App.Kit.models import KitProduto
from App.Produto.api.serializers import ProdutoSerializer


class KitSerializer(ModelSerializer):
    class Meta:
        model = KitProduto
        fields = '__all__'