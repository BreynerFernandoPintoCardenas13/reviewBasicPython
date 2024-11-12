letraSecreta = "a"

while True:
    desicion = input("Enter a letter between A and E: ").lower()

    if desicion not in ["a", "b", "c", "d", "e"]:
        print("Please enter a valid letter between A and E.")
        continue

    def guess(resultado):
        match resultado:
            case "b":
                return "Nah bro B that is not the correct letter."
            case "c":
                return "Nah bro C that is not the correct letter."
            case "d":
                return "Nah bro D that is not the correct letter."
            case "e":
                return "Nah bro E that is not the correct letter."

    respuesta = guess(desicion)
    print(respuesta)

    if desicion == letraSecreta:
        print("WOWWWW YOU GUESSED IT!")
        break
