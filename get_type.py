import re

def detect_message_types(message, data_group) -> list[str]:
    """
    Detect all message types (text, link, mention, forwarded, mediaâ€¦)
    """
    types = []
    user_id = str(message.sender_id)

    # اگه کاربر هنوز وجود نداره، ایجاد کن
    if user_id not in data_group["users"]:
        data_group["users"][user_id] = {
            "num_text": 0,
            "num_photo": 0,
            "num_video": 0,
            "num_voice": 0,
            "num_audio": 0,
            "num_document": 0,
            "num_archive": 0,
            "num_executable": 0,
            "num_font": 0,
            "num_sticker": 0,
            "num_poll": 0,
            "num_contact": 0,
            "num_location": 0,
            "num_live_location": 0,
            "num_link": 0,
            "num_id": 0,
            "num_forwarded": 0,
        }

    user_data = data_group["users"][user_id]

    # Text
    if message.text:
        types.append("text")
        data_group["num_text"] += 1
        user_data["num_text"] += 1
        if getattr(message, "has_link", False):
            types.append("link")
            data_group["num_link"] += 1
            user_data["num_link"] += 1
        # Look for @mentions / IDs inside the text
        if re.search(r'@\w+', message.text):
            types.append("id")
            data_group["num_id"] += 1
            user_data["num_id"] += 1

    # Media
    if getattr(message, "is_media", False):
        if getattr(message, "is_photo", False):
            types.append("photo")
            data_group["num_photo"] += 1
            user_data["num_photo"] += 1
            
        if getattr(message, "is_video", False):
            types.append("video")
            data_group["num_video"] += 1
            user_data["num_video"] += 1
            
        if getattr(message, "is_audio", False):
            types.append("audio")
            data_group["num_audio"] += 1
            user_data["num_audio"] += 1
        if getattr(message, "is_voice", False):
            types.append("voice")
            data_group["num_voice"] += 1
            user_data["num_voice"] += 1
        if getattr(message, "is_document", False):
            types.append("document")
            data_group["num_document"] += 1
            user_data["num_document"] += 1
        if getattr(message, "is_archive", False):
            types.append("archive")
            data_group["num_archive"] += 1
            user_data["num_archive"] += 1
        if getattr(message, "is_executable", False):
            types.append("executable")
            data_group["num_executable"] += 1
            user_data["num_executable"] += 1
        if getattr(message, "is_font", False):
            types.append("font")
            data_group["num_font"] += 1
            user_data["num_font"] += 1

    # Sticker
    if getattr(message, "sticker", None):
        types.append("sticker")
        data_group["num_sticker"] += 1
        user_data["num_sticker"] += 1

    # Poll
    if getattr(message, "poll", None):
        types.append("poll")
        data_group["num_poll"] += 1
        user_data["num_poll"] += 1


    # Contact
    if getattr(message, "contact_message", None):
        types.append("contact")
        data_group["num_contact"] += 1
        user_data["num_contact"] += 1
        
    # Location
    if getattr(message, "location", None):
        types.append("location")
        data_group["num_location"] += 1
        user_data["num_location"] += 1
        
    if getattr(message, "live_location", None):
        types.append("live location")
        data_group["num_live_location"] += 1
        user_data["num_live_location"] += 1
    # Forwarded
    if getattr(message, "is_forwarded", False):
        types.append("forwarded")
        data_group["num_forwarded"] += 1
        user_data["num_forwarded"] += 1

    if not types:
        types.append("unknown")

    return types


def detect_user_types(all_data, data_group, sender_id) -> list[str]:
    types = []
    if sender_id == all_data.get("bot", ""):
        types.append(1)
    if sender_id in all_data.get("makar2", ""):
        types.append(2)
    if sender_id in data_group.get("manager", []):
        types.append(3)
    if sender_id in data_group.get("admin", []):
        types.append(4)
    if sender_id in data_group.get("silent", []):
        types.append(5)
    if sender_id in data_group.get("no_ansewr", []):
        types.append(6)
    if sender_id in data_group.get("mauf", []):
        types.append(6)
    return types