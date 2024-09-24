import datetime

class timer:

    def __init__(self):
        amount_of_time_seconds = 0

    def timecount(self,func):
        def wrapper(*args, **kwargs):
            #開始時刻
            start_time = datetime.datetime.now()

            #関数実行
            result = func(*args, **kwargs)

            #終了時刻
            end_time = datetime.datetime.now()

            #実行時間
            self.amount_of_time_seconds = (end_time - start_time).total_seconds()

            return result
        
        def show_time(self):
            print(f"Total time taken: {self.amount_of_time_seconds} seconds")
