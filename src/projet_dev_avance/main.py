from projet_dev_avance.module1 import hello_module1
from projet_dev_avance.module2 import add
from projet_dev_avance.utilitaires.texte import to_upper_case
from projet_dev_avance.utilitaires.maths import multiply

if __name__ == '__main__':
    print(hello_module1())
    print(("2+3=", add(2, 3)))
    print("multiply(2,3)=", multiply(2, 3))
    print(to_upper_case(hello_module1()))
    