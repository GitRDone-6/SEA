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

    def __init__(self, lower: str, upper: str):
        self._check_valid_range(lower, upper)
        self._list = [(lower, upper)]

    @staticmethod
    def _check_valid_range(lower: str, upper: str) -> None:
        if lower > upper:
            raise ValueError('lower is greater than upper')

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
            Answer  3) Extend the tuple to the outlying bound.
            Return  3) [("126.0.0.1", "128.0.0.1"), ("129.0.0.1"), ("201.0.0.1", 204.0.0.1")]
            
        We also need to check if a tuple goes over any other tuple.
        
        '''
        self._check_valid_range(lower, upper)
        singular_range = lower is upper
        new_range = IPRange(lower, upper)
        #check if new range is exclusive and get the index where it was not
        exclusive, index = self.is_mutually_exclusive(new_range)
        if not exclusive:
            #Singular tuple
            if type(self._list[index]) is str:
                #TODO Make the case where the mutually inclusive range is handled here
            #If its the case where o[---n)o) and n[-o[-), then the o[ is now n[
            elif self._list[index][1] >= upper and lower < self._list[index][0]:
                self._list[index][0] = lower
            #If its the case where o[n[ and o)-n)
            elif self._list[index][0] <= lower and upper > self._list[index][1]:
                '''
                It doesn't know if the new upper bound is greater than only this old ip upper bound or the next one's as
                well. So we must check each one after the one in the index.
                '''
                #If its the last element of the list, just update the upper.
                if index is len(self._list)-1:
                    self._list[index][1] = upper
                #Since there might be more than one tuple to eliminate, then lets track how many.
                ranges_to_eliminate = 0
                for ip_range in self._list:
                    #Check if the tuple the i is on is singular
                    if type(ip_range) is str:
                        # If the singular tuple is equal to the upper, then increment, update the upper for index,
                        # and stop.
                        if ip_range is upper:
                            ranges_to_eliminate += 1
                            self._list[index][1] = upper
                            break
                        # If the singular tuple is greater than the upper, then just update the upper for index, and
                        # stop.
                        elif ip_range > upper:
                            self._list[index][1] = upper
                            break
                        # All that's left is if the singular tuple is less than the upper; increment, update, and cont.
                        else:
                            ranges_to_eliminate += 1
                            self._list[index][1] = upper
                    #Non-singular tuples
                    #If n)-o[, update index and stop
                    elif upper < ip_range[1]:
                        self._list[index][1] = upper
                    #If the case is o[n) and n)o), remove this index, expand the original upper, and stop
                    elif ip_range[0] <= upper <= ip_range[1]:
                        ranges_to_eliminate += 1
                        self._list[index][1] = upper
                        break
                    #If o(-o]-n], increment, and continue
                    elif ip_range[0] <= upper > ip_range[1]:
                        ranges_to_eliminate += 1
                #Eliminate the range tuples
        else:
            # Search where to insert the new ip tuple




    def is_mutually_exclusive(self, other: 'IPRange') -> (bool, int):
        """
        Checks if the IP is mutually exclusive.
        :param other:
        :return:
        """
        '''
        There's only two cases: 
            1) Other's lower bound is greater than This lower bound -> False
            2) Other's upper bound is less than This upper bound -> False
            
        Check each tuple in each ip range if they are inside each other. If they are singular then there are special 
        case
        
        TODO: This implementation can be improved. This .index method traverses the list a second time. Please update 
        this
        '''

        this_list = self.get_list()
        other_list = other.get_list()
        for this_ip_range in this_list:
            for other_ip_range in other_list:
                #Only way to check if a tuple is singular is a type check, len returns the len of the element itself
                if type(this_ip_range) is str and type(other_ip_range) is str:
                    if this_ip_range[0] is other_ip_range[0]:
                        return False, this_list.index(this_ip_range)
                elif type(this_ip_range) is str and type(other_ip_range) is not str:
                    if other_ip_range[0] <= this_ip_range[0] < other_ip_range[1]:
                        return False, this_list.index(this_ip_range)
                elif type(this_ip_range) is not str and type(other_ip_range) is str:
                    if this_ip_range[0] <= other_ip_range[0] < this_ip_range[1]:
                        return False, this_list.index(this_ip_range)
                else:
                    if this_ip_range is other_ip_range:
                        return False, this_list.index(this_ip_range)
                    elif this_ip_range[0] <= other_ip_range[0] < this_ip_range[1]:
                        return False, this_list.index(this_ip_range)
                    elif other_ip_range[0] <= this_ip_range[0] < other_ip_range[1]:
                        return False, this_list.index(this_ip_range)
        return True, None

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

    def eliminate(self, range: 'IPRange') -> bool:
        """
        Removes all of the IPs from the IP Range
        :param ip_range:
        :return:
        """
        pass