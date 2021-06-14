import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    #CLIENT_ID = "ffe18477-6d0b-4ddf-8e80-1908c4874679"  # project1ArticleCMS
    #CLIENT_SECRET = "b3D6z_K-25c~Kjj90zYUq1tzmWyH-i_fAZ" #  project1ArticleCMS
    
    CLIENT_ID = "e76afb98-de31-4914-b603-1a1ddeda1403" # ArticleCMSUdacity APP
    CLIENT_SECRET = "8VlskU3pr2oqUWP-~41V8~-afX-Nj_.n1W" # ArticleCMSUdacity APP

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'project1articlecms'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'F+Qf1tYlbE9GM82e77AgD3y7cebw6Hx63apInfX7mnFzOAexIF5OE/ERWP+rWkJ/BYpiwnKMb2QVdETvI58R/A=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'helloworld.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'helloworld'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'articlecmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Password123?'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")
    AUTHORITY = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
    #AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    #AUTHORITY = "https://login.microsoftonline.com/garima"

    

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    #ENDPOINT = 'https://login.microsoftonline.com/consumers/oauth2/authorize' 
    #ENDPOINT = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
    #ENDPOINT = 'https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize'
    #ENDPOINT = "https://login.microsoftonline.com/0ebd8976-160f-42fd-a9bf-92ae762dab79/oauth2/v2.0/authorize"
    #ENDPOINT = ' https://login.microsoftonline.com/0ebd8976-160f-42fd-a9bf-92ae762dab79/v2.0/adminconsent?client_id=e76afb98-de31-4914-b603-1a1ddeda1403'
    ENDPOINT = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
