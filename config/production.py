from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR,'pybo.db')
)

SQLALCHEMY_TRACK_MODIFICATION = False


SECRET_KEY = b'\xc6\xa3\x01\xf3\xf9\xd8\x90\x0flu\xb1l\xc1'