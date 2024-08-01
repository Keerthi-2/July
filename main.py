
import getAuth as authCode
import getAccessToken 
def automate_login():

    # Obtain Authorization Code
    authCode()

    #Exchange Authorization Code for Access Token
    getAccessToken()

    #Access LinkedIn API with Access Token
    





if __name__ == '__main__':

    automate_login()