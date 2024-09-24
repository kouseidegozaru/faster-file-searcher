import os

def is_match(file_name, filter_options):
    # filter_optionsをセットに変換
    filter_set = set(filter_options)
    # 全てのフィルター条件を満たすか確認
    return filter_set.issubset(file_name)

def file_search(target_dir_path, *filter_options):
    try:
        #ディレクトリ下の情報を取得する
        with os.scandir(target_dir_path) as entries:
            for entry in entries:

                # フィルターを適用する
                if is_match(entry.name, filter_options):
                    yield entry.path  # ファイルパスを返す

                # サブディレクトリを探索する
                if entry.is_dir():
                    yield from file_search(entry.path, *filter_options)

    except PermissionError:
        pass
