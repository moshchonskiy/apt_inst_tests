import pytest
import testinfra


class TestAptGetInstall:

    @pytest.mark.positive
    def test_apt_get_install_success(self, shell_executor, remove_rolldice, host):
        """Check apt-get install successfully installs a package

           Pre-conditions
               1. Fully uninstall a package

           Scenario:
               1. Install a package using apt-get install
               2. Check if it was installed
        """
        pkg_name = "rolldice"
        shell_executor.apt_install_pkg(pkg_name)
        pkg = host.package(pkg_name)
        assert pkg.is_installed, 'the specified pkg is not installed: {}'.format(pkg_name)

    @pytest.mark.positive
    def test_apt_get_install_version(self, shell_executor, remove_rolldice, host):
        """Check apt-get install successfully installs a package with specified version

           Pre-conditions
               1. Fully uninstall a package

           Scenario:
               1. Install a specified version of a package using apt-get install
               2. Check if it was installed
        """
        version = "1.14-2"
        pkg_name = "rolldice"
        pkg_version = "{}={}".format(pkg_name, version)
        shell_executor.apt_install_pkg(pkg_version)
        pkg = host.package(pkg_name)
        assert version == pkg.version, 'the specified version is not equal to installed: {} != {}'.format(
            version, pkg.version)

    @pytest.mark.negative
    def test_apt_get_install_wrong_pkg_name(self, shell_executor, remove_rolldice, host):
        """Check apt-get install can not install a package with wrong package name

           Pre-conditions
               1. Fully uninstall a package

           Scenario:
               1. Try to install a package using apt-get install
               2. Check that apt-get returns an error
               3. Check if it was not installed
        """
        pkg_name = "rolldice"
        _, error = shell_executor.apt_install_pkg(pkg_name[:7])
        assert error, 'should return an error: Unable to locate package {}'.format(pkg_name[:7])
        pkg = host.package(pkg_name)
        assert not pkg.is_installed, 'the specified pkg is unexpectedly installed: {}'.format(pkg_name)

    @pytest.mark.negative
    def test_apt_get_install_wrong_version(self, shell_executor, remove_rolldice, host):
        """Check apt-get install can not install a package with wrong package version
               Pre-conditions
                   1. Fully uninstall a package

               Scenario:
                   1. Try to install a package using apt-get install
                   2. Check that apt-get returns an error
                   3. Check if it was not installed
        """
        version = "1.16-2"
        pkg_name = "rolldice"
        pkg_version = "{}={}".format(pkg_name, version)
        _, error = shell_executor.apt_install_pkg(pkg_version)
        assert error, "should return an error: Version '{}' for '{}' was not found".format(version, pkg_name)
        pkg = host.package(pkg_name)
        assert not pkg.is_installed, 'the specified pkg is unexpectedly installed: {}'.format(pkg_name)
