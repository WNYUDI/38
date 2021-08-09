import os
import platform
import subprocess
import sys
import threading


class ProcessService:

    __encoding = None

    __process = None

    __read_bytes = None

    __error_bytes = None

    when_read = None

    when_error = None

    when_exec = None

    def __init__(self, encoding=None):
        if encoding == None:
            self.__encoding = 'GBK' if platform.system() == 'Windows' else 'UTF-8'

    def __del__(self):
        self.close()

    def start(self):
        self.__process = subprocess.Popen('cmd' if platform.system() == 'Windows' else 'sh' if platform.system(
        ) == 'Linux' else None, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        def out_runnable():
            try:
                while self.__process.poll() == None:
                    content_bytes = self.__process.stdout.read(1)
                    if content_bytes != None and len(content_bytes) > 0:
                        if self.when_read != None:
                            if self.__read_bytes == None:
                                self.__read_bytes = content_bytes
                            else:
                                self.__read_bytes += content_bytes
                            content = None
                            try:
                                content = self.__read_bytes.decode(
                                    encoding=self.__encoding)
                            except UnicodeDecodeError as e:
                                pass
                            if content != None and self.when_read(content) == True:
                                self.__read_bytes = None
            except Exception:
                pass

        def err_runnable():
            try:
                while self.__process.poll() == None:
                    content_bytes = self.__process.stderr.read(1)
                    if content_bytes != None and len(content_bytes) > 0:
                        if self.when_error != None:
                            if self.__error_bytes == None:
                                self.__error_bytes = content_bytes
                            else:
                                self.__error_bytes += content_bytes
                            if self.when_error(self.__error_bytes.decode(encoding=self.__encoding)) == True:
                                self.__read_bytes = None
            except Exception:
                pass

        def alive_runnable():
            self.__process.wait()
            self.close()
        threading.Thread(target=out_runnable).start()
        threading.Thread(target=err_runnable).start()
        threading.Thread(target=alive_runnable).start()

    def is_alive(self):
        return self.__process != None

    def exec(self, cmd, prefix='', suffix='\n'):
        cmd2 = (prefix + cmd + suffix)
        if self.when_exec != None:
            if self.when_exec(cmd2) != True:
                return
        self.__process.stdin.write(cmd2.encode())
        self.__process.stdin.flush()

    def close(self):
        if self.is_alive():
            self.__process.kill()
            self.__process = None


when_read = None

when_error = None

when_exec = None


def start():
    process_service = ProcessService()
    process_service.when_read = when_read
    process_service.when_error = when_error
    process_service.when_exec = when_exec
    process_service.start()
    return process_service
