class RecipeHTMLtags():

    def __init__(self):
        self.titleTag = None
        self.ingredientsTag = None
        self.instructionsTag = None
        self.url = None


tagsDatabase = {'foodnetwork.com': RecipeHTMLtags(),
                'seriouseats.com': RecipeHTMLtags(),
                'testurl.com': RecipeHTMLtags()}

tagsDatabase['testurl.com'].titleTag = 'h1'
tagsDatabase['testurl.com'].ingredientsTag = 'li'
tagsDatabase['testurl.com'].instructionsTag = 'b'
tagsDatabase['testurl.com'].url = 'testurl.com'

tagsDatabase['foodnetwork.com'].titleTag = 'h1'
tagsDatabase['foodnetwork.com'].ingredientsTag = 'ingredient'
tagsDatabase['foodnetwork.com'].instructionsTag = 'procedure'
tagsDatabase['foodnetwork.com'].url = 'foodnetwork.com'

tagsDatabase['seriouseats.com'].titleTag = 'h1'
tagsDatabase['seriouseats.com'].ingredientsTag = 'li class="ingredient" itemprop="ingredients"'
tagsDatabase['seriouseats.com'].instructionsTag = 'procedure'
tagsDatabase['seriouseats.com'].url = 'seriouseats.com'

#def loadTagsDatabase(dataFile):
#
#   with open(dataFile, 'r') as tagsDatafile:
#       htmldata = tagsDatafile.readlines()
