from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25479482"))
    API_HASH = getenv("API_HASH", "6ab604ff91a73fb91cc6526818e28ab1")
    BOT_TOKEN = getenv("BOT_TOKEN", "6210086334:AAEKhSp8l8PzmjKSbYQeCyUvm4RxH37S--I")
    FSUB = getenv("FSUB", "Krsbots")
    CHID = int(getenv("CHID", "-1001779064622"))
    SUDO = list(map(int, getenv("5736579519").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://kartik:Kartik8379@cluster0.zrpl3tc.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
