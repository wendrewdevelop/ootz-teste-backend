from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from App.Kit.api.serializers import KitSerializer
from App.Kit.models import KitProduto


class KitViewset(ModelViewSet):
    serializer_class = KitSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'nome_kit')

    def get_queryset(self):
        #Definindo os paramêtros de busca
        '''
            O paramêtro poderia ser definido como uma lista, porém
            se não fosse preenchido o sistema apresentaria um erro.
            id = self.request.query_params['id']
        '''
        id = self.request.query_params.get('id', None)
        nome_kit = self.request.query_params.get('nome_kit', None)

        #instanciando a queryset
        queryset = KitProduto.objects.all()

        if id:#se o id existir
            queryset.filter(id__iexact = id)#busca id
        
        if nome_kit:#se o nome_kit existir
            queryset.filter(nome_kit = nome_kit)#busca nome_kit
            
        return queryset

        def list(self, request, *args, **kwargs):
            return super(KitViewset, self).list(request, *args, **kwargs)

        def create(self, request, *args, **kwargs):
            return super(KitViewset, self).create(request, *args, **kwargs)

        def destroy(self, request, *args, **kwargs):
            return super(KitViewset, self).destroy(request, *args, **kwargs)

        def retrieve(self, request, *args, **kwargs):
            return super(KitViewset, self).retrieve(request, *args, **kwargs)

        def update(self, request, *args, **kwargs):
            return super(KitViewset, self).update(request, *args, **kwargs)
            
        def partial_update(self, request, *args, **kwargs):
            return super(KitViewset, self).partial_update(request, *args, **kwargs)