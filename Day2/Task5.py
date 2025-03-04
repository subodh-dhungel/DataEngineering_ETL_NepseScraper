with open("original_text.txt", "w", encoding="utf-8") as file:
    file.write("Hello, this is a test file!\nHello world.\n")

with open("original_text.txt", "r", encoding="utf-8") as file:
    text = file.read()
    byte_data = text.encode("utf-8")

with open("bytes_file.bin", "wb") as file:
    file.write(byte_data)

with open("bytes_file.bin", "rb") as file:
    read_bytes = file.read()
    decoded_text = read_bytes.decode("utf-8")

print("Original Text:")
print(text)
print("\nDecoded Text:")
print(decoded_text)