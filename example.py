import UdfsDevTools
import requests

def delete():
    tool = UdfsDevTools.UdfsDevTools()
    url = tool.deletefile("uosAccount","secretKey", 10000,"QmTLXPs77vn6ss268ghAUbnMFR12yzR5cHr3kud19SZWTs")
    conn = requests.delete(url)
    print(conn)

def download():
    tool = UdfsDevTools.UdfsDevTools()
    url = tool.getDownloadUrl("uosAccount","secretKey", 10000,"QmTLXPs77vn6ss268ghAUbnMFR12yzR5cHr3kud19SZWTs")
    conn = requests.get(url)

    with open('QmTLXPs77vn6ss268ghAUbnMFR12yzR5cHr3kud19SZWTs', "wb") as code:
        code.write(conn.content)
def upload():
    files = {'file': open('D:\\home\\1.mp4','rb')}
    tool = UdfsDevTools.UdfsDevTools()
    url = tool.getUploadUrl(10000,"uosAccount","secretKey","D:\\home\\1.mp4","")
    upload_res = requests.post(url,files=files)
    print(upload_res)
upload()
download()
delete()
download()