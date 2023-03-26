from apitools.python.other import greeting_in_other
import apitools.python.tests.functions as func
import apitools

if __name__ == "__main__":
    print("msg from greeting in other function ---" + greeting_in_other())
    print("msg from greeting function --- " + func.greeting())
    print("other way to call greeting fucntion " + apitools.python.tests.functions.greeting())
