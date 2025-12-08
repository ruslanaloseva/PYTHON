
disk_size_mb = 1.44
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

disk_size_bytes = disk_size_mb * 1024 * 1024
chars_per_book = pages * lines_per_page * chars_per_line
book_size_bytes = chars_per_book * bytes_per_char

books_on_disk = int(disk_size_bytes // book_size_bytes)

print(f"На дискету поместится {books_on_disk} одинаковых книг")