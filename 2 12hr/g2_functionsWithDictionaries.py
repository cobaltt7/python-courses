def introducer(person):
    print(
        f"Hi! I'm {person['name']}, my shirt is {person['shirt']}, and my laptop is"
        f" {person['laptop']}."
    )


introducer(
    {
        "name": "Paul",
        "shirt": "black",
        "laptop": "Windows",
    }
)
