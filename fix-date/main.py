def run(input_date: str, base_year: int) -> str:
    date_split= input_date.split("/")
    year_final = int(date_split[2]) + base_year
    output_date = f"{date_split[1]}-{date_split[0]}-{str(year_final)}"
    return output_date


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
