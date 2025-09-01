from mnemonic import Mnemonic

# ۱۱ کلمه شما با جای خالی برای کلمه دوم
words = ["foot", None, "tiger", "admit", "champion", "van",
         "erosion", "route", "divert", "net", "destroy", "ask"]

mnemo = Mnemonic("english")

print("=== شروع جستجوی کلمه گمشده ===")
print("تعداد کل کلمات ممکن:", len(mnemo.wordlist))
print("لطفاً صبر کنید، این فرآیند ممکن است چند دقیقه طول بکشد...\n")

found = False
counter = 0

# حلقه برای امتحان کردن همه کلمات BIP39
for word in mnemo.wordlist:
    counter += 1
    if counter % 100 == 0:
        print(f"در حال بررسی کلمه شماره {counter} از {len(mnemo.wordlist)}...")

    test_words = words.copy()
    test_words[1] = word  # جایگذاری کلمه دوم
    phrase = " ".join(test_words)
    
    if mnemo.check(phrase):
        print("\n✅ کلمه گمشده پیدا شد:", word)
        found = True
        break

if not found:
    print("\n⚠️ هیچ کلمه‌ای پیدا نشد. مطمئن شوید که بقیه کلمات درست هستند.")
