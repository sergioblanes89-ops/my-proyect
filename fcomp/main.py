def run(xmin: int, xmax: int) -> list:
    intervalo = list(range(xmin, xmax+1))
    values = [3 * v1 + 2 for v1 in intervalo]
    return values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
