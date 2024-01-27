import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_similar_books(self):
        book_name = 'Кладбище домашних животных'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1 and collector.get_books_genre() == {book_name: ''}

    def test_add_new_book_add_book_with_name_over_40_symbols(self):
        book_name = 'Чудесный костюм цвета сливочного мороженого'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0 and collector.get_books_genre() == {}

    @pytest.mark.parametrize('book, genre', [['Гарри Поттер и Кубок огня', 'Фантастика'],
                                             ['Убийство в Восточном экспрессе', 'Детективы']])
    def test_set_book_genre_set_genre_from_genre_list(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    def test_set_book_genre_book_not_in_books_genre_list(self):
        collector = BooksCollector()
        collector.set_book_genre('Крокодил Гена', 'Мультфильмы')
        assert collector.get_book_genre('Крокодил Гена') is None

    @pytest.mark.parametrize('book, genre', [['Божественная комедия', 'Трагедии'],
                                             ['Мифы и легенды Древней Греции', 'Мифы и легенды']])
    def test_set_book_genre_genre_not_in_genre_list(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == ''

    def test_get_book_genre_book_in_books_genre_list(self):
        book_name = 'Жареные зелёные помидоры'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Комедии')
        assert collector.get_book_genre(book_name) == 'Комедии'

    def test_get_book_genre_book_not_in_books_genre_list(self):
        book_name = 'Убить пересмешника'
        collector = BooksCollector()
        assert collector.get_book_genre(book_name) is None

    def test_get_book_genre_book_without_genre(self):
        book_name = 'Зелёный свет'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre_two_books_in_each_genre(self):
        books_and_genres = [['Коралина', 'Ужасы'], ['Зов Ктулху', 'Ужасы'], ['Книга Джунглей', 'Мультфильмы'],
                            ['Русалочка', 'Мультфильмы']]
        collector = BooksCollector()
        for i in books_and_genres:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])
        assert collector.get_books_with_specific_genre('Ужасы') == ['Коралина', 'Зов Ктулху'] and collector.get_books_with_specific_genre('Мультфильмы') == ['Книга Джунглей', 'Русалочка']

    @pytest.mark.parametrize('genre', ['Мультфильмы', 'Детективы'])
    def test_get_books_with_specific_genre_no_books_with_this_genre(self, genre):
        books_and_genres = [['Коралина', 'Ужасы'], ['Зов Ктулху', 'Ужасы'], ['Дневник Бриджит Джонс', 'Комедии'],
                            ['Укрощение строптивой', 'Комедии']]
        collector = BooksCollector()
        for i in books_and_genres:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])
        assert collector.get_books_with_specific_genre(genre) == []

    @pytest.mark.parametrize('genre', ['Трагедии', 'Мифы и легенды'])
    def test_get_books_with_specific_genre_no_genre_in_genre_list(self, genre):
        book_name = 'Дневник Бриджит Джонс'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Комедии')
        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_genre_empty_dictionary(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_books_genre_with_one_book(self):
        book_name = 'Белая рыба'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1 and collector.get_books_genre() == {book_name: ''}

    @pytest.mark.parametrize('book, genre', [['Фантастические твари и где они обитают', 'Фантастика'], ['Наруто', 'Мультфильмы'],
                                             ['Дневник сварливого кота', 'Комедии']])
    def test_get_books_for_children_all_books_are_suitable(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == [book]

    @pytest.mark.parametrize('book, genre', [['Побег из Шоушенка', 'Ужасы'], ['Шерлок Холмс', 'Детективы']])
    def test_get_books_for_children_all_books_are_unsuitable(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert not collector.get_books_for_children() == [book]

    def test_add_book_in_favorites_book_added_in_favorites_list(self):
        book_name = 'Гарри Поттер и Принц полукровка'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1 and collector.get_list_of_favorites_books() == [book_name]

    def test_add_book_in_favorites_try_add_book_in_favorites_again(self):
        book_name = '12 стульев'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert not len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_book_not_in_books_genre_list(self):
        book_name = 'Незнайка на Луне'
        collector = BooksCollector()
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_in_favorites_list(self):
        book_name = 'Гарри Поттер и Принц полукровка'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_favorites_list_contains_four_books(self):
        books = ['Коралина', 'Зов Ктулху', 'Книга Джунглей', 'Русалочка']
        collector = BooksCollector()
        for i in books:
            collector.add_new_book(i)
            collector.add_book_in_favorites(i)
        assert len(collector.get_list_of_favorites_books()) == 4 and collector.get_list_of_favorites_books() == books
