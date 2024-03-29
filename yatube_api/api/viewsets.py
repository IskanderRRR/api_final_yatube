from rest_framework import mixins, viewsets


class CreateGetViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    pass
