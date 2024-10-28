from rest_framework import serializers

from core.models import (
    Recipe,
    # Tag,
    # Ingredient,
)

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    # tags = TagSerializer(many=True, required=False)
    # ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']
        
class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']