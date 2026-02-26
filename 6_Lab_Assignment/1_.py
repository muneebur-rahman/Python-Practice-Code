s=input("Enter String: ")
vowel_count=0
consonent_count=0
space_count=0
lower_case_count=0
vowels="aeiouAEIOU"
for ch in s:
    if ch in vowels:
        vowel_count+=1
    elif ch.isalpha():
        consonent_count+=1
    elif ch==" ":
        space_count+=1
    elif ch.islower():
        lower_case_count+=1
print(f"Vowels = {vowel_count}")
print(f"Consonent = {consonent_count}")
print(f"Space = {space_count}")
print(f"Lower Case Letter = {lower_case_count}")
    