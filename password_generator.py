import random
import time

# Given Data
names = ["Ali", "Mustafa"]
years = ["1990"]
footballs = ["Messi"]
cars = ["Nissan"]
cats = ["Siri"]
sons = ["Ahmed"]

# Configuration
TOTAL_PASSWORDS = 100000
OUTPUT_FILE = "passwords.txt"
SPECIAL_CHARS = ["@", "#", "_", "!", "$"]

def generate_passwords():
    start_time = time.time()
    passwords = set()
    
    # We continue generating until the set size reaches 100,000
    while len(passwords) < TOTAL_PASSWORDS:
        # Select random elements
        n = random.choice(names)
        y = random.choice(years)
        f = random.choice(footballs)
        c = random.choice(cars)
        ct = random.choice(cats)
        s = random.choice(sons)
        rand_num = random.randint(0, 9999)
        rand_char = random.choice(SPECIAL_CHARS)
        
        # 5 Different Patterns
        patterns = [
            f"{n}{y}",                          # Ali1990
            f"{f}{rand_char}{y}",               # Messi@1990
            f"{c}_{s}",                         # Nissan_Ahmed
            f"{ct.lower()}{rand_num}!",         # siri123!
            f"{n}{rand_char}{s.upper()}{rand_num}" # Ali$AHMED99
        ]
        
        # Add a random pattern to the set
        passwords.add(random.choice(patterns))
        
    # Save to file
    with open(OUTPUT_FILE, "w") as f:
        for pwd in passwords:
            f.write(pwd + "\n")
            
    end_time = time.time()
    
    print(f"✅ Successfully generated {len(passwords)} passwords!")
    print(f"📁 Saved to: {OUTPUT_FILE}")
    print(f"⏱️  Time elapsed: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    generate_passwords()