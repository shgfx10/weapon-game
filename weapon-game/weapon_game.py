

print("=== Welcome to the Weapon Selection Game ===")

weapon = input("Choose your weapon (firesword / icesword): ").lower()

while weapon != "firesword" and weapon != "icesword":
    print("❌ Invalid choice! You must choose either 'firesword' or 'icesword'.")
    weapon = input("Choose your weapon (firesword / icesword): ").lower()


print(f"\n✅ You have chosen the {weapon}!")


if weapon == "firesword":
    print("🔥 The Fire Sword burns with eternal hellfire!")
elif weapon == "icesword":
    print("❄️ The Ice Sword glows with heavenly frozen power!")
