import csv
from datetime import datetime


class CSVLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file = 'path_to_your_log_file.csv'  # 로그 파일 경로를 지정하세요.

    def __call__(self, request):
        response = self.get_response(request)

        with open(self.log_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), request.method, request.path])

        return response
