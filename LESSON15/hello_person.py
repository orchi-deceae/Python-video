def hello(name, lang):
    greetings = {
        "English": "Hello",
        "French": "Salut",
        "Yoruba": "kilo de",
        "Spanish": "Hola",
        "German": "Hallo"
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "French", "Yoruba", "Spanish", "German"], 
        help="The language of the greeting"
    )
    
    args = parser.parse_args()

    hello(args.name, args.lang)

    # print(f"Hello {args.name}!")

    # "C:\Users\ADMIN\OneDrive\Desktop\Python video\LESSON15\hello_person.py"