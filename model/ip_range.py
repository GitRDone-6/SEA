from copy import deepcopy


class IPRange:
    """
    This class is capable of providing logical representation of the IP Range
    groups. This class was produced by Jose Eduardo Soto to generalize Whitelisted IP and
    Blacklisted IP. Scanned IP is another candidate for a useful subclass for our Scan Result
    class. It is a data structure for knowing the logical IP ranges. As opposed to having an
    entire set of IP Addresses.

    Another IPRange has been discovered in an api called netaddr 0.8.0 https://pypi.org/project/netaddr/
    For the projects sake, we'll still construct our own data structure 3/23/21
    """

    def __init__(self):
        self._list = []
        pass

    def insert(self, lower: str, upper: str) -> None:
        """
        Insert a given range. Input the same IP for a single IP.
        :param upper: exclusive upper bound of an ip range.
        :param lower: inclusive lower bound of an ip range.
        :return:
        """

        '''
        [("127.0.0.1", "128.0.0.1"), ("129.0.0.1"), ("201.0.0.1", 204.0.0.1")]
        So there are three different cases we have to figure out:
        
            Case    1) The range given is entirely inclusive to 1 IP tuple.
            Given   1) ("127.0.0.3", "127.1.0.3")
            Answer  1) No change needed
            Return  1) [("127.0.0.1", "128.0.0.1"), ("129.0.0.1"), ("201.0.0.1", 204.0.0.1")]
            
            Case    2) The range given is entirely exclusive to any IP range.
            Given   2) ("126.0.0.0", "127.0.0.0")
            Answer  2) Insert the range where appropriate
            Return  2) [("126.0.0.0", "127.0.0.0"),("127.0.0.1", "128.0.0.1"), ("129.0.0.1"), ("201.0.0.1", 204.0.0.1")]
            
            Case    3) The range given is partially inclusive of 1 IP Tuple
            Given   3) ("126.0.0.1", 127.0.0.99")
            Answer  3) Extend the tuple to the outling bound.
            Return  3) [("126.0.0.1", "128.0.0.1"), ("129.0.0.1"), ("201.0.0.1", 204.0.0.1")]
            
        We also need to check if a tuple goes over any other tuple.
        
        '''
        if lower > upper:
            raise ValueError('Lower is greater than upper')
        singular_range = lower is upper
        if not self._list:
            self._list.append((lower, upper))
        else:
            for ip_range in self._list:
                if singular_range:


    def is_mutually_exclusive(self, other: 'IPRange') -> bool:
        """
        Checks if the IP is mutually exclusive.
        :param other:
        :return:
        """
        '''
        There's only two cases: 
            1) Other's lower bound is greather than This lower bound -> False
            2) Other's upper bound is less than This upper bound -> False
            
        Check each tuple in each ip range if they are inside each other. If they are singular then there are special case
        '''
        for this_ip_range in self.get_list():
            for other_ip_range in other.get_list():
                if len(this_ip_range) is 1 and len(other_ip_range) is 1:
                    if this_ip_range[0] is other_ip_range[0]:
                        return False
                elif len(this_ip_range) is 1 and len(other_ip_range) is not 1:
                    if other_ip_range[0] <= this_ip_range[0] < other_ip_range[1]:
                        return False
                elif len(this_ip_range) is not 1 and len(other_ip_range) is 1:
                    if this_ip_range[0] <= other_ip_range[0] < this_ip_range[1]:
                        return False
                else:
                    if this_ip_range is other_ip_range:
                        return False
                    elif this_ip_range[0] <= other_ip_range[0] < this_ip_range[1]:
                        return False
                    elif other_ip_range[0] <= this_ip_range[0] < other_ip_range[1]:
                        return False
        return True

    def get_list(self) -> list:
        """
        Returns a deep copy of the IP Range list
        :return:
        """
        return deepcopy(self._list)

    def pop_lowest(self) -> str:
        """
        Removes and returns the lowest IP in the IP Range
        :return:
        """
        pass

    def pop_highest(self) -> str:
        """
        Removes and returns the highest IP in the IP Range
        :return:
        """
        pass

    def peek_highest(self) -> str:
        """
        Returns the highest IP in the IP Range
        :return:
        """
        pass

    def peek_lowest(self) -> str:
        """
        Returns the lowest IP in the IP Range
        :return:
        """
        pass

    def remove_(self, range: 'IPRange') -> bool:
        """
        Removes all of the IPs from the IP Range
        :param ip_range:
        :return:
        """
        pass