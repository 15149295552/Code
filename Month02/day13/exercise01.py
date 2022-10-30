# "我过去"
import module_exercise

print(module_exercise.data)
module_exercise.func01()
m = module_exercise.MyClass()
m.func02()

# "你过来"
from module_exercise import *

print(data)
func01()
m = MyClass()
m.func02()