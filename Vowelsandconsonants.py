def Check_Vow(string, vowels):

    final = [each for each in string if each in vowels]

    print(len(final))

    print(final)
    
def Check_con(string, consonants):

    final1 = [each for each in string if each in consonants]

    print(len(final1))

    print(final1)

     
# Driver Code

string = "Geeks for Python programming"
consonants="BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);
Check_con(string, consonants);


 