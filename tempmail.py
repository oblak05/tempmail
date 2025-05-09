

from pytempbox import PyTempBox

# 1️⃣ CREATE - Instant email generator
temp_mail = PyTempBox()
email_address = temp_mail.generate_email()
print(f"📩 Your new temp email by Gueverro: {email_address}")

# 2️⃣ RECEIVE - Smart email checker (auto-retries)
print("\n🔎 Checking inbox...")
inbox = temp_mail.get_messages(email_address)

if not inbox:
    print("✨ Inbox is empty (try sending a test email first!)")
else:
    # 3️⃣ READ - Clean message display
    print(f"\n📨 Found {len(inbox)} message(s):")
    
    for i, message in enumerate(inbox, 1):
        print(f"\n━━━━ Message #{i} ━━━━")
        print(f"From: {message['from']}")
        print(f"Subject: {message['subject']}")
        print(f"\n{message['body_text'][:200]}...")  # Preview first 200 chars
        print("━━━━━━━━━━━━━━━━━━━━")