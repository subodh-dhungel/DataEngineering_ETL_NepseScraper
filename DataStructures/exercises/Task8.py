#8. Write a Python program to convert a list to a list of dictionaries.
#["Black", "Red", "Maroon", "Yellow"]
#["#000000", "#FF0000", "#800000", "#FFFF00"]

colors = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

dict_list = [{"color": color, "code": code} for color, code in zip(colors, codes)]
print(dict_list)