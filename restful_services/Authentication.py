from common.Constants import *
from rauth import OAuth2Service
from flask import request, redirect, session
from flask_restful import Resource

facebookAgent = OAuth2Service(name=facebookAuthentication.name,
                              authorize_url=facebookAuthentication.authorizedUrl,
                              access_token_url=facebookAuthentication.accessTokenUrl,
                              client_id=facebookAuthentication.appID,
                              client_secret=facebookAuthentication.secretKey,
                              base_url=facebookAuthentication.graphUrl)


class facebookLogin(Resource):
    def get(self):
        # facebookAuthentication.returnURL = request.args.get("redirect")
        params = {'redirect_uri': facebookAuthentication.redirectURL}
        return redirect(facebookAgent.get_authorize_url(**params))


class facebookCallBack(Resource):
    def get(self):
        # make a request for the access token credentials using code
        data = dict(code=request.args['code'], redirect_uri=facebookAuthentication.redirectURL)
        facebookSession = facebookAgent.get_auth_session(data=data)
        session["facebook_user_token"] = facebookSession.access_token
        # return redirect(facebookConstants.returnURL)
