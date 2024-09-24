import os
from time_counter import timer

def is_match(file_name, filter_options):
    # filter_optionsをセットに変換
    filter_set = set(filter_options)
    # 全てのフィルター条件を満たすか確認
    return filter_set.issubset(file_name)

def file_search(target_dir_path, *filter_options):

    match_time = timer()
    scan_time = timer()

    # ディレクトリ内のエントリーを非同期でスキャンするジェネレーター関数
    def scan_dir(target_dir_path):
        try:
            # ディレクトリのスキャンをタイミング計測
            @scan_time.timecount
            def scan():
                return os.scandir(target_dir_path)

            # ディレクトリ内のエントリーをジェネレーターとして返す
            for entry in scan():
                yield entry

        except PermissionError:
            # アクセス許可がない場合はスキップ
            pass

    # 内部探索関数
    def inner(target_dir_path, *filter_options):
        for entry in scan_dir(target_dir_path):

            # フィルタに一致するかの判定をタイミング計測
            @match_time.timecount
            def match():
                if is_match(entry.name, filter_options):
                    yield entry.path  # 一致したファイルパスを返す

            # 一致する場合のみyield
            yield from match()

            # サブディレクトリがあれば再帰的に探索
            if entry.is_dir(follow_symlinks=False):
                yield from inner(entry.path, *filter_options)

    # 最初のディレクトリから探索を開始
    yield from inner(target_dir_path, *filter_options)

    # 結果の時間を表示
    scan_time.show_time()
    match_time.show_time()
