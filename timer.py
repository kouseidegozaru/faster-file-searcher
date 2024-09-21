from datetime import datetime
def timer(func):
    def wrapper(*args, **kwargs):

        #開始時刻表示
        start_time = datetime.now()
        print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

        #関数実行
        result = func(*args, **kwargs)

        #終了時刻表示
        end_time = datetime.now()
        print(f"Ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

        #実行時間表示
        print(f"Total time taken: {(end_time - start_time).total_seconds()} seconds")

        return result
    
    return wrapper