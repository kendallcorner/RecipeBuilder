from html.parser import HTMLParser
from RecipeHTMLtags import *


# create a subclass and override the handler methods
class MyRecipeBuilder(HTMLParser):
    #ingredient = False
    def __init__(self, tagsdb, url):
        HTMLParser.__init__(self)
        self.anIngredient = False
        self.ingredients = []
        self.inInstructions = False
        self.instructions = []
        self.time = None
        self.picture = None
        self.serves = None
        self.isTitle = False
        self.title = None
        self.url = url
        self.tagsdb = tagsdb

    def handle_starttag(self, tag, attrs):
        if tag == self.tagsdb[self.url].ingredientsTag:
            #print "Encountered a start tag:"
            self.anIngredient = True
        if tag == self.tagsdb[self.url].titleTag:
            self.isTitle = True
        #if tag == self.tagsdb[self.url].titleTag:
            #self.inInstructions = True

    def handle_endtag(self, tag):
        if tag == self.tagsdb[self.url].ingredientsTag:
            #print "Encountered  an end tag:"
            self.anIngredient = False
        if tag == self.tagsdb[self.url].titleTag:
            self.isTitle = False
        #if tag == self.tagsdb[self.url].titleTag:
            #self.inInstructions = True

    def handle_data(self, data):
        if self.anIngredient:
            self.ingredients.append(data)
        if self.isTitle:
            self.title = data

    def buildRecipe(self):
        return Recipe(self.title, self.ingredients,
                      None, None, None, None, None)


class Recipe():

    def __init__(self, title, ingredients, instructions, time,
                 serves, picture, source):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.time = time
        self.serves = serves
        self.picture = picture
        self.source = source

    def show(self):
        print (self.title)
        print (self.ingredients)
        print (self.instructions)
        print (self.time)
        print (self.serves)
        print (self.picture)
        print (self.source)


# instantiate the parser and feed it some HTML
recipeBuilder = MyRecipeBuilder(tagsDatabase, "testurl.com")

with open('recipe.html', 'r') as htmlfile:
    htmldata = htmlfile.read()

recipeBuilder.feed(htmldata)

newRecipe = recipeBuilder.buildRecipe()

newRecipe.show()

#recipeBuilder = MyRecipeBuilder(tagsDatabase, "seriouseats.com")

#with open('Pumpkin.html', 'r') as htmlfile:
    #htmldata = htmlfile.readlines()

#recipeBuilder.feed(unicode(htmldata))

#newRecipe = recipeBuilder.buildRecipe()

#newRecipe.show()
