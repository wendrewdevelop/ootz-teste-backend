from rest_framework.serializers import ModelSerializer
from App.Produto.models import Produto


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'