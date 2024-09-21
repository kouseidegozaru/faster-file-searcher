from fileFinder import file_search
from timer import timer

@timer
def main():
    # target_dir_path = input('検索したいディレクトリのパスを入力して下さい。: ')
    # target_file_names = input('検索したいファイル名を入力して下さい。 スペース区切り: ').split()
    target_dir_path = 'C:\\Users\\mfh077_user.MEFUREDMN\\Desktop'
    target_file_names = '.txt'
    
    file_search(target_dir_path, *target_file_names)

if __name__ == '__main__':
    main()