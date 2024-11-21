def main():
    # opens file and reads its contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Prints contents of file
    print(file_contents)

# Call the main function to run the program
if __name__ == "__main__":
    main()