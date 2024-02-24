#TASK 1
import json
import pickle

# def save_object(obj, filename):
#     try:
#         with open(filename, 'w') as json_file:
#             json.dump(obj, json_file)
#         print("ობიექტი შევინახეთ სერიალიზაციით.")
#     except Exception as e:
#         print(f"ვერ მოხარხდა ობიქეტის შენახვა JSON -ით: {e}")
#         try:
#             with open(filename, 'wb') as pickle_file:
#                 pickle.dump(obj, pickle_file)
#             print("ობიქტის შენახვამოხდა pickle სერიალიზაციით.")
#         except Exception as e:
            
#             print("ობიექტის შენახვა pickle სერიალიზაციით ვერ მოხდა.")


# my_object = {'key': 'value'}
# save_object(my_object, 'my_file.json')

#TASK 2
# def load_object(filename):
#     try:
#         with open(filename, 'r') as json_file:
#             data = json.load(json_file)
#         print("ობიექტი ჩაიტვირთდა JSON დესერიალიზაციით:")
#         print(data)
#     except Exception as json_error:
#         print(f"დაფეილდა ობიექტის ჩატვირთვა: {json_error}")
#         try:
#             with open(filename, 'rb') as pickle_file:
#                 data = pickle.load(pickle_file)
#             print("ობიექტი ჩაიტვირთდა pickle დესერიალიზაციით:")
#             print(data)
#         except Exception as pickle_error:
#             print(f"დაფეილდა ობიექტის ჩატვირთვა pickle-ით: {pickle_error}")

# load_object('my_file.json') 

#TASK 3
import dill
def save_object(obj, filename):
    try:
        with open(filename, 'w') as json_file:
            json.dump(obj, json_file)
        print("ობიექტი შევინახეთ სერიალიზაციით.")
    except Exception as json_error:
        print(f"ვერ მოხარხდა ობიქეტის შენახვა JSON-ით: {json_error}")
        try:
            with open(filename, 'wb') as dill_file:
                dill.dump(obj, dill_file)
            print("ობიექტი შევინახეთ  dill სერიალიზაციით.")
        except Exception as dill_error:
            print(f"ვერ მოხარხდა ობიქეტის შენახვა dill-ით: {dill_error}")
            print("Object serialization failed.")

def load_object(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        print("ობიექტი ჩაიტვირთდა JSON დესერიალიზაციით:")
        print(data)
    except Exception as json_error:
        print(f"ვერ მოხარხდა ობიქეტის შენახვა JSON-ით: {json_error}")
        try:
            with open(filename, 'rb') as dill_file:
                data = dill.load(dill_file)
            print("ობიექტი ჩაიტვირთდა dill დესერიალიზაციით:")
            print(data)
        except Exception as dill_error:
            print(f"ვერ მოხარხდა ობიქეტის ჩატვირთვა: {dill_error}")

#მაგალითად
my_lambda = lambda x: x ** 2


save_object(my_lambda, 'my_lambda.dill')
load_object('my_lambda.dill')