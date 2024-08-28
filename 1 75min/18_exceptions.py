try:
    raise BaseException("Bad")
except BaseException as e:
    print(e)
print("yay")

raise BaseException("Bad")

print("yay")
