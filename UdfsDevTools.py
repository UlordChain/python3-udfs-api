import base64
import hashlib
import hmac
import os
import time
from hashlib import sha1

class UdfsDevTools():

    def GetFileMd5(self,filePath):
        if not os.path.isfile(filePath):
            return
        myhash = hashlib.md5()
        f = open(filePath, 'rb')
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()

    #expireSec:指定毫秒后过期时间
    #secretKey:秘钥,用于udfs访问,从udfs官方获取
    #uosAccount:uos账号
    #filePath:需要上传的文件路径
    #udfsCallbackUrl:回调url,udfs上传完毕后回调该url,将返回（文件id，哈希值，文件size），该参数可为空
    def getUploadUrl(self,expireSec, uosAccount,secretKey,  filePath, udfsCallbackUrl):
        fileName = os.path.basename(filePath);
        fileSize = str(os.path.getsize(filePath))
        md5 = self.GetFileMd5(filePath);
        expireTime = int(time.time())
        expireTime += expireSec;
        expireTime=str(expireTime)
        if udfsCallbackUrl == None or udfsCallbackUrl == "":
            json = "{\"ver\":0,\"expired\":" + expireTime + ",\"callback_url\":\"\",\"callback_body\":\"\",\"ext\":{\"file_name\":\"" + fileName + "\",\"size\":" + fileSize + ",\"md5\":\"" + md5 + "\"}}";
        else:
            json = "{\"ver\":0,\"expired\":" + expireTime + ",\"callback_url\":\"" + udfsCallbackUrl + "\",\"callback_body\":\"{\\\"file_size\\\":\\\"$(size)\\\",\\\"hash\\\":\\\"$(hash)\\\",\\\"file_id\\\":0}\",\"ext\":{\"file_name\":\"" + fileName + "\",\"size\":" + fileSize + ",\"md5\":\"" + md5 + "\"}}";
        try :
            textByte = json.encode(encoding="utf-8")
            encodedPolicy = base64.urlsafe_b64encode(textByte)
            my_sign = hmac.new(secretKey.encode(encoding="utf-8"), encodedPolicy, sha1).digest()
            encodeSign = base64.urlsafe_b64encode(my_sign)
        except Exception as ex:
            raise Exception("构建上传链接出错" + ex.toString())
        token = uosAccount + ":" + str(encodeSign, encoding="utf-8") + ":" + str(encodedPolicy, encoding="utf-8")
        uploadUrl = 'http://api.udfs.one:15001/api/v0/add' + "?token=" + token
        return uploadUrl;

    #uosAccount:uos账号
    #secretKey:秘钥,用于udfs访问,从udfs官方获取
    #expireSec:指定毫秒后过期时间
    #hashvalue:要下载的对象哈希值
    def getDownloadUrl(self,uosAccount,secretKey,expireSec,hashvalue):
        expireTime = int(time.time())
        expireTime += expireSec;
        json = "{\"ver\":0,\"expired\": "+str(expireTime)+",\"ext\":{}}"
        try :
            textByte = json.encode(encoding="utf-8")
            encodedPolicy = base64.urlsafe_b64encode(textByte)
            my_sign = hmac.new(secretKey.encode(encoding="utf-8"), encodedPolicy, sha1).digest()
            encodeSign = base64.urlsafe_b64encode(my_sign)
        except Exception as ex:
            raise Exception("构建下载链接出错" + ex.toString())
        token = uosAccount + ":" + str(encodeSign, encoding="utf-8") + ":" + str(encodedPolicy, encoding="utf-8")
        downloadUrl = 'http://api.udfs.one:15001/api/v0/cat/' + hashvalue + "?token=" + token
        return downloadUrl

    def deletefile(self,uosAccount,secretKey,expireSec,hashvalue):
        expireTime = int(time.time())
        expireTime += expireSec;
        json = "{\"ver\":0,\"expired\": "+str(expireTime)+",\"ext\":{}}"
        try :
            textByte = json.encode(encoding="utf-8")
            encodedPolicy = base64.urlsafe_b64encode(textByte)
            my_sign = hmac.new(secretKey.encode(encoding="utf-8"), encodedPolicy, sha1).digest()
            encodeSign = base64.urlsafe_b64encode(my_sign)
        except Exception as ex:
            raise Exception("构建删除链接出错" + ex.toString())
        token = uosAccount + ":" + str(encodeSign, encoding="utf-8") + ":" + str(encodedPolicy, encoding="utf-8")
        deleteUrl = 'http://api.udfs.one:15001/api/v0/delete/' + hashvalue + "?token=" + token
        return deleteUrl




