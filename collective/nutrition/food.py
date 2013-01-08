import os

from five import grok
from lxml import etree
from zope import schema
from zope import interface
from plone import api
from plone.dexterity.content import Item
from plone.directives import form, dexterity
from plone.app.textfield import RichText
from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.utils import getToolByName
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from z3c.formwidget.query.interfaces import IQuerySource


class IFood(form.Schema):
    #<title>BUTTER,WITH SALT</title>
    title = schema.TextLine(
        title=u"Name",
    )

    ndb_no = schema.TextLine(
        title=u"NDB number",
        required=False,
    )

    #<ndb_no>01001</ndb_no>
    description = schema.TextLine(
        title=u"Description",
        required=False,
    )

    # TODO: <gmwt_desc1>1 cup</gmwt_desc1>
    #<gmwt_1>227</gmwt_1>
    gmwt_1 = schema.Float(
        title=u"1 cup",
        required=False,
    )

    #<gmwt_2>14.2</gmwt_2>
    # TODO: <gmwt_desc2>1 tbsp</gmwt_desc2>
    gmwt_2 = schema.Float(
        title=u"1 tbsp",
        required=False,
    )

    alcohol = schema.Float(
        title=u"Alcohol",
        required=False,
        default=0.0,
    )

    potassium = schema.Float(
        title=u"Potassium",
        required=False,
    )

    #<alpha_carot>0</alpha_carot>
    alpha_carot = schema.Float(
        title=u"Alpha carot",
        required=False,
    )

    #<ash>2.11</ash>
    ash = schema.Float(
        title=u"Ash",
        required=False,
    )

    #<beta-carotene>158</beta-carotene>
    beta_carotene = schema.Float(
        title=u"Beta Carotene",
        required=False,
    )

    #<beta-cryptoxanthin >0</beta-cryptoxanthin >
    beta_cryptoxanthin = schema.Float(
        title=u"Beta Cryptoxanthin",
        required=False,
    )

    #<calcium>24</calcium>
    calcium = schema.Float(
        title=u"Calcium",
        required=False,
    )

    #<carbohydrate_by_difference>0.06</carbohydrate_by_difference>
    carbohydrate_by_difference = schema.Float(
        title=u"Carbohydrate by difference",
        required=False,
    )

    #<cholesterol >215</cholesterol >
    cholesterol = schema.Float(
        title=u"Cholesterol",
        required=False,
    )

    #<choline_total>18.8</choline_total>
    choline_total = schema.Float(
        title=u"Choline total",
        required=False,
    )

    #<copper>0</copper>
    copper = schema.Float(
        title=u"Copper",
        required=False,
    )

    #<energy>717</energy>
    energy = schema.Float(
        title=u"Energy",
        required=False,
    )

    #<folate_dietary_folate_equivalents>3</folate_dietary_folate_equivalents>
    folate_dietary_folate_equivalents = schema.Float(
        title=u"Folate dietary folate equivalents",
        required=False,
    )

    #<folate_total>3</folate_total>
    folate_total = schema.Float(
        title=u"Folate total",
        required=False,
    )

    #<folic_acid>0</folic_acid>
    folic_acid = schema.Float(
        title=u"Folic acid",
        required=False,
    )

    #<food_folate>3</food_folate>
    food_folate = schema.Float(
        title=u"Food folate",
        required=False,
    )

    #<iron>0.02</iron>
    iron = schema.Float(
        title=u"Iron",
        required=False,
    )

    #<lutein+zeazanthin>0</lutein+zeazanthin>
    lutein_zeazanthin = schema.Float(
        title=u"Lutein Zeazanthin",
        required=False,
    )

    #<lycopene>0</lycopene>
    lycopene = schema.Float(
        title=u"Lycopene",
        required=False,
    )

    #<magnesium>2</magnesium>
    magnesium = schema.Float(
        title=u"Magnesium",
        required=False,
    )

    #<manganese>0</manganese>
    manganese = schema.Float(
        title=u"Manganese",
        required=False,
    )

    #<Monounsaturated_fatty_acids >21.021</Monounsaturated_fatty_acids >
    monounsaturated_fatty_acids = schema.Float(
        title=u"Monounsaturated fatty acids",
        required=False,
    )

    #<niacin>0.042</niacin>
    niacin = schema.Float(
        title=u"Niacin",
        required=False,
    )

    #<Pantothenic_acid >0.11</Pantothenic_acid >
    pantothenic_acid = schema.Float(
        title=u"Pantothenic acid",
        required=False,
    )

    #<percent_refuse>0</percent_refuse>
    percent_refuse = schema.Float(
        title=u"Percent refuse",
        required=False,
    )

    #<phosphorus>24</phosphorus>
    phosphorus = schema.Float(
        title=u"Phosphorus",
        required=False,
    )

    #<polyunsaturated_fatty_acids >3.043</polyunsaturated_fatty_acids >
    polyunsaturated_fatty_acids = schema.Float(
        title=u"Polyunsaturated fatty acids",
        required=False,
    )

    #<potassium>24</potassium>
    potassium = schema.Float(
        title=u"Potassium",
        required=False,
    )

    #<protein>0.85</protein>
    protein = schema.Float(
        title=u"Protein",
        required=False,
    )

    #<retinol>671</retinol>
    retinol = schema.Float(
        title=u"Retinol",
        required=False,
    )

    #<riboflavin>0.034</riboflavin>
    riboflavin = schema.Float(
        title=u"Riboflavin",
        required=False,
    )

    #<saturated_fatty_acid >51.368</saturated_fatty_acid >
    saturated_fatty_acid = schema.Float(
        title=u"Saturated fatty acid",
        required=False,
    )

    #<selenium>1</selenium>
    selenium = schema.Float(
        title=u"Selenium",
        required=False,
    )

    #<sodium>576</sodium>
    sodium = schema.Float(
        title=u"Sodium",
        required=False,
    )
    #<sugar_total>0.06</sugar_total>
    sugar_total = schema.Float(
        title=u"Sugar Total",
        required=False,
    )
    #<thiamin>0.005</thiamin>
    thiamin = schema.Float(
        title=u"Thiamin",
        required=False,
    )
    #<total_dietary_fiber >0</total_dietary_fiber >
    total_dietary_fiber = schema.Float(
        title=u"Total dietary fiber",
        required=False,
    )
    #<total_lipid_(fat)>81.11</total_lipid_(fat)>
    total_lipid_fat = schema.Float(
        title=u"Total Lipid",
        required=False,
    )
    #<Vitamin_A >60</Vitamin_A >
    vitamin_a = schema.Float(
        title=u"Vitamin A",
        required=False,
    )
    #<Vitamin_A_(IU/100 g)>2499</Vitamin_A_(IU/100 g)>
    vitamin_a_iu = schema.Float(
        title=u"Vitamin A IU",
        required=False,
    )
    #<vitamin_A_retinol_activity_equivalents>684</vitamin_A_retinol_activity_equivalents>
    vitamin_a_retinol_activity_equivalents = schema.Float(
        title=u"Vitamin A retinol activity equivalents",
        required=False,
    )
    #<vitamin_b12>0.17</vitamin_b12>
    vitamin_b12 = schema.Float(
        title=u"Vitamin B12",
        required=False,
    )
    #<vitamin_B6>0.003</vitamin_B6>
    vitamin_b6 = schema.Float(
        title=u"Vitamin B6",
        required=False,
    )
    #<vitamin_c>0</vitamin_c>
    vitamin_c = schema.Float(
        title=u"Vitamin C",
        required=False,
    )
    #<vitamin_D >1.5</vitamin_D >
    vitamin_d = schema.Float(
        title=u"Vitamin D",
        required=False,
    )
    #<vitamin_e>2.32</vitamin_e>
    vitamin_e = schema.Float(
        title=u"Vitamin E",
        required=False,
    )
    #<vitamin_k>7</vitamin_k>
    vitamin_k = schema.Float(
        title=u"Vitamin K",
        required=False,
    )
    #<water>15.87</water>
    water = schema.Float(
        title=u"Water",
        required=False,
    )
    #<zinc>0.09</zinc>
    zinc = schema.Float(
        title=u"Zinc",
        required=False,
    )


class Food(Item):
    pass


class ParseXML(grok.View):
    grok.context(IFolderish)
    grok.require('zope2.View')

    def parse(self):
        here = os.path.realpath(os.path.dirname(__file__))
        # see http://stackoverflow.com/a/4363070/133235
        tree = etree.parse(os.path.join(here, "foods.xml"))
        root = tree.getroot()
        for food_item in root.iterchildren():
            def func(item):
                k = item.tag.lower().replace('-', '_')
                v = item.text
                try:
                    return k, float(v)
                except ValueError:
                    return k, v
            fields = dict(map(func, food_item.iterchildren()))
            self.context.invokeFactory('collective.nutrition.food',
                                       fields.pop('entry'),
                                       description=fields['title'],
                                       **fields)


class FoodSourceBinder(object):
    grok.implements(IContextSourceBinder, IQuerySource)

    def __init__(self, context=None):
        pass

    @property
    def vocab(self):
        if getattr(self, '_vocab', None) is None:
            catalog = api.portal.get_tool(name='portal_catalog')
            foods = catalog(object_provides=IFood.__identifier__)
            d = {}
            # make terms unique
            for item in foods:
                d[item.Title] = item.UID

            foods_list = [('', '')] + [(title, UID) for title, UID in d.iteritems()]
            self._vocab = SimpleVocabulary.fromItems(foods_list)
        return self._vocab

    def __call__(self, context):
        return FoodSourceBinder("init")

    def __contains__(self, term):
        return self.vocab.__contains__(term)

    def __iter__(self):
        return self.vocab.__iter__()

    def __len__(self):
        return self.vocab.__len__()

    def getTerm(self, value):
        return self.vocab.getTerm(value)

    def getTermByToken(self, value):
        return self.vocab.getTermByToken(value)

    def search(self, query_string):
        q = query_string.lower()
        return [k for k in self.vocab if q in k.token.lower()]
