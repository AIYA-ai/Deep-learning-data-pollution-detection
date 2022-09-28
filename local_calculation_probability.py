import time
import gzip
import os
import tarfile
import zipfile
import rarfile


class localfile():
    def __int__(self):
        super(localfile, self).__int__()

    def un_gz(self, file_name):
        f_name = file_name.replace(".gz", "")
        g_file = gzip.GzipFile(file_name)
        open(f_name, "w+").write(g_file.read())
        g_file.close()

        # tar

    def un_tar(self, file_name):
        tar = tarfile.open(file_name)
        names = tar.getnames()
        if os.path.isdir(file_name):
            pass
        else:
            os.mkdir(file_name)
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
        rar = rarfile.RarFile(file_name)
        if os.path.isdir(file_name):
            pass
        else:
            os.mkdir(file_name)
        os.chdir(file_name)
        rar.extractall()
        rar.close()

    def infomation(self, path):
        self.timedict = {}
        self.path = path
        self.xunhuan(self.path)
        allnumber = 0
        shuliang = 0
        gailv = 0
        try:
            for i in self.timedict:
                allnumber += self.timedict[i]
                shuliang += 1
            for i in self.timedict:
                for j in self.timedict:
                    if i != j:
                        if self.timedict[i] > self.timedict[j]:
                            gailv += 1 - self.timedict[j] / self.timedict[i]
                        else:
                            gailv += 1 - self.timedict[i] / self.timedict[j]
            if (shuliang - 1) == 0:
                return 0
            else:
                return gailv / (shuliang * (shuliang - 1))
        except:
            return 0

    def formatTime(self, atime):
        return time.strftime("%Y-%m-%d", time.localtime(atime))

    def xunhuan(self, path):
        if not os.path.isdir(path):
            new_path = path
            if 'zip' in path:
                new_path = path[0:len(path) - 4]
                if os.path.exists(new_path) == 0:
                    self.un_zip(path, new_path)
            elif 'gz' in path:
                if 'tar' in path:
                    new_path = path[0:len(path) - 7]
                if os.path.exists(new_path) == 0:
                    self.un_gz(new_path)
            elif 'tar' in path:
                new_path = path[0:len(path) - 4]
                if os.path.exists(new_path) == 0:
                    self.un_tar(new_path)
            elif 'rar' in path:
                new_path = path[0:len(path) - 4]
                if os.path.exists(new_path) == 0:
                    self.un_rar(new_path)

            if new_path != path:
                self.infomation(new_path)
            else:
                return 0
        else:
            files = os.listdir(path)
            for file in files:
                if os.path.isdir(path + '/' + file):
                    self.xunhuan(path + '/' + file)
                else:
                    self.fileinfo = os.stat(path + '/' + file)
                    try:
                        self.timedict[self.formatTime(self.fileinfo.st_mtime)] += 1
                    except:
                        self.timedict[self.formatTime(self.fileinfo.st_mtime)] = 1


if __name__ == '__main__':
    d = localfile()
    path = r'F:\shuju\archive (2)'
    d.infomation(path)
