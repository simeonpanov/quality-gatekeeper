#!/bin/bash

if [ -z "$1" ]; then
  TARGET_URL="https://jsonplaceholder.typicode.com"
  echo "No target URL provided, using default: $TARGET_URL"
else
  TARGET_URL=$1
fi

REPORT_PATH=reports/security/zap_report.html
mkdir -p $(dirname "$REPORT_PATH")

/usr/local/bin/zap.sh -daemon -port 8090 -host 127.0.0.1 -config api.disablekey=true &
ZAP_PID=$!

echo "Starting ZAP daemon, waiting for startup..."
sleep 20

echo "Running baseline scan on $TARGET_URL ..."
./scripts/zap-baseline.py -t "$TARGET_URL" -r "$REPORT_PATH"
SCAN_EXIT=$?

if [ $SCAN_EXIT -ne 0 ]; then
  echo "Baseline scan failed with exit code $SCAN_EXIT"
  kill $ZAP_PID
  exit $SCAN_EXIT
fi

curl "http://127.0.0.1:8090/JSON/core/action/shutdown/"

echo "ZAP scan complete. Report saved to $REPORT_PATH"
