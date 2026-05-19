from task_1 import T1
from task_2 import T2
from task_3 import T3

rls = input("Ввод пользователей: ").split()
print(T1().run(rls))

print(T2().run())
print(T3().run())