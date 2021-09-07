import unittest
from model.ip_range import IPRange


class TestIPRange(unittest.TestCase):
    ip: IPRange
    HIGHEST_IP: str = '255.255.255.255'
    LOWEST_IP: str = '0.0.0.0'
    LOWER_IP: str = '127.0.0.1'
    UPPER_IP: str = '128.0.0.1'

    def setUp(self) -> None:
        self.ip = IPRange(TestIPRange.LOWER_IP, TestIPRange.UPPER_IP)

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def tearDown(self) -> None:
        del self.ip

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_insert_ip(self):
        """
        Tests insert_ip
        :return:
        """

        """
        TC1: Insert an IP that should already be contained logically in the given IP range object. It should contain it.
        The previous version of the range should be the same as the new one after the change. 
        """
        list_old_version: list = self.ip.get_list()
        self.ip.insert_ip('127.0.0.1')
        self.assertTrue(self.ip.contains('127.0.0.1'))
        self.assertEqual(list_old_version, self.ip.get_list())

        """
        TC2: Insert an IP that should not be already contained logically in the given IP range object. It should not
        contain it. The previous version of the range should not be the same as the new one after the change. 
        """
        self.ip.insert_ip('128.0.0.2')
        self.assertTrue(self.ip.contains('128.0.0.2'))
        self.assertNotEqual(list_old_version, self.ip.get_list())

    def test_contains(self):
        """
        Tests contains
        :return:
        """

        '''
        TC1: Check if edge case IPs should logically be inside of the IP Range Object are indeed inside. 
        '''
        self.assertTrue(self.ip.contains(TestIPRange.LOWER_IP))
        self.assertTrue(self.ip.contains(TestIPRange.UPPER_IP))

        '''
        TC2: Check if the outter edge case IPs should logically be outside of the IP Range Object
        '''
        self.assertFalse(self.ip.contains('127.0.0.0'))
        self.assertFalse(self.ip.contains('128.0.0.2'))

    def test__check_valid_range(self):
        """
        Tests _check_valid_range
        :return:
        """

        '''
        TC1: Check if lower is equal to upper
        '''
        self.assertIsNone(self.ip._check_valid_range(TestIPRange.LOWEST_IP, TestIPRange.LOWEST_IP))

        '''
        TC2: Check when lower is greater than upper
        '''
        self.assertRaises(ValueError, self.ip._check_valid_range, TestIPRange.HIGHEST_IP, TestIPRange.LOWEST_IP)

    def test_different_by_one(self):
        """
        Tests _different_by_one
        :return:
        """

        '''
        TC1: IF both IP's are the same, should return false.'''
        self.assertFalse(self.ip._different_by_one('0.0.0.0', '0.0.0.0'))

        '''
        TC2: If the IP's are the edge IP's then return false'''
        self.assertFalse(self.ip._different_by_one(TestIPRange.LOWEST_IP, TestIPRange.HIGHEST_IP))

        '''
        TC3: If the IP's are different by one in the last byte, return true'''
        self.assertTrue(self.ip._different_by_one(TestIPRange.LOWEST_IP, '0.0.0.1'))

        '''
        TC4: If the first IP's last byte is 255 and the second IP's last byte is 0 and the other bytes are valid, return
        true.'''
        self.assertTrue(self.ip._different_by_one('127.0.0.255', '127.0.1.0'))

        '''
        TC5: If the other octets are not neighbors then return false'''
        self.assertFalse(self.ip._different_by_one('127.0.0.0', '128.0.0.1'))
        self.assertFalse(self.ip._different_by_one('127.0.0.0', '127.1.0.1'))
        self.assertFalse(self.ip._different_by_one('127.0.0.0', '127.0.1.1'))

    def test_insert_range(self):
        """
        Tests insert_range
        :return:
        """

        old_version_list: list
        changed_version_list: list

        '''
        TC1: Insert a single range (1 IP address) that is logically included in the older version of IP Range Object. It
        should be the same list as before. The list will stay ordered from least to greatest.
        '''
        old_version_list = self.ip.get_list()
        self.ip.insert_range(TestIPRange.LOWER_IP, TestIPRange.LOWER_IP)
        changed_version_list = self.ip.get_list()
        self.assertEqual(old_version_list, changed_version_list)
        self.check_in_order_least_to_greatest(changed_version_list)

        '''
        TC2: Insert a single range (1 IP address) that is logically not included in the older version of the IP Range
        Object. It should not be the same list as before. The list will stay ordered from least to greatest.
        '''
        old_version_list = changed_version_list
        self.ip.insert_range('128.0.0.3', '128.0.0.3')
        changed_version_list = self.ip.get_list()
        self.assertNotEqual(old_version_list, changed_version_list)
        self.check_in_order_least_to_greatest(changed_version_list)

        '''
        TC3: Insert a range that is logically included in the older version of the IP Range. The IP Range object should 
        not have changed. The list will stay ordered from least to greatest.
        '''
        old_version_list = changed_version_list
        self.ip.insert_range(TestIPRange.LOWER_IP, TestIPRange.UPPER_IP)
        changed_version_list = self.ip.get_list()
        self.assertEqual(old_version_list, changed_version_list)
        self.check_in_order_least_to_greatest(changed_version_list)

        '''
        TC4: Insert a range that is logically completed excluded in the older version of the IP Range. The bounds are at
        more that 1 difference. The IP Range object should have a completely new element in its list that matches the 
        given range therefore the length of the list has grown by 1. The list will stay ordered from least to greatest. 
        '''
        old_version_list = changed_version_list
        self.ip.insert_range('128.0.0.4', '129.0.0.0')
        changed_version_list = self.ip.get_list()
        self.assertEqual(len(old_version_list) + 1, len(changed_version_list))
        self.check_in_order_least_to_greatest(changed_version_list)

        '''
        TC5: Insert a range that is partially included in the IP Range object of only one element by its upper region. 
        The IP Range object should have that element extended by the lower bound given AND the list should have the same
        number of elements. The list will stay ordered from least to greatest.
        '''
        old_version_list = changed_version_list
        self.ip.insert_range('126.0.0.0', '127.1.0.0')
        changed_version_list = self.ip.get_list()
        self.assertEqual(len(old_version_list), len(changed_version_list))
        self.compare_range_less(changed_version_list[0], old_version_list[0])
        self.check_in_order_least_to_greatest(changed_version_list)

        '''
        TC6: Insert a range that is partially included in the IP Range object of only one element by its lower region. 
        The IP Range object should have that element extended by the upper bound given AND the list should have the same
        number of elements. The list will stay ordered from least to greatest.
        '''
        old_version_list = changed_version_list
        self.ip.insert_range('128.1.0.0', '130.0.0.0')
        changed_version_list = self.ip.get_list()
        self.assertEqual(len(old_version_list), len(changed_version_list))
        self.compare_range_greater(changed_version_list[-1], old_version_list[-1])
        self.check_in_order_least_to_greatest(changed_version_list)

        '''
        TC7: Insert a range that is partially included in the IP Range object of at least 2 elements. All inclusive 
        ranges will have the bounds changed will be changed and any over-covered IP ranges will be eliminated. The 
        length of the changed list will be decreased. The list will stay ordered from least to greatest.
        '''
        old_version_list = changed_version_list
        self.ip.insert_range('131.0.0.0', '131.0.0.1')
        self.ip.insert_range('127.0.0.1', '131.1.0.0')
        changed_version_list = self.ip.get_list()
        self.assertGreater(len(old_version_list), len(changed_version_list))
        self.check_in_order_least_to_greatest(changed_version_list)

    def check_in_order_least_to_greatest(self, ip_range_list):
        for index in range(len(ip_range_list)-1):
            prev = ip_range_list[index]
            nex_t = ip_range_list[index + 1]
            self.compare_range_less(prev, nex_t)

    def compare_range_less(self, previous, nex_t):
        if type(previous) is str and type(nex_t) is str:
            self.assertLess(previous, nex_t)
        if type(previous) is str and type(nex_t) is not str:
            self.assertLess(previous, nex_t[0])
        if type(previous) is not str and type(nex_t) is str:
            self.assertLess(previous[0], nex_t)
        if type(previous) is not str and type(nex_t) is not str:
            self.assertLess(previous[0], nex_t[0])

    def test_is_mutually_exclusive(self):
        """
        Tests is_mutually_exclusive
        :return:
        """

        '''
        TC1: Check if not mutually exclusive if they are the same list
        '''
        other_ip_range = IPRange(TestIPRange.LOWER_IP, TestIPRange.UPPER_IP)
        exclusive, index = self.ip.is_mutually_exclusive(other_ip_range)
        self.assertFalse(exclusive)
        self.assertEqual(0, index)

        '''
        TC2: Check if mutually exclusive'''
        other_ip_range = IPRange('129.0.0.0', '130.0.0.0')
        exclusive, index = self.ip.is_mutually_exclusive(other_ip_range)
        self.assertTrue(exclusive)
        self.assertIsNone(index)

        '''
        TC3: Check if only one element of the other range is not mutually exclusive'''
        other_ip_range.insert_ip(TestIPRange.HIGHEST_IP)
        self.ip.insert_ip(TestIPRange.HIGHEST_IP)
        exclusive, index = self.ip.is_mutually_exclusive(other_ip_range)
        self.assertFalse(exclusive)

    def test_get_list(self):
        """
        Tests get_list
        :return:
        """

        '''
        TC1: Make sure the type is correct'''
        test_list = self.ip.get_list()
        self.assertIsInstance(test_list, list)

    def test_pop_lowest(self):
        """
        Tests pop_lowest
        :return:
        """

        '''
        TC1: If the list is empty, it should return an empty string'''
        self.ip.clear_list()
        self.assertEqual(self.ip.pop_lowest(), '')

        '''
        TC2: If the list has only one element, it should withdraw only that element and be empty'''
        self.ip.insert_ip(TestIPRange.HIGHEST_IP)
        self.assertEqual(self.ip.pop_lowest(), TestIPRange.HIGHEST_IP)
        self.assertTrue(self.ip.empty())

    def test_pop_highest(self):
        """
        Tests pop_highest
        :return:
        """

        '''
        TC1: If the list is empty, it should return an empty string'''
        self.ip.clear_list()
        self.assertEqual(self.ip.pop_highest(), '')

        '''
        TC2: If the list has only one element, it should withdraw only that element and be empty'''
        self.ip.insert_ip(TestIPRange.LOWEST_IP)
        self.assertEqual(self.ip.pop_highest(), TestIPRange.LOWEST_IP)
        self.assertTrue(self.ip.empty())

    def test_peek_highest(self):
        """
        Tests peek_highest
        :return:
        """

        '''
        TC1: Should return the highest IP in the list and not remove it'''
        self.ip.insert_ip(TestIPRange.HIGHEST_IP)
        self.assertEqual(self.ip.peek_highest(), TestIPRange.HIGHEST_IP)
        self.assertEqual(self.ip.peek_highest(), TestIPRange.HIGHEST_IP)

        '''
        TC2: Should return an empty string if it is empty'''
        self.ip.clear_list()
        self.assertEqual(self.ip.peek_highest(), '')

    def test_peek_lowest(self):
        """
        Tests peek_lowest
        :return:
        """

        '''
        TC1: Should return the lowest IP in the list and not remove it.'''
        self.ip.insert_ip(TestIPRange.LOWEST_IP)
        self.assertEqual(self.ip.peek_lowest(), TestIPRange.LOWEST_IP)
        self.assertEqual(self.ip.peek_lowest(), TestIPRange.LOWEST_IP)

        '''
        TC2: Should return en ampty string if it is empty'''
        self.ip.clear_list()
        self.assertEqual(self.ip.peek_lowest(), '')

    def test_eliminate_range(self):
        """
        Tests eliminate_range
        :return:
        """

        other_ip_range = IPRange(TestIPRange.LOWER_IP, TestIPRange.UPPER_IP)

        '''
        TC1: If this_ip_range is empty, should return false'''
        self.ip.clear_list()
        self.assertFalse(self.ip.eliminate_range(other_ip_range))

        '''
        TC2: If this_ip_range and other_ip_range are the exact same range, then the list should be empty and the 
        operation evaluate to True'''
        self.ip.insert_range(TestIPRange.LOWER_IP, TestIPRange.UPPER_IP)
        self.assertEqual(self.ip.get_list(), other_ip_range.get_list())
        self.assertTrue(self.ip.empty())
        self.assertTrue(self.ip.eliminate_range(other_ip_range))

        '''
        TC3: If this_ip_range and other_ip_range are mutually exclusive, then the list should not change.'''
        self.ip.insert_range(TestIPRange.LOWER_IP, TestIPRange.UPPER_IP)
        self.assertTrue(self.ip.is_mutually_exclusive(other_ip_range))
        older_version_list = self.ip.get_list()
        self.ip.eliminate_range(other_ip_range)
        changed_version_list = self.ip.get_list()
        self.assertEqual(older_version_list, changed_version_list)

    def test_eliminate_ip(self):
        """
        Tests eliminate_ip
        :return:
        """

        '''
        TC1: If the IP Range list is empty, just return false.'''
        self.ip.clear_list()
        self.assertFalse(self.ip.eliminate_ip(self.LOWER_IP))

        '''
        TC2: If the IP Range contains a range of IP's and is given an IP in the middle of the range, The list size will
        grow by 1. Operation will be True.'''
        self.ip.insert_range(self.LOWER_IP, self.UPPER_IP)
        older_version_list = self.ip.get_list()
        eliminated = self.ip.eliminate_ip('127.1.0.0')
        changed_version_list = self.ip.get_list()
        self.assertLess(len(older_version_list), len(changed_version_list))
        self.assertTrue(eliminated)

        '''
        TC3: If the IP Range contains a range of IP's and is given an IP on the edge of the range, the list size will 
        stay the same. Operation will be True.'''
        self.ip.clear_list()
        self.ip.insert_range(TestIPRange.LOWER_IP, TestIPRange.UPPER_IP)
        older_version_list = self.ip.get_list()
        eliminated = self.ip.eliminate_ip(TestIPRange.LOWER_IP)
        changed_version_list = self.ip.get_list()
        self.assertEqual(len(older_version_list), len(changed_version_list))
        self.assertTrue(eliminated)

        '''
        TC4: If the IP Range contains a range of IP's and the given IP is not logically represented, the list size will
        stay the same. Operation will be False.'''
        self.ip.clear_list()
        self.ip.insert_range(TestIPRange.LOWER_IP, TestIPRange.UPPER_IP)
        older_version_list = self.ip.get_list()
        eliminated = self.ip.eliminate_ip(TestIPRange.HIGHEST_IP)
        changed_version_list = self.ip.get_list()
        self.assertEqual(len(older_version_list), len(changed_version_list))
        self.assertFalse(eliminated)

    def test_to_dict(self):
        this_dictionary = {'ip_range_list': self.ip.get_list()}
        self.assertDictEqual(self.ip.to_dict(), this_dictionary)

    def compare_range_greater(self, previous, nex_t):
        if type(previous) is str and type(nex_t) is str:
            self.assertGreater(previous, nex_t)
        if type(previous) is str and type(nex_t) is not str:
            self.assertGreater(previous, nex_t[1])
        if type(previous) is not str and type(nex_t) is str:
            self.assertGreater(previous[1], nex_t)
        if type(previous) is not str and type(nex_t) is not str:
            self.assertGreater(previous[1], nex_t[1])
