import os
import time
import threading
import configparser


class Starter:
    """
    This Starter is helpful when you want to open many programs,
    like you want to use Windows Task Scheduler to start some programs,
    but you have many programs, so you should keep adding to scheduler,
    but if you use this script then you just setting the config once,
    then put this script to Windows Task Scheduler, it's done,
    and also this is easier to modify.
    """
    def __init__(self):
        result = self.init_config()
        self.start(result)

    @staticmethod
    def init_config():
        """
        To init the config file, and get the value of config.
        in setting.ini is look like this:
        [DEFAULT]
        FolderMode = False

        [PATH]
        FolderPath = path...
        Path = filePath... , filePath....

        FolderMode is to decide which mode you want, support two mode, in detail see below.
        FolderPath Use raw str, e.g. D:\PythonProject\Project1
        Path Use "," to split, Path e.g. D:\PythonProject\Project2\main.py , D:\PythonProject\Project3\main.py
        """
        config = configparser.ConfigParser()

        if not os.path.isfile('setting.ini'):
            config['DEFAULT']['FolderMode'] = False
            config['PATH'] = {
                'FolderPath': '',
                'Path': ''
            }
            with open('setting.ini', 'w') as configfile:
                config.write(configfile)

        config.read('setting.ini')
        return [config['DEFAULT']['FolderMode'], config['PATH']['FolderPath'], config['PATH']['Path']]

    def start(self, result):
        """
        Starter exec programs.
        :param result: The result value just the config value.
        """
        folderMode, folderPath, path = result

        if not folderPath and not path:
            raise ValueError

        if 'True' in folderMode:
            folderPath = self.convertPath(folderPath)
            files = os.listdir(folderPath)
            print(f'All files: {files}')
            for file in files:
                print(f'Open... {file}')
                thread = threading.Thread(target=self.execFile, args=(f'{folderPath}{file}',))
                thread.start()
                time.sleep(2)
        else:
            Paths = path.split(',')
            print(f'All Path: {Paths}')
            for path in Paths:
                path = self.convertPath(path)[:-1].strip()
                print(f'Open... {path}')
                thread = threading.Thread(target=self.execFile, args=(path,))
                thread.start()
                time.sleep(2)

        print('Open Done!')

    @staticmethod
    def execFile(filePath):
        """
        Exec programs.
        :param filePath: the programs path.
        """
        exec(open(filePath).read(), globals())

    @staticmethod
    def convertPath(path):
        """
        To convert the separator "\" to "/" and add the "/" to last str.
        Sometimes the path will not work in python,
        at you use the Windows Explorer's separator "\",
        i found the reason from stack overflow,
        title is Python subprocess filepath white spaces and famous...
        「 Backslashes in strings trigger escape characters 」 -Max Noel
        so i make the simple function to solve the problem.
        :param path: just the path.
        :rtype str:
        """
        if path[-1] is '/' or path[-1] is '\\':
            return path.replace('\\', '/')
        else:
            return path.replace('\\', '/') + '/'


if __name__ == '__main__':
    obj = Starter()
