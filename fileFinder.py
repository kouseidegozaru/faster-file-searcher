import os
import itertools

def file_search(target_dir_path, *args):
    target_file_names = args
    try:
        all_file_list = os.listdir(target_dir_path)
    except PermissionError:
        return

    # ファイル名に条件が含まれるファイルのパスを出力
    match_name_list = filter(
        lambda file: all(cond in file for cond in target_file_names),
        all_file_list
    )
    match_path_list = list(map(lambda file: os.path.join(target_dir_path, file), match_name_list))

    # サブディレクトリを再帰的に検索
    dir_path_list = filter(
        lambda file: os.path.isdir(os.path.join(target_dir_path, file)),
        all_file_list
    )
    sub_match_path_list = list(itertools.chain.from_iterable(map(lambda dir_path: file_search(os.path.join(target_dir_path, dir_path), *args), dir_path_list)))

    # ファイル名に条件が含まれるファイルのパスを列挙
    return list(itertools.chain(match_path_list,sub_match_path_list))


