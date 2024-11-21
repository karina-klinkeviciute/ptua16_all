def decode(message_file):
    pyramid_lines = []

    # Read the pyramid structure from the file
    with open(message_file, 'r') as file:
        for line in file:
            # Split each line into a list of words
            line_words = line.strip().split()

            # Extract the number and word from the line
            num, word = int(line_words[0]), line_words[-1]

            # Append the word to the pyramid_lines list
            pyramid_lines.append((num, word))

    # Sort the lines based on the numbers
    sorted_lines = sorted(pyramid_lines, key=lambda x: x[0])

    # Extract the words from the sorted lines
    decoded_words = [word for _, word in sorted_lines]

    # Build the decoded message
    decoded_message = ' '.join(decoded_words)

    return decoded_message

# Example usage:
message_file_path = "C:\\Users\\dmste\\Desktop\\coding_qual_input.txt"
decoded_message = decode(message_file_path)
print(decoded_message)

