import os

def is_match(file_name, *args):
    return all(map(lambda arg: arg in file_name, args))

def file_search(target_dir_path, *args):

    filter_options = args

    try:
        # os.scandirを使い、ファイルやディレクトリの情報をジェネレーターで得る
        with os.scandir(target_dir_path) as entries:
            for entry in entries:
                
                # フィルターを適用する
                if is_match(entry.name, *filter_options):
                    yield entry.path  # ファイルパスを返す
                
                # サブディレクトリを探索する
                if entry.is_dir():
                    # サブディレクトリに対して再帰処理を行う
                    yield from file_search(entry.path, *filter_options)

    except PermissionError:
        pass
