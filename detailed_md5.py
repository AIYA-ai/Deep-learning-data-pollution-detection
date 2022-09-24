import gzip
import os
import tarfile
import zipfile
import pymysql
import rarfile
from hashlib import md5


class confirmation():
    def inspect(self, localpath, dataset_Nam):
        self._localpath = localpath
        self._dataset_Name = dataset_Nam
        new_path = localpath
        if 'zip' in self._localpath:
            new_path = self._localpath[0:len(self._localpath) - 4]
            if os.path.exists(new_path) == 0:
                self.un_zip(self._localpath, new_path)
        elif 'gz' in self._localpath:
            if 'tar' in self._localpath:
                new_path = self._localpath[0:len(self._localpath) - 7]
            if os.path.exists(new_path) == 0:
                self.un_gz(self._localpath)
        elif 'tar' in self._localpath:
            new_path = self._localpath[0:len(self._localpath) - 4]
            if os.path.exists(new_path) == 0:
                self.un_tar(self._localpath)
        elif 'rar' in self._localpath:
            new_path = self._localpath[0:len(self._localpath) - 4]
            if os.path.exists(new_path) == 0:
                self.un_rar(self._localpath)
        self.save_path = new_path
        for i in range(len(self.save_path)):
            if '/' == self.save_path[i]:
                jl = i

        self.wrrong = []
        self.xunhuan(self.save_path)
        return self.wrrong

    # gz
    def un_gz(self, file_name):
        """ungz zip file"""
        f_name = file_name.replace(".gz", "")
        # 获取文件的名称，去掉
        g_file = gzip.GzipFile(file_name)
        # 创建gzip对象
        open(f_name, "w+").write(g_file.read())
        # gzip对象用read()打开后，写入open()建立的文件里。
        g_file.close()
        # 关闭gzip对象

    # tar
    def un_tar(self, file_name):
        # untar zip file"""
        tar = tarfile.open(file_name)
        names = tar.getnames()
        if os.path.isdir(file_name):
            pass
        else:
            os.mkdir(file_name)
        # 因为解压后是很多文件，预先建立同名目录
        for name in names:
            tar.extract(name, file_name)
        tar.close()

    # zip
    def un_zip(self, file_name, new_file):
        """unzip zip file"""
        zip_file = zipfile.ZipFile(file_name)
        if os.path.isdir(file_name):
            pass
        else:
            os.mkdir(new_file)
        for names in zip_file.namelist():
            zip_file.extract(names, new_file)
        zip_file.close()

    # rar
    def un_rar(self, file_name):
        """unrar zip file"""
        rar = rarfile.RarFile(file_name)  # 待解压文件
        if os.path.isdir(file_name):
            pass
        else:
            os.mkdir(file_name)
        os.chdir(file_name)
        rar.extractall()  # 解压指定目录
        rar.close()

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

    def create_md5(self, path):
        m = md5()
        # 需要使用二进制格式读取文件内容
        a_file = open(path, 'rb')
        m.update(a_file.read())
        a_file.close()
        return m.hexdigest()

    def xunhuan(self, new_path):

        frompath = new_path[len(self.save_path) + 1:len(new_path)]
        if not os.path.isdir(new_path):

            md55 = self.create_md5(new_path)
            con = self.mysql_db()
            cur = con.cursor()

            sql = f"select md5 from detailed_table where name='{new_path}' and frompath='{frompath}' and belong='{self._dataset_Name}'"
            cur.execute(sql)
            result = cur.fetchone()
            try:
                if md55 != result[0]:
                    self.wrrong.append(new_path)
            except:
                self.wrrong.append(new_path)
        else:

            files = os.listdir(new_path)
            for file in files:

                if os.path.isdir(new_path + '/' + file):
                    self.xunhuan(new_path + '/' + file)
                else:
                    md55 = self.create_md5(new_path + '/' + file)
                    con = self.mysql_db()
                    cur = con.cursor()
                    sql = f"select md5 from detailed_table where name='{file}' and frompath='{frompath}' and belong='{self._dataset_Name}'"
                    cur.execute(sql)
                    result = cur.fetchone()
                    try:
                        if md55 != result[0]:
                            self.wrrong.append(new_path + '/' + file)
                    except:
                        self.wrrong.append(new_path + '/' + file)
