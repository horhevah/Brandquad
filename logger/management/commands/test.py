from datetime import datetime

import requests

from ...models import ApacheLog

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Test'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='?', type=str,
                            help='test', default='swda')

    def handle(self, *args, **kwargs):
        url = kwargs['url']
        with requests.get(url=url, stream=True) as r:
            for chunk in r.iter_lines():
                line = str(chunk, 'utf-8')
                if line:
                    values = line.split()
                    ip_address = values[0]
                    date_str = values[3][1:] + ' ' + values[4][:-1]
                    date = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')
                    method = values[5][1:]
                    url = values[6]
                    status_code = values[8]
                    size = values[9]
                    log = ApacheLog(ip_address=ip_address,data_time=date,method=method,url=url,status_code=status_code,size=size)
                    log.save()
                    print(log.pk)




