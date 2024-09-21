import os
import itertools

def is_match(file_name, *args):
    return all(cond in file_name for cond in args)

def convert_path(dir_path, file_name):
    return os.path.join(dir_path, file_name)

def file_search(target_dir_path, *args):

    # 抽出条件
    filter_options = args

    # ディレクトリ内の全ファイル名を抽出
    try:
        all_file_names = os.listdir(target_dir_path)
    # アクセス権限がなければ終了
    except PermissionError:
        return


    # ファイル名に条件が含まれるファイル名を抽出
    matched_file_names = filter(lambda file: is_match(file, *filter_options),all_file_names)
    # ファイル名をファイルパスに変換
    matched_file_paths = map(lambda file: convert_path(target_dir_path, file), matched_file_names)


    # フルパスに変換
    all_paths = map(lambda file: convert_path(target_dir_path, file), all_file_names)
    # ディレクトリのみを抽出
    dir_paths = filter(lambda path: os.path.isdir(path), all_paths)


    # ディレクトリを再帰的に探索
    sub_matched_paths_result = map(lambda dir_path: file_search(dir_path, *args), dir_paths)
    # ディレクトリ下の条件が含まれるファイルのパスを列挙
    sub_matched_file_paths = itertools.chain.from_iterable(sub_matched_paths_result)
    # ファイルとディレクトリ下の条件が含まれるファイルのパスを列挙
    all_matched_paths = itertools.chain(matched_file_paths, sub_matched_file_paths)

    return all_matched_paths