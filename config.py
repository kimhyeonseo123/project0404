import os

#폴더
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR,'pybo.db')
)

SQLALCHEMY_TRACK_MODIFICATION = False


SECRET_KEY = "MBC606"