from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyRecipeBuilder(HTMLParser):
    #ingredient = False
    def __init__(self):
        HTMLParser.__init__(self)
        self.AnIngredient = False
        self.ingredients = []
        self.instructions = None
        self.time = None
        self.picture = None
        self.serves = None

    def handle_starttag(self, tag, attrs):
        if tag=="li":
            #print "Encountered a start tag:"
            self.AnIngredient = True
        if tag == "h1":
            self.IsTitle = True

    def handle_endtag(self, tag):
        if tag=="li":
            #print "Encountered  an end tag:"
            self.AnIngredient = False

    def handle_data(self, data):
        if self.AnIngredient:
            print "This is an ingredient :", data
            self.ingredients.append(data)
    

class Recipe(title, ingredients, instructions, time, serves, picture, source):

    def __init__(self):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.time = time
        self.serves = serves
        self.picture = picture
        self.source = source


# instantiate the parser and feed it some HTML
recipeBuilder = MyRecipeBuilder()

with open('recipe.html', 'r') as htmlfile:
    htmldata = htmlfile.readlines()

recipeBuilder.feed(unicode(htmldata))

print recipeBuilder.ingredients

#TODO: need to open recipe.html file