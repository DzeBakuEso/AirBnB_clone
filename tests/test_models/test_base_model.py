#!/usr/bin/python3

from models.base_model import BaseModel

def test_base_model():
    # here we created a new BaseModel instance
    my_model = BaseModel()

    # Here we add the attriutes
    my_model.name = "My First model"
    my_model.my_number = 89

    # We print the model
    print(my_model)  # Test __str__

    # here we call, save and print agian
    my-model.save()
    print(my_model)  # Test updated_at change

    # we get the dict repres and print it
    my_model_dict = my_model.to_dict()
    print(my_model_dict)

    # here we print JSON formatted values
    print("JSON of my_model:")
    for key, value in my_model_dict.items():
        print(f"\t{key}: ({type(value)}) - {value}")

if __name__ == "__main__":
    test_base_model()
