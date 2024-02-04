# qa_python
## test_add_new_book_add_two_books
>проверка возможности добавления книг в словарь books_genre

## test_add_new_book_add_similar_books
>проверка невозможности добавления одной и той же книги в словарь books_genre дважды (названия совпадают)

## test_add_new_book_add_book_with_name_over_40_symbols
>проверка невозможности добавления книги в словарь books_genre с названием из более 40 символов

## test_set_book_genre_set_genre_from_genre_list
>проверка возможности установить книге из словаря books_genre жанр из списка genre

## test_set_book_genre_book_not_in_books_genre_list
>проверка невозможности установить жанр из списка genre книге, которой нет в словаре books_genre

## test_set_book_genre_genre_not_in_genre_list
>проверка невозможности установить книге из словаря books_genre жанр, которого нет в списке genre

## test_get_book_genre_book_in_books_genre_list
>проверка получения жанра книги из словаря books_genre по её названию

## test_get_book_genre_book_not_in_books_genre_list
>проверка получения жанра книги, которой нет в словаре books_genre

## test_get_book_genre_book_without_genre
>проверка получения жанра книги из словаря books_genre, которой жанр не установлен

## test_get_books_with_specific_genre_two_books_in_each_genre
>проверка получения списка книг по определённому жанру

## test_get_books_with_specific_genre_no_books_with_this_genre
>проверка получения списка книг по определённому жанру, книги по данному жанру в словаре books_genre отсутствуют

## test_get_books_with_specific_genre_no_genre_in_genre_list
>проверка получения списка книг по определённому жанру, данные жанры в списке жанров genre отсутствуют

## test_get_books_genre_empty_dictionary
>проверка получения словаря books_genre, словарь не заполнен

## test_get_books_genre_with_one_book
>проверка получения словаря books_genre, в словаре одна книга (один элемент)

## test_get_books_for_children_all_books_are_suitable
>проверка получения списка книг из словаря books_genre с жанром без возрастного рейтинга, которые подходят для детей

## test_get_books_for_children_all_books_are_unsuitable
>проверка получения списка книг из словаря books_genre с жанром без возрастного рейтинга, которые подходят для детей.
Список books_genre содержит только книги с жанром из genre_age_rating

## test_add_book_in_favorites_book_added_in_favorites_list
>проверка добавления книги из словаря books_genre в список избранных книг

## test_add_book_in_favorites_try_add_book_in_favorites_again
>проверка невозможности добавления книги в список избранных книг повторно

## test_add_book_in_favorites_book_not_in_books_genre_list
>проверка невозможности добавления книги в список избранных книг, которой нет в словаре books_genre

## test_delete_book_from_favorites_book_in_favorites_list
>проверка удаления книги из списка избранных книг (книга в списке присутствует)

## test_get_list_of_favorites_books_favorites_list_contains_four_books
>проверка получения списка избранных книг, в списке 4 книги