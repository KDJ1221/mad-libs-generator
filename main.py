def madLibs():
    adjective = input("Please enter an adjective: ")
    noun = input("Please enter a noun: ")
    verb_past = input("Please enter a verb, past tense: ")
    second_adjective = input("Enter another adjective: ")
    final_adjective = input("Enter another adjective: ")
    final_noun = input("Enter another noun: ")

    story = input("Okay now pick a story: A) Zoo B) Park\n")
    if story == 'A':
        print("You've chosen the story about the zoo!")
        print(f"Today I went to the zoo. I saw a(n) {adjective} {noun}.")
        print(f"I {verb_past} the {second_adjective} {final_noun} and then got a {final_adjective} scoop of ice cream")
    elif story == 'B':
        print("You've chosen the story about the park!")
        print(f"Today my camp group went to a {adjective} park with a large {noun}")
        print(f"It was a fun park with a pretty cool {second_adjective} {final_noun}")
        print(f"My friends and I {verb_past} to the final ride and were pretty {final_adjective} by the end of the day")

madLibs()