import os

class Config:

    BOT_TOKEN = os.environ.get("1173368697:AAF5y6krHu-X3KjzpfeaZbmgzclJH5gAf7U")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", 'youtubeitbot')

    API_ID = int(os.environ.get("1144902"))

    API_HASH = os.environ.get("e743e5a4f35076e4c558a4bd713082e9")

    CLIENT_ID = os.environ.get("285126996267-d58o2euqvb47sbar0bmsid5fmpmgt8b4.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("Kbmpa7_0vM317_jV8KtGJ1CT")

    BOT_OWNER = int(os.environ.get("754495556"))
    
    AUTH_USERS_TEXT = os.environ.get("754495556", '')

    AUTH_USERS = [BOT_OWNER, 374321319] + ([int(user.strip()) for user in AUTH_USERS_TEXT.split(",")] if AUTH_USERS_TEXT else [])
    
    VIDEO_DESCRIPTION = os.environ.get("VIDEO_DESCRIPTION", '').replace('<', '').replace('>', '')
    
    VIDEO_CATEGORY = int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    
    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", '')
    
    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", '')
    
    DEBUG = bool(os.environ.get("DEBUG"))
    
    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ['private', 'public', 'unlisted']:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"



