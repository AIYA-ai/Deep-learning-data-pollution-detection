# -*- encoding:utf-8 -*-
from hashlib import md5
import pymysql
import os
import zipfile


class md5contrast():
    def __int__(self):
        super(md5contrast, self).__int__()

    def zipDir(self, dirpath):
        self.outFullName = dirpath + '.zip'
        if os.path.exists(self.outFullName) == False:
            zip = zipfile.ZipFile(self.outFullName, "w", zipfile.ZIP_DEFLATED)
            for path, dirnames, filenames in os.walk(dirpath):
                # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
                fpath = path.replace(dirpath, '')

                for filename in filenames:
                    zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
            zip.close()

    def getting(self, filepath, dataname):
        try:
            self.md = self.generate_file_md5value(filepath)
        except:
            self.zipDir(filepath)
            self.md = self.generate_file_md5value(self.outFullName)
        con = self.mysql_db()
        cur = con.cursor()
        try:
            sql = f"select md5 from all_table where data_name='{dataname}'"
            cur.execute(sql)
            result = cur.fetchone()
            if result[0] == self.md:
                return True
            else:
                return False

        except:
            pass

    def mysql_db(self):
        # 连接数据库肯定需要一些参数
        conn = pymysql.connect(
            host="106.12.144.39",
            port=3306,
            database="data_verification",
            charset="utf8",
            user="tourist",
            passwd="~!@#cxsys987",
            autocommit=True
        )
        return conn

    def generate_file_md5value(self, fpath):
        m = md5()
        # 需要使用二进制格式读取文件内容
        a_file = open(fpath, 'rb')
        m.update(a_file.read())
        a_file.close()
        return m.hexdigest()


if __name__ == "__main__":
    path = "F:\shuju\cifar-100-python.tar.gz"
    name = "cifar-100-python"
    d = md5contrast()
    d.getting(path, name)
