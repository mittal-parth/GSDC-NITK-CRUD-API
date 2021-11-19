from django.urls import path

# provides a GUI to work with GraphQL
from graphene_django.views import GraphQLView
from base.schema import schema

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]
