from django.db import models

import uuid

from django.db.models import Sum

class BaseClass(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True

# class CakesChoices(models.TextChoices):

#     BIRTHDAY_CAKES = 'Birthday Cakes', 'Birthday Cakes'
#     WEDDING_CAKES = 'Wedding Cakes', 'Wedding Cakes'
#     PLUM_CAKES = 'Plum Cakes', 'Plum Cakes'
#     CUP_CAKES = 'Cup Cakes', 'Cup Cakes'

class Categorey(BaseClass):

    name = models.CharField(max_length=50)

    class Meta:

        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

# class FlavoursChoices(models.TextChoices):

#     VANILLA = 'Vanilla', 'Vanilla'
#     CHOCOLATE = 'Chocolate', 'Chocolate'
#     RED_VELVET = 'Red Velvet', 'Red Velvet'
#     STRAWBERRY = 'Strawberry', 'Strawberry'
#     LEMON = 'Lemon', 'Lemon'
#     CARROT = 'Carrot', 'Carrot'
#     BLACK_FOREST = 'Black Forest', 'Black Forest'
#     COCONUT = 'Coconut', 'Coconut'
#     TIRAMISU = 'Tiramisu', 'Tiramisu'
#     MOCHA = 'Mocha','Mocha'
#     OTHER = 'Other', 'Other'

class Flavours(BaseClass):

    name = models.CharField(max_length=50)

    class Meta:

        verbose_name = 'Flavours'
        verbose_name_plural = 'Flavours'

    def __str__(self):
        return f'{self.name}'

# class ShapeChoices(models.TextChoices):

#     ROUND = 'Round', 'Round'
#     SQUARE = 'Square', 'Square'
#     HEART = 'Heart', 'Heart'
#     RECTANGLE = 'Rectangle', 'Rectangle'
#     HEXAGON = 'Hexagon', 'Hexagon'
#     OVAL = 'Oval', 'Oval'
#     NUMBER = 'Number', 'Number'
#     TIERED = 'Tiered', 'Tiered'
#     DOLL_SHAPE = 'Doll Shape', 'Doll Shape'
#     PHOTO_CAKE = 'Photo Cake', 'Photo Cake'
#     OTHER = 'Other', 'Other'

class Shapes(BaseClass):

    name = models.CharField(max_length=50)

    class Meta:

        verbose_name = 'Shapes'
        verbose_name_plural = 'Shapes'

    def __str__(self):
        return f'{self.name}'

# class WeightChoices(models.TextChoices):

#     HALF_KG = '0.5 kg', '0.5 kg'
#     ONE_KG = '1 kg', '1 kg'
#     TWO_KG = '2 kg', '2 kg'
#     THREE_KG = '3 kg', '3 kg'
#     FIVE_KG = '5 kg', '5 kg'

class Weights(BaseClass):

    value = models.CharField(max_length=50)

    class Meta:

        verbose_name = 'Weights'
        verbose_name_plural = 'Weights'

    def __str__(self):
        return f'{self.value}'

class EggStatusChoices(models.TextChoices):

    EGG = 'Egg','Egg'
    EGGLESS = 'Eggless','Eggless'

# class ToppingsChoices(models.TextChoices):

#     CHOCO_CHIPS = 'Choco chips', 'Choco Chips'
#     SPRINKLES = 'Sprinkles', 'Sprinkles'
#     FRESH_FRUIT = 'Fresh fruit', 'Fresh Fruit'
#     NUTS = 'Nuts', 'Nuts'
#     WHIPPED_CREAM = 'Whipped cream', 'Whipped Cream'
#     CHOCOLATE_DRIZZLE = 'Chocolate drizzle', 'Chocolate Drizzle'
#     CARAMEL_DRIZZLE = 'Caramel drizzle', 'Caramel Drizzle'

class Toppings(BaseClass):

    name = models.CharField(max_length=50)

    class Meta:

        verbose_name = 'Toppings'
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return f'{self.name}'

class Cakes(BaseClass):

    name = models.CharField(max_length=50)
    desciption = models.TextField()
    photo = models.ImageField(upload_to='cakes/')

    # categorey = models.CharField(max_length=30, choices=CakesChoices.choices)
    # flavour = models.CharField(max_length=20, choices=FlavoursChoices.choices)
    # shape = models.CharField(max_length=10, choices=ShapeChoices.choices)
    # weight = models.CharField(max_length=10, choices=WeightChoices.choices)
    # egg_sts = models.CharField(max_length=15, choices=EggStatusChoices.choices)
    # toppings = models.CharField(max_length=25, choices=ToppingsChoices.choices)

    categorey = models.ForeignKey('Categorey', on_delete=models.CASCADE)
    flavour = models.ForeignKey('Flavours', on_delete=models.CASCADE)
    shape = models.ForeignKey('Shapes', on_delete=models.CASCADE)
    weight = models.ForeignKey('Weights', on_delete=models.CASCADE)
    egg_sts = models.CharField(max_length=15, choices=EggStatusChoices.choices)
    toppings = models.ForeignKey('Toppings', on_delete=models.CASCADE)

    is_available = models.BooleanField()
    price = models.FloatField()

    class Meta:

        verbose_name = 'Cakes'
        verbose_name_plural = 'Cakes'

    def __str__(self):
        # return f'{self.name}-{self.categorey}-{self.weight}'
        return f'{self.name}-{self.categorey.name}-{self.weight.value}'
    
class WishList(BaseClass):
    
    user = models.OneToOneField('authentication.Profile', on_delete=models.CASCADE)

    cakes = models.ManyToManyField('Cakes', blank=True)

    class Meta:

        verbose_name = 'WishList'
        verbose_name_plural = 'WishList'

    def __str__(self):
        return f'{self.user.first_name}-{self.user.last_name}-WishList'

class Cart(BaseClass):
    
    user = models.OneToOneField('authentication.Profile', on_delete=models.CASCADE)

    cakes = models.ManyToManyField('Cakes', blank=True)

    def get_total(self):
        
        total = self.cakes.aggregate(price_total = Sum("price"))['price_total']

        return total if total else 0

    class Meta:

        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

    def __str__(self):
        return f'{self.user.first_name}-{self.user.last_name}-Cart'