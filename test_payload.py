from os import system

HOST = 'example-service-name-yyrg.onrender.com'  # Localhost IP address
PORT = '443'  # Port number to connect to

data = f'''POST https://{HOST}/gimme:{PORT}/ HTTP/1.1
Host: {HOST}:{PORT}
Content-Length: 20
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Accept: */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36

{'{"helow": "roworor"}'} '''

with open("request.txt", "w") as file:
    file.write(data)

system("cat request.txt")
system("cat request.txt | openssl s_client -connect example-service-name-yyrg.onrender.com:443")
# system("touch request.txt")
# system("cat request.txt | ncat --ssl example.com 443")
