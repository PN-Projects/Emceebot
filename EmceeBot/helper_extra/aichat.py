from EmceeBot import mongodb as db_x

kuki = db_x["CHATBOT"]


def add_chat(chat_id):
    stark = kuki.find_one({"chat_id": chat_id})
    if stark:
        return False
    kuki.insert_one({"chat_id": chat_id})
    return True


def remove_chat(chat_id):
    stark = kuki.find_one({"chat_id": chat_id})
    if not stark:
        return False
    kuki.delete_one({"chat_id": chat_id})
    return True


def get_all_chats():
    r = list(kuki.find())
    if r:
        return r
    return False


def get_session(chat_id):
    stark = kuki.find_one({"chat_id": chat_id})
    if not stark:
        return False
    return stark
