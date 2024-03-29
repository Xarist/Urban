class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def generate_exception(some_data):
    try:
        if not some_data:
            raise InvalidDataException("Данные не переданы")

        if len(some_data) < 5:
            raise ProcessingException("Обработка данных не удалась!")

    except InvalidDataException as exc:
        print("Обработка InvalidDataException:", exc)
        # raise
    except ProcessingException as exc:
        print("Обработка ProcessingException:", exc)
        # raise

    else:
        print("Действия, выполняемые при отсутствии исключений")

    finally:
        print("Действия, выполняемые всегда")


def main():
    generate_exception([])
    print()

    generate_exception("1234")
    print()

    generate_exception('my_data')
    print()


main()

