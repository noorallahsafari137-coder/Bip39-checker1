from mnemonic import Mnemonic

# ۱۱ کلمه شما با جای خالی برای کلمه دوم
words = ["foot", None, "tiger", "admit", "champion", "van",
         "erosion", "route", "divert", "net", "destroy", "ask"]

mnemo = Mnemonic("english")

# بررسی ۱۱ کلمه دیگر
invalid_words = [w for w in words if w is not None and w not in mnemo.wordlist]

if invalid_words:
    print("⚠️ هشدار: یکی یا چند کلمه شما صحیح نیستند یا فاصله اضافی دارند:")
    for w in invalid_words:
        print(" -", w)
    print("\nلطفاً کلمات خود را دوباره بررسی کنید قبل از جستجوی کلمه دوم.")
else:
    print("✅ همه ۱۱ کلمه دیگر درست هستند. جستجوی کلمه دوم شروع می‌شود...\n")

    found = False
    counter = 0

    for word in mnemo.wordlist:
        counter += 1
        if counter % 100 == 0:
            print(f"در حال بررسی کلمه شماره {counter} از {len(mnemo.wordlist)}...")

        test_words = words.copy()
        test_words[1] = word
        phrase = " ".join(test_words)

        if mnemo.check(phrase):
            print("\n✅ کلمه گمشده پیدا شد:", word)
            found = True
            break

    if not found:
        print("\n⚠️ هیچ کلمه‌ای پیدا نشد. مطمئن شوید که بقیه کلمات دقیق هستند.")
