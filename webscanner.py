from flask import Flask, render_template, request
import requests
import ssl
import socket
from urllib.parse import urlparse
from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

app = Flask(__name__)

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

session = requests.Session()
session.mount("https://", SSLAdapter())

def test_sql_injection(url):
    sqli_payloads = ["' OR 1=1 --", "' OR 'a'='a", '" OR "a"="a']
    for payload in sqli_payloads:
        try:
            response = session.get(url, params={"search": payload})
            if "error" in response.text or "syntax" in response.text:
                return f"Potential SQL Injection detected in {url}"
        except requests.exceptions.RequestException as e:
            return f"Error testing SQLi: {e}"
    return None

def test_xss(url):
    xss_payloads = ["<script>alert('XSS')</script>", "<img src='x' onerror='alert(1)'>"]
    for payload in xss_payloads:
        try:
            response = session.get(url, params={"search": payload})
            if payload in response.text:
                return f"Potential XSS vulnerability detected in {url}"
        except requests.exceptions.RequestException as e:
            return f"Error testing XSS: {e}"
    return None

def check_security_headers(url):
    response = requests.get(url)
    headers = response.headers
    security_headers = ['Strict-Transport-Security', 'X-Content-Type-Options', 'Content-Security-Policy', 'X-Frame-Options']
    return {header: headers.get(header, 'Not found') for header in security_headers}

def check_ssl_cert(url):
    hostname = urlparse(url).hostname
    try:
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        conn.connect((hostname, 443))
        cert = conn.getpeercert()
        return f"SSL certificate valid for {hostname}"
    except Exception as e:
        return f"SSL certificate check failed: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        sql_injection_result = test_sql_injection(url)
        xss_result = test_xss(url)
        headers = check_security_headers(url)
        ssl_cert = check_ssl_cert(url)

        # You can add additional functionality here for open ports, status code, etc.
        open_ports = "Not implemented yet"  # Replace with actual port checking logic
        status_code = requests.get(url).status_code

        return render_template('index.html', url=url, 
                               sql_injection_result=sql_injection_result, 
                               xss_result=xss_result, 
                               headers=headers, 
                               ssl_cert=ssl_cert,
                               open_ports=open_ports, 
                               status_code=status_code)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
