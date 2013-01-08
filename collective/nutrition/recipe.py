from five import grok
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
#from collective.z3cform.chosen import AjaxChosenFieldWidget
from plone import api
from plone.memoize import view
from plone.dexterity.content import Item
from plone.directives import form, dexterity
from plone.app.textfield import RichText
from zope import schema
from zope import interface
import z3c.form.interfaces
import z3c.form.widget

from collective.nutrition.food import IFood, FoodSourceBinder


class IRecipeFood(form.Schema):
    amount = schema.Float(
        title=u"Amount in 100 grams",
        default=1.0,
    )

#    form.widget(food=AjaxChosenFieldWidget)
    food = schema.Choice(
        title=u"Food",
        source=FoodSourceBinder(),
    )


class IRecipe(form.Schema):
    # TODO: searchable
    title = schema.TextLine(
        title=u"Name",
    )

    description = schema.TextLine(
        title=u"Description",
        required=False,
    )

    text = RichText(
        title=u"Text",
        required=False,
    )

    form.widget(foods=DataGridFieldFactory)
    foods = schema.List(
        title=u"Foods",
        value_type=DictRow(schema=IRecipeFood),
    )


class Recipe(Item):
    pass


class View(grok.View):
    grok.context(IRecipe)
    grok.require('zope2.View')

    @view.memoize
    def get_objects(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        return [(catalog(UID=item['food'])[0].getObject(), item['amount']) for item in self.context.foods]

    def values(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        l = []
        for obj, amount in self.get_objects():
            l.append({
                'title': obj.Title,
                'amount': amount * 100,
                'protein': amount * obj.protein,
            })
        return l

    @view.memoize
    def total_proteins(self):
        return sum([obj.protein * amount for obj, amount in self.get_objects()])

    def total_grams(self):
        return sum([100 * amount for obj, amount in self.get_objects()])

    def total_calories(self):
        l = []
        for obj, amount in self.get_objects():
            cals = sum([obj.protein * amount * 4 + obj.carbohydrate_by_difference * amount * 4 + obj.total_lipid_fat * amount * 9 + obj.alcohol * amount * 7 for obj, amount in self.get_objects()])
            l.append(cals)

        return sum(l)
