# x = "Hello"
# y = enumerate(x)
# print(list(y))

# # file = open('test.py')
# file = open('test.py', 'w')


# # file 

# file = open('youtube.txt', 'w')

# try:
#     file.write('write the code')
# finally:
#     file.close()


# with open('youtube.txt', 'w') as file:
#     file.write('cha aur code')



import json



def load_Data():
    
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_data_Helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)



def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. ")
        

def Add_videos():
    pass

def Update_videos():
    pass

def Delete_videos():
    pass



def main():

    videos = load_Data()

    while True:

        print('\n Youtube Manager ')
        print('1. List all Youtube videos: ')
        print('2. Add a Youtube video ')
        print('3. Update a Youtube video details: ')
        print('4. Delete a Youtube video: ')
        print('5. Exit the app ')

        choice = input("Enter Your choice")


        match choice:

            case '1':
                list_all_videos(videos)

            case '2':
                Add_videos(videos)

            case '3':
                Update_videos(videos)

            case '4':
                Delete_videos(videos)

            case '5':
                break

            case _:
                print("InvaldChoice")



if __name__ == "__main__":
    main()