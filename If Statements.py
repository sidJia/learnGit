

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif is_tall and not (is_male):
    print("You are a tall female")
else:
    print("You are a short female")

