import subprocess
from log import logger


class ShellExecutor(object):

    @staticmethod
    def execute_command(cmd):
        """
        :param cmd: Command to execute
        :return:
        """
        if not cmd:
            cmd = []
        logger.info("executing: {}".format(cmd))
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        # logger.info("stdout: {}\nstderr: {}".format(stdout, stderr))
        return stdout, stderr

    def apt_install_pkg(self, pkg_name, parameters=''):
        cmd = "apt-get install {} {}".format(parameters, pkg_name)
        logger.info('installing {}'.format(pkg_name))
        return self.execute_command(cmd)

    def apt_purge_pkg(self, pkg_name):
        cmd = "apt-get purge -y {}".format(pkg_name)
        logger.info('installing {}'.format(pkg_name))
        return self.execute_command(cmd)
