from fileFinder import file_search
from timer import timer

@timer
def main():
    # target_dir_path = input('検索したいディレクトリのパスを入力して下さい。: ')
    # target_file_names = input('検索したいファイル名を入力して下さい。 スペース区切り: ').split()
    target_dir_path = 'C:\\Users\\mfh077_user.MEFUREDMN\\Desktop'
    target_file_names = '.txt'
    
    #高階関数を受け取る
    matched_path_list = list(file_search(target_dir_path, *target_file_names))
    # #ファイルパスを出力
    # for path in matched_path_list:print(path)

    print('検索結果: ', len(matched_path_list), ' 件')


if __name__ == '__main__':
    main()