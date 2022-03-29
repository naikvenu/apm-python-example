import requests
 
# Change this APM Endpoint url
apm_upload_endpoint_url="https://<APM Endpoint obtained from OCI Console>/20200101/observations/public-span?dataFormat=zipkin&dataFormatVersion=2&dataKey=<Public APM Data Key obtained from OCI console>"
 
def http_transport(encoded_span):
      result = requests.post(
             #Construct a URL that communicate with Application Performance Monitoring
             apm_upload_endpoint_url,
             data=encoded_span,
             headers={'Content-Type': 'application/json'},
        )
      return result
