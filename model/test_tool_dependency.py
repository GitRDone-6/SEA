import unittest
from model import tool_dependency as td


class TestToolDependency(unittest.TestCase):

    def setUp(self) -> None:
        self._tool_dep = td.ToolDependency()

    def tearDown(self) -> None:
        del self._tool_dep

    def test_dependent(self):
        self.assertFalse(self._tool_dep.dependent())
        self._tool_dep.set_name('CutyCapt Nmap Dependency').set_expression()
        self.assertTrue(self)
