import sys
import os
import importlib.util
from pathlib import Path

class ModuleLoader:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.loaded_modules = {}
        
    def load_module(self, module_path, class_name):
        try:
            full_path = self.project_root / module_path
            
            if not full_path.exists():
                print(f"Файл не найден: {full_path}")
                return None
                
            spec = importlib.util.spec_from_file_location(module_path.replace('/', '.'), full_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, class_name):
                self.loaded_modules[class_name] = getattr(module, class_name)
                return self.loaded_modules[class_name]
            else:
                print(f"Класс {class_name} не найден в {module_path}")
                return None
                
        except Exception as e:
            print(f"Ошибка загрузки модуля {module_path}: {e}")
            return None
        
class ProgramRunner:
    def __init__(self):
        self.results = {}
        self.loader = ModuleLoader()
        self.load_all_modules()
        
    def load_all_modules(self):
        modules_to_load = [
            ("task_1.py", "T1"),
            ("task_2.py", "T2"),
            ("task_3.py", "T3")
        ]
        for module_path, class_name in modules_to_load:
            self.loader.load_module(module_path, class_name)

    def run_1_task(self):
        T1 = self.loader.loaded_modules["T1"]
        rls = input("Ввод пользователей: ").split()
        task = T1()
        self.results['1'] = task.run(rls)

    def run_2_task(self):
        T2 = self.loader.loaded_modules["T2"]
        task = T2()
        self.results['2'] = task.run()
    
    def run_3_task(self):
        T3 = self.loader.loaded_modules["T3"]
        task = T3()
        self.results['3'] = task.run()
    

    def run_all(self):
        print("=" * 50)
        print("ЗАПУСК ПРОГРАММЫ С 3 ЗАДАЧАМИ")
        print("=" * 50)

        self.run_1_task()
        self.run_2_task()
        self.run_3_task()

        print("\n" + "=" * 50)
        print("ВСЕ ЗАДАЧИ ВЫПОЛНЕНЫ")
        print("=" * 50)

        return self.results

if __name__ == "__main__":
    runner = ProgramRunner()
    final_results = runner.run_all()
    print(f"\nВыполнено задач: {len(final_results)}")
    for x, y in final_results.items():
        print(f"{x}: {y}\n\n")