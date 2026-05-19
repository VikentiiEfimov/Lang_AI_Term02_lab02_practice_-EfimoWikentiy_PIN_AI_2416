import functools
import random
from string import ascii_lowercase, ascii_uppercase

user_role = "admin"

class T1:
    @staticmethod
    def role_required(role: str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                global user_role
                if user_role == role:
                    return func(*args, **kwargs)
                else:
                    print(f"Доступ запрещён: требуется роль '{role}', текущая роль '{user_role}'")
                    return None
            return wrapper
        return decorator

    @staticmethod
    @role_required("admin")
    def secret_resource():
        chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
        while True:
            password = ''.join(random.choice(chars) for _ in range(8))
            yield password

    def run(self, lst):
        results = []
        for rl in lst:
            global user_role
            user_role = rl
            gen = self.secret_resource()
            if gen is not None:
                print(f"Роль '{rl}': первые 5 паролей")
                passwords = []
                for i in range(5):
                    passwords.append(f"{i+1}: {next(gen)}")
                results.append("\n".join(passwords))
            else:
                results.append("secret_resource() вернула None – функция не выполнена.")
        return results