import json
import boto3
import os
import sys
import yfinance as yf

tickers = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
start_date = '2021-11-30'
end_date = '2021-12-01'
time_interval = '5m'

def lambda_handler(event, context):
    kinesis = boto3.client('kinesis', 'us-east-1')
    for ticker in tickers:
        data = yf.download(ticker, start = start_date, end = end_date, interval = time_interval)
        for datetime, value in data.iterrows():
            record = {'high': value['High'],
                      'low': value['Low'],
                      'ts': str(datetime),
                      'name': ticker}
            as_jsonstr = json.dumps(record, separators=(',',':')) + '\n'
            kinesis.put_record(
                StreamName='sta9760_stream1',
                Data=as_jsonstr.encode('utf-8'),
                PartitionKey='partitionkey')
                
    return {
        'statusCode': 200,
        'body': json.dumps('Fin.')
    }
