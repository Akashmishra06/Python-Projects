import json


class ToolsForYoutubeManager:

    def load_data():

        try:

            with open('youtube.txt', 'r') as file:
                return json.load(file)
            
        except FileNotFoundError:

            return []
            

    def save_data_helper(videos):

        with open('youtube.txt', 'w') as file:
            json.dump(videos, file)


    def list_all_videos(videos):

        print("\n")
        print("*" * 70)

        for index, video in enumerate(videos, start=1):

            print(f"{index}. {video['name']}, Duration: {video['time']} ")

        print("\n")
        print("*" * 70)


    def add_video(videos):

        name = input("Enter video name: ")
        time = input("Enter video time: ")
        videos.append({'name':name, 'time': time})
        ToolsForYoutubeManager.save_data_helper(videos)


    def update_video(videos):

        ToolsForYoutubeManager.list_all_videos(videos)
        index = int(input("Enter the videp the number too update"))

        if 1<= index <= len(videos):

            name = input("Enter thhe new video name")
            time = input("Enter the new video time")
            videos[index-1] = {'name':name, 'time':time}
            ToolsForYoutubeManager.save_data_helper(videos)

        else:

            print("Invalidd syntac selected")


    def delete_video(videos):

        ToolsForYoutubeManager.list_all_videos(videos)
        index = int(input("Enter the vidoe number to be deleted"))

        if 1<= index <= len(videos):

            del videos[index-1]
            ToolsForYoutubeManager.save_data_helper(videos)

        else:

            print("Invalid vedio index selected")


if __name__ == "__main__":
    pass