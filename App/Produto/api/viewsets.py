from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import filters
from App.Produto.models import Produto
from App.Produto.api.serializers import ProdutoSerializer


class ProdutoViewset(ModelViewSet):
    serializer_class = ProdutoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'nome')

    def get_queryset(self):
        #Definindo os paramêtros de busca
        '''
            O paramêtro poderia ser definido como uma lista, porém
            se não fosse preenchido o sistema apresentaria um erro.
            id = self.request.query_params['id']
        '''
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)

        #instanciando a queryset
        queryset = Produto.objects.all()

        if id:#se o id existir
            queryset.filter(id__iexact = id)#busca id
        
        if nome:#se o nome existir
            queryset.filter(nome = nome)#busca nome
            
        return queryset

        def list(self, request, *args, **kwargs):
            return super(ProdutoViewset, self).list(request, *args, **kwargs)

        def create(self, request, *args, **kwargs):
            return super(ProdutoViewset, self).create(request, *args, **kwargs)

        def destroy(self, request, *args, **kwargs):
            return super(ProdutoViewset, self).destroy(request, *args, **kwargs)

        def retrieve(self, request, *args, **kwargs):
            return super(ProdutoViewset, self).retrieve(request, *args, **kwargs)

        def update(self, request, *args, **kwargs):
            return super(ProdutoViewset, self).update(request, *args, **kwargs)
            
        def partial_update(self, request, *args, **kwargs):
            return super(ProdutoViewset, self).partial_update(request, *args, **kwargs)