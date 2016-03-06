class common:
    baseUrl = "http://localhost:5000"


class facebookAuthentication:
    def __init__(self):
        pass
    name = "facebook"
    authorizedUrl = "https://www.facebook.com/dialog/oauth"
    graphUrl = 'https://graph.facebook.com/'
    accessTokenUrl = graphUrl + 'oauth/access_token'
    secretKey = "2c0536b9a512f22028f7a3c55168f2ea"
    appID = "1684553838485934"
    GraphAPIVersion = "v2.5"
    redirectURL = common.baseUrl + "/callback/facebook"
    baseGraphApiUrl = "https://graph.facebook.com/v2.5/"
    getUserInitInfoUrl = "me?fields=name,birthday,about,bio,email,education,gender," \
                         "id,hometown"
    returnURL = ""
