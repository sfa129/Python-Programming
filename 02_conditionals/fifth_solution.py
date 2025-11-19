password = "324kdjlk3k"

if len(password) > 8:
    strength = "very strong"
elif len(password) > 6:
    strength = "strong"
else: 
    strength = "weak"

print(strength)