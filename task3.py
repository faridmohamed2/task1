def is_vowel(letter):
    vowels="aeiouAEIOU"
    if  letter in vowels:
        return letter
    

if is_vowel("f"):
    print("the letter is vowel")
else:
    print("the letter is not vowel")