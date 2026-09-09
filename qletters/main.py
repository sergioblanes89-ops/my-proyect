def run(text: str) -> list[str]:
    cola_mayus = []
    cola_minus = []

    for ch in text:
        if ch == ' ':
            cola_mayus = []
            cola_minus = []
        elif ch.isalpha():
            if ch.isupper():
                cola_mayus.append(ch)
            else:
                cola_minus.append(ch)

    return cola_mayus + cola_minus

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
