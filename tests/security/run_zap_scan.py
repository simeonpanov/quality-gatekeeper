from zapv2 import ZAPv2
import time
import sys

target = 'https://jsonplaceholder.typicode.com'
zap = ZAPv2(apikey='', proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

print('Starting ZAP scan...')

# Access target to populate sites tree
zap.urlopen(target)
time.sleep(2)

print('Spidering target...')
scan_id = zap.spider.scan(target)
while int(zap.spider.status(scan_id)) < 100:
    print('Spider progress %: ' + zap.spider.status(scan_id))
    time.sleep(2)

print('Spider complete.')

print('Starting active scan...')
scan_id = zap.ascan.scan(target)
while int(zap.ascan.status(scan_id)) < 100:
    print('Active scan progress %: ' + zap.ascan.status(scan_id))
    time.sleep(5)

print('Active scan complete.')

alerts = zap.core.alerts()
print('Alerts summary:')
for alert in alerts:
    print(f"- {alert['alert']} (Risk: {alert['risk']}) on {alert['url']}")


with open('reports/security/zap_full_report.html', 'w') as f:
    f.write(zap.core.htmlreport())

print('Report saved to reports/security/zap_full_report.html')
