def count_vowels_consonants(text):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    
    return vowel_count, consonant_count

# Example usage
text = "How many vowels and consonants are in this sentence?"
vowel_count, consonant_count = count_vowels_consonants(text)

print(f"The number of vowels in the string is: {vowel_count}")
print(f"The number of consonants in the string is: {consonant_count}")
