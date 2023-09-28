def generate_number_and_save(start, end, out_file):
    with open(out_file, "w") as file:
        for i in range(start, end +1):
            formatted_number = str(i).zfill(4)
            file.write(formatted_number + "\n")

if __name__ == "__main__":
    start_number = int(input("Enter start number: "))
    end_number = int(input("Enter end number: "))
    out_file = input("Enter output file name: ")
    generate_number_and_save(start_number, end_number, out_file)
    print(f"Number file has been generated from {start_number} to {end_number} saved in {out_file}")