# python3-udfs-api

 Language: Python >= 3.6
 
# example

    def download():
        tool = UdfsDevTools.UdfsDevTools()
        url = tool.getDownloadUrl("uosAccount","secretKey", 10000,"QmPuzPAtLjRpJNHM5qbuShS2s1Etki92C3672JLt8oJiGg")
        conn = requests.get(url)

        with open('QmPuzPAtLjRpJNHM5qbuShS2s1Etki92C3672JLt8oJiGg', "wb") as code:
            code.write(conn.content)

    def upload():
        files = {'file': open('D:\\home\\1.mp4',
                              'rb')}
        tool = UdfsDevTools.UdfsDevTools()
        url = tool.getUploadUrl(10000,"secretKey","uosAccount","D:\\home\\1.mp4","")
        upload_res = requests.post(url,files=files)
        print upload_res
        
    def delete():
        tool = UdfsDevTools.UdfsDevTools()
        url = tool.deletefile("uosAccount","secretKey", 10000,"QmTLXPs77vn6ss268ghAUbnMFR12yzR5cHr3kud19SZWTs")
        conn = requests.delete(url)
        print(conn)
 
 # tips
   You can obtain the key and the uosAccount from the Ulord foundation 
