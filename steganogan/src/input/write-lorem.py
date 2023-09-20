import lipsum

output_directory = "test_files"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') for _ in range(length))

for i in range(1, 11):
    file_name = f"test_{i}.txt"
    file_path = os.path.join(output_directory, file_name)

    # Generate random size between 5 KB and 1 MB
    file_size_kb = 5 * 1024  # 5 KB
    file_size_kb *= (2 ** (i - 1))  # Doubling size for each file
    if file_size_kb > 1024 * 1024:
        continue  # Skip if size exceeds 1 MB

    # Generate random text
    lorem_text = generate_random_text(file_size_kb)

    # Write text to the file
    with open(file_path, "w") as file:
        file.write(lorem_text)

    print(f"Generated '{file_path}' with size {file_size_kb / 1024:.2f} KB")
