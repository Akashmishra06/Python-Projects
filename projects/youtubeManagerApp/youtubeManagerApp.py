from youtubeManagerTools.youtubeManagerTools import ToolsForYoutubeManager

class YoutubeManagerApp:
    
    @staticmethod
    def main():
        videos = ToolsForYoutubeManager.load_data()

        while True:

            print("\n Youtube Manager | choose an option ")

            print("1. List favorite videos ")
            print("2. Add a YouTube video ")
            print("3. Update a YouTube video details ")
            print("4. Delete a YouTube video ")
            print("5. Exit the app")

            choice = input("Enter Your choice: ")

            if choice == '1':
                ToolsForYoutubeManager.list_all_videos(videos)

            elif choice == '2':
                ToolsForYoutubeManager.add_video(videos)

            elif choice == '3':
                ToolsForYoutubeManager.update_video(videos)

            elif choice == '4':
                ToolsForYoutubeManager.delete_video(videos)

            elif choice == '5':
                break
                
            else:
                print("Invalid choice")

if __name__ == "__main__":

    YoutubeManagerApp.main()
