# TODO Найдите количество книг, которое можно разместить на дискете

symbol_weight = 4
line_weight = symbol_weight*25
page_weight = line_weight*50
book_weight = page_weight*100
book_weight_in_mb = book_weight/(1024**2)
book_quantity = round(1.44/book_weight_in_mb)

print("Количество книг, помещающихся на дискету:", book_quantity)
