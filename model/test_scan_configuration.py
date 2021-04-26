import unittest
from model.scan_configuration import ScanConfiguration
from model.tool_configuration import ToolConfiguration


class TestScanConfiguration(unittest.TestCase):


    def setUp(self) -> None:
        self.tool: ToolConfiguration = ToolConfiguration()
        self.tool.set_name('Super Test Scan')
        self.tool.set_path('/usr/bin/nmap')
        self.tool.set_option_arg(['-p 21-25,80,139,8080 127.0.0.1'])
        self.scan_config: ScanConfiguration = ScanConfiguration(scan_identification='asdfalkjsdf90823rlksdjf')
        self.scan_config.__tool_configuration = self.tool
        self.scan_config.set_execution_number(0)

    def tearDown(self) -> None:
        del self.tool
        self.scan_config.terminate_()
        del self.scan_config

    def test_execute_(self):
        self.scan_config.execute_()
