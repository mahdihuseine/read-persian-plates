from hezar.models import Model
import os

# نقشه تبدیل اعداد فارسی به انگلیسی
persian_to_english_numbers = {
    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'
}

# نقشه تبدیل حروف فارسی به حروف لاتین
persian_to_english_letters = {
    'ب': 'B', 'پ': 'P', 'ت': 'T', 'ث': 'TH', 'ج': 'J', 'چ': 'CH', 'ح': 'H', 'خ': 'KH', 'د': 'D', 'ذ': 'DH',
    'ر': 'R', 'ز': 'Z', 'ژ': 'ZH', 'س': 'S', 'ش': 'SH', 'ص': 'S', 'ض': 'Z', 'ط': 'T', 'ظ': 'Z', 'ع': 'A',
    'غ': 'GH', 'ف': 'F', 'ق': 'Q', 'ک': 'K', 'گ': 'G', 'ل': 'L', 'م': 'M', 'ن': 'N', 'و': 'V', 'ه': 'H',
    'ی': 'Y'
}

def convert_persian_to_english(text):
    # تبدیل اعداد فارسی به انگلیسی
    text = ''.join([persian_to_english_numbers.get(char, char) for char in text])

    # تبدیل حروف فارسی به حروف لاتین
    text = ''.join([persian_to_english_letters.get(char, char) for char in text])

    return text

# بارگذاری مدل از هاب Hezar
model = Model.load("hezarai/crnn-fa-64x256-license-plate-recognition")

# پیش‌بینی با استفاده از مدل
image_path = 'fa.bmp'
predicted_text = model.predict(image_path)

# استخراج متن پلاک از خروجی مدل
predicted_text = predicted_text[0]['text']  # دسترسی به متن از اولین دیکشنری در لیست

# تبدیل متن به انگلیسی (در صورتی که نیاز باشد)
predicted_text_english = convert_persian_to_english(predicted_text)

# ایجاد مسیر فایل متنی با استفاده از نام تصویر
base_name = os.path.splitext(image_path)[0]  # حذف پسوند فایل
txt_file_path = f"{base_name}_english.txt"  # اضافه کردن پسوند .txt به نام فایل

# ذخیره متن شناسایی‌شده در فایل
with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
    txt_file.write(predicted_text_english)

print("متن شناسایی‌شده در فایل ذخیره شد:", txt_file_path)
