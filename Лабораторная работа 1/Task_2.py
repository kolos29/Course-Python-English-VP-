# TODO Найдите количество книг, которое можно разместить на дискете

symbol_weight_in_kb = 4
symbols_per_line = 25
lines_per_page = 50
pages_in_book = 100
floppy_volume = 1.44

line_weight_in_kb = symbol_weight_in_kb*symbols_per_line
page_weight_in_kb = line_weight_in_kb*lines_per_page
book_weight_in_kb = page_weight_in_kb*pages_in_book
book_weight_in_mb = book_weight_in_kb/(1024**2)
book_quantity = round(floppy_volume/book_weight_in_mb)

print("Количество книг, помещающихся на дискету:", book_quantity)
