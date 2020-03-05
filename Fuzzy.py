from fuzzywuzzy import fuzz
Str1 = "Evil Batman"
Str2 = "Evil batman"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
print(Ratio)


r= fuzz.ratio("this is a test", "this is a test!")
print(r)