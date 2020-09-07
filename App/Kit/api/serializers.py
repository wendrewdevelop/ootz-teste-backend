from rest_framework.serializers import ModelSerializer
from App.Kit.models import KitProduto


class KitSerializer(ModelSerializer):
    class Meta:
        model = KitProduto
        fields = '__all__'