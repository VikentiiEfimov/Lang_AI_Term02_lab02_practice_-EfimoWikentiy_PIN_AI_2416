def cache(db: str, expiration: int):
    def decorator(func):
        storage = {} 

        def wrapper(thing: str) -> str:
            if thing in storage:
                cached_str, remaining = storage[thing]
                if remaining > 0:
                    storage[thing][1] = remaining - 1
                    return f"Info about: {thing} cached in {db}, expire={remaining - 1}"
                else:
                    new_str = f"Info about: {thing} from {db}, now cached with expire={expiration}"
                    storage[thing] = [new_str, expiration]
                    return new_str
            else:
                new_str = f"Info about: {thing} from {db}, now cached with expire={expiration}"
                storage[thing] = [new_str, expiration]
                return new_str

        return wrapper
    return decorator


class T2:
    def run(self) -> str:
        thing = input("Введите предмет (thing): ").strip()

        @cache("postgresql", 5)
        def get_info_pg(thing: str) -> str:
            return f"Real info about {thing}"
        for _ in range(7):
            print(get_info_pg(thing))

        @cache("sqlite", 3)
        def get_info_sqlite(thing: str) -> str:
            return f"Real info about {thing}"
        for _ in range(5):
            print(get_info_sqlite(thing))

        return "Готово"