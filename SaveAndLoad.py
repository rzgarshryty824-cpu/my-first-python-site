import os
import json
import pickle
import os
from pathlib import Path


import os
import json
from pathlib import Path

def save_json(filename, data):
    tmp_filename = filename + ".tmp"
    try:
        Path(tmp_filename).parent.mkdir(parents=True, exist_ok=True)  # پوشه رو می‌سازه
        with open(tmp_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, default=lambda o: getattr(o, "dict", str(o)), ensure_ascii=False, indent=4)
        os.replace(tmp_filename, filename)
    except Exception as e:
        if os.path.exists(tmp_filename):
            os.remove(tmp_filename)
        print(f"❌ خطا در ذخیره فایل {filename}: {e}")

def load_json(filename, default_value=None):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ خطا در خواندن فایل {filename}: {e}")
    return default_value



def save_pkl(filename, data):
    tmp_filename = filename + ".tmp"
    try:
        Path(tmp_filename).parent.mkdir(parents=True, exist_ok=True)  # ← ایجاد پوشه اگر وجود نداشت
        with open(tmp_filename, "wb") as f:
            pickle.dump(data, f)
        os.replace(tmp_filename, filename)  # جایگزینی امن فایل اصلی
    except Exception as e:
        if os.path.exists(tmp_filename):
            os.remove(tmp_filename)
        print(f"❌ خطا در ذخیره فایل {filename}: {e}")

def load_pkl(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return {}


def save_session_json(name, number, auth, private_key, chat_id):
    data = {
            "number":number,
            "auth":auth,
            "private_key": private_key,
            "chat_id":chat_id
        }
    os.makedirs(f"session/{number}", exist_ok=True)
    with open(name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_session_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)