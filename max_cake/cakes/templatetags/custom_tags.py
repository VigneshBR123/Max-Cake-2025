from django import template

register = template.Library()

@register.simple_tag
def already_exists_in_wishlist(request, cake_uuid):

    if request.user.is_authenticated and request.user.role == "user":

        return request.user.wishlist.cake.filter(uuid = cake_uuid).exists()

    return False


@register.simple_tag
def cart_list(request):

    if request.user.is_authenticated and request.user.role == "user":

        cakes = request.user.cart.cakes.all()

        return cakes