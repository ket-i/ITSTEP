import json

def display_file(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)


def read_file_content(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            return content


def update_file_content(file_path, new_content):
        with open(file_address, 'w') as file:
            file.write(new_content)



def write_dict_to_file(file_path, new_data):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        existing_data.extend(new_data)

        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=2)

        print("ფაილი განახლდა")
 


file_address = 'E:/IT_academy/New folder'


display_file(file_path)


content = read_file_content(file_path)

print(content)


new_content = "ფაილის განახლება"
update_file_content(file_path, new_content)


new_data = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]
write_dict_to_file(file_path, new_data)