import math
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

    _list: list[tuple[str, str]] or list[str]

    def __init__(self, lower: str, upper: str):
        self._check_valid_range(lower, upper)
        self._list = [(lower, upper)]

    @staticmethod
    def _check_valid_range(lower: str, upper: str) -> None:
        """
        Checks if the given strings follow the semantics of being a lower and an upper
        :param lower: The given inclusive lowest IP of the IP Range.
        :type lower: str
        :param upper: The given inclusive highest IP of the IP range.
        :type upper: str
        :return: Nothing
        :raises ValueError: If the lower is greater than the upper.
        """
        if lower > upper:
            raise ValueError('Invalid Range: lower is greater than upper')

    def insert_range(self, given_lower: str, given_upper: str) -> None:
        """
        Insert a given range. Input the same IP for a single IP.
        :param given_upper: inclusive upper bound of an ip range.
        :type given_upper: str
        :param given_lower: inclusive lower bound of an ip range.
        :type given_lower: str
        :return: Nothing. IP Range will completely contain the given ranges. Completely means there are no breaks
        between the ranges.
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

        self._check_valid_range(given_lower, given_upper)
        singular_range = given_lower is given_upper
        new_range = IPRange(given_lower, given_upper)
        #check if new range is exclusive and get the index where it was not
        exclusive, index = self.is_mutually_exclusive(new_range)
        if not exclusive:
            #Singular tuple, a tuple with only one thing is no longer a tuple type.
            if type(self._list[index]) is str:
                #TODO Make the case where the mutually inclusive range is handled here
                pass
            #If its the case where o[---n)o) and n[-o[-), then the o[ is now n[
            elif self._list[index][1] >= given_upper and given_lower < self._list[index][0]:
                self._list[index] = list(self._list[index])
                self._list[index][0] = given_lower
                self._list[index] = tuple(self._list[index])
            #If its the case where o[n[ and o)-n), then n) is the new o)
            elif self._list[index][0] <= given_lower and given_upper > self._list[index][1]:
                '''
                It doesn't know if the new upper bound is greater than only this old ip upper bound or the next one's as
                well. So we must check each one after the one in the index.
                '''
                #If its the last element of the list, just update the upper.
                if index is len(self._list)-1:
                    self._list[index] = list(self._list[index])
                    self._list[index][1] = given_upper
                    self._list[index] = tuple(self._list[index])
                #Since there might be more than one tuple to eliminate, then lets track how many.
                ranges_to_eliminate = 0
                for ip_range in self._list[index + 1:]:
                    #Check if the tuple the i is on is singular
                    if type(ip_range) is str:
                        # If the singular tuple is equal to the upper, then increment, update the upper for index,
                        # and stop.
                        if ip_range is given_upper:
                            ranges_to_eliminate += 1
                            self._list[index][1] = given_upper
                            break
                        # If the singular tuple is greater than the upper, then just update the upper for index, and
                        # stop.
                        elif ip_range > given_upper:
                            self._list[index][1] = given_upper
                            break
                        # All that's left is if the singular tuple is less than the upper; increment, update, and cont.
                        else:
                            ranges_to_eliminate += 1
                            self._list[index][1] = given_upper
                    #Non-singular tuples
                    #If n)-o[, update index and stop
                    elif given_upper < ip_range[1]:
                        self._list[index][1] = given_upper
                    #If the case is o[n) and n)o), remove this index, expand the original upper, and stop
                    elif ip_range[0] <= given_upper <= ip_range[1]:
                        ranges_to_eliminate += 1
                        self._list[index][1] = given_upper
                        break
                    #If o(-o]-n), increment, and continue
                    elif ip_range[0] <= given_upper > ip_range[1]:
                        ranges_to_eliminate += 1
                #Eliminate the range tuples. if ranges_to_eliminate is 0 then it won't delete anything nor crash.
                #TODO I have to find an easy way to not have to traverse through the code again and just delete from
                #TODO where we were found the end of our included tuples
                for i in range(1, ranges_to_eliminate):
                    del self._list[index + i]
        else:
            # Search where to insert the new ip tuple
            # Maybe I can use the mutally exclusive method to return the index of where it stopped looking. CANNOT
            for ind in range(len(self._list)):
                if ind is len(self._list)-1:
                    if given_upper < self._list[ind][0]:
                        self._list.insert(ind, (given_lower, given_upper))
                        break
                    else:
                        self._list.append((given_lower, given_upper))
                        break
                elif ind is 0:
                    if given_upper < self._list[ind][0]:
                        self._list.insert(ind, (given_lower, given_upper))
                        break
                if self._list[ind] is str:
                    if given_upper < self._list[ind]:
                        self._list.insert(ind, (given_lower, given_upper))
                        break
                elif type(self._list[ind]) is tuple:
                    if given_upper < self._list[ind][0]:
                        self._list.insert(ind, (given_lower, given_upper))
                        break

    @staticmethod
    def _different_by_one(ip1: str, ip2: str) -> bool:
        """
        Returns whether or not the two ips are different by 1
        :param ip1: First IP to be compared
        :type ip1: str
        :param ip2: Second IP to be compared
        :type ip2: str
        :return: True if the IP's are logically different by 1, false if same or different by more than 1
        """

        if ip1 is ip2: return False

        greater_ip: str = max(ip1, ip2)
        greater_list: list[int] = [int(octet) for octet in greater_ip.split('.')]
        lesser_ip: str = min(ip1, ip2)
        lesser_list: list[int] = [int(octet) for octet in lesser_ip.split('.')]

        if lesser_list[-1] == 255 and greater_list[-1] == 0:
            if lesser_list[-2] == 255 and greater_list[-2] == 0:
                if lesser_list[-3] == 255 and greater_list[-3] == 0:
                    if lesser_list[-4] == 255 and greater_list[-4] == 0:
                        return False
                    elif lesser_list[-4]+1 == greater_list[-4]:
                        return True
                    else:
                        return False
                elif lesser_list[-3]+1 == greater_list[-3] and lesser_list[-4] == greater_list[-4]:
                    return True
                else:
                    return False
            elif lesser_list[-2]+1 == greater_list[-2] and lesser_list[-3] == greater_list[-3] and lesser_list[-4] == greater_list[-4]:
                return True
            else:
                return False
        if lesser_list[-1]+1 == greater_list[-1] and \
                lesser_list[-2] == greater_list[-2] and \
                lesser_list[-3] == greater_list[-3] and \
                lesser_list[-4] == greater_list[-4]:
            return True
        return False

    def insert_ip(self, ip: str) -> 'IPRange':
        """
        Inserts a single IP into the IP range.
        :param ip: IP to be inserted. Requires the str to be in IPv4 format
        :type ip: str
        :return: This IP Range object. Ensures that the object will now contain the IP.
        :rtype: IPRange
        """

        list_size = len(self._list)
        if not self._list: self._list.append(ip)
        for index in range(list_size):
            if index is list_size-1:
                if type(self._list[index]) is str:
                    if ip is not self._list[index]:
                        if ip > self._list[index]:
                            if IPRange._different_by_one(ip, self._list[index]):
                                temp_ip = self._list[index]
                                self._list[index] = (temp_ip, ip)
                            else:
                                self._list.append(ip)
                        elif ip < self._list[index]:
                            if IPRange._different_by_one(ip, self._list[index]):
                                temp_ip = self._list[index]
                                self._list[index] = (ip, temp_ip)
                            else:
                                self._list.insert(index, ip)
                elif type(self._list[index]) is tuple:
                    #IP before insert or after append. inside do nothing
                    if ip < self._list[index][0]:
                        if IPRange._different_by_one(ip, self._list[index][0]):
                            self._list[index] = list(self._list[index])
                            self._list[index][0] = ip
                            self._list[index] = tuple(self._list[index])
                        else:
                            self._list.insert(index, ip)
                    elif ip > self._list[index][1]:
                        if IPRange._different_by_one(ip, self._list[index][1]):
                            self._list[index] = list(self._list[index])
                            self._list[index][1] = ip
                            self._list[index] = tuple(self._list[index])
                        else:
                            self._list.append(ip)
            else:
                if self._list[index] is str:
                    #IP Before insert and break, same do nothing and break, after continue
                    if ip < self._list[index]:
                        if IPRange._different_by_one(ip, self._list[index]):
                            temp_ip = self._list[index]
                            self._list[index] = (ip, temp_ip)
                            break
                        else:
                            self._list.insert(index, ip)
                            break
                    elif ip is self._list[index]:
                        break
                    elif ip > self._list[index] and IPRange._different_by_one(ip, self._list[index]):
                        temp_ip = self._list[index]
                        self._list[index] = (temp_ip, ip)
                        break
                elif self._list[index] is tuple:
                    #IP before insert and break, inside do nothing and break. After continue
                    if ip < self._list[index][0]:
                        if IPRange._different_by_one(ip, self._list[index][0]):
                            self._list[index] = list(self._list[index])
                            self._list[index][0] = ip
                            self._list[index] = tuple(self._list[index])
                            break
                        else:
                            self._list.insert(index, ip)
                            break
                    elif self._list[index][0] <= ip <= self._list[index][1]:
                        break
                    elif ip > self._list[index][1] and IPRange._different_by_one(ip, self._list[index][1]):
                        self._list[index] = list(self._list[index])
                        self._list[index][1] = ip
                        self._list[index] = tuple(self._list[index])
        return self

    def contains(self, ip: str) -> bool:
        """
        Returns if the given ip is logically in this IP Range object.
        :param ip: IP to be checked if logically inside IP Range object. Requires ip to be in IPv4 format string.
        :type ip: str
        :return: True if given IP is logically within the IP Range object, false otherwise. Ensures that ip is or is not
        logically inside of the IP Range object.
        """

        for ip_range in self._list:
            if type(ip_range) is str:
                if ip_range is ip:
                    return True
            elif type(ip_range) is tuple:
                if ip_range[0] <= ip <= ip_range[1]:
                    return True
        return False

    def is_mutually_exclusive(self, other: 'IPRange') -> (bool, int):
        """
        Checks if the IP is mutually exclusive. Meaning that there is no single ip inside of the other.
        For all IP's in this_ip_range: x. !other_ip_range.contain(x) &&
        For all IP's in other_ip_range: y. !this_ip_range.contain(y)
        :param other: Other IP Range to be compared.
        :type other: IPRange
        :returns: True if they are mutually exclusive, otherwise false. And the index of the IP Range wheree this_ip
        contains the first found inclusive IP.
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
        Returns a deep copy of the IP Range list such that:
        this_ip_range == returned_ip_range && (returned_ip_range does not reference this_ip_range)
        :return: A deep copy list of the IP range.
        """
        return deepcopy(self._list)

    def clear_list(self) -> 'IPRange':
        """
        Clears all of the contents of the ip range.
        :return:
        """

        self._list.clear()
        return self

    def empty(self) -> bool:
        """
        Returns whether the IP range is empty or not
        :return:
        """
        return len(self._list) is 0

    def pop_lowest(self) -> str:
        """
        Removes and returns the lowest IP in the IP Range
        :return:
        """
        if not self._list: return ''
        lowest_ip: str
        if type(self._list[0]) is str:
            lowest_ip = self._list[0]
            del self._list[0]
            return lowest_ip
        if type(self._list[-1]) is tuple:
            lowest_ip = self._list[0][0]
            if IPRange._different_by_one(self._list[0][0], self._list[0][1]):
                self._list[0] = self._list[0][1]
                return lowest_ip
            self._list[0] = list(self._list[0])
            self._list[0][0] = IPRange.get_next_ip(self._list[0][0], 'upper')
            self._list[0] = tuple(self._list[0])
            return lowest_ip

    @staticmethod
    def get_next_ip(ip: str, upper_or_lower:str) -> str:
        ip_list:list[int] = [int(octet) for octet in ip.split('.')]
        if upper_or_lower is 'upper':
            if ip_list[-1] is 255:
                if ip_list[-2] is 255:
                    if ip_list[-3] is 255:
                        if ip_list[-4] is 255:
                            return ip
                        else:
                            ip_list[-4] += 1
                            ip_list[-3] = 0
                            ip_list[-2] = 0
                            ip_list[-1] = 0
                            return '.'.join([str(octet) for octet in ip_list])
                    else:
                        ip_list[-3] += 1
                        ip_list[-2] = 0
                        ip_list[-1] = 0
                        return '.'.join([str(octet) for octet in ip_list])
                else:
                    ip_list[-2] += 1
                    ip_list[-1] = 0
                    return '.'.join([str(octet) for octet in ip_list])
            else:
                ip_list[-1] += 1
                return '.'.join([str(octet) for octet in ip_list])

        elif upper_or_lower is 'lower':
            if ip_list[-1] is 0:
                if ip_list[-2] is 0:
                    if ip_list[-3] is 0:
                        if ip_list[-4] is 0:
                            return ip
                        else:
                            ip_list[-4] -= 1
                            ip_list[-3] = 255
                            ip_list[-2] = 255
                            ip_list[-1] = 255
                            return '.'.join([str(octet) for octet in ip_list])
                    else:
                        ip_list[-3] -= 1
                        ip_list[-2] = 255
                        ip_list[-1] = 255
                        return '.'.join([str(octet) for octet in ip_list])
                else:
                    ip_list[-2] -= 1
                    ip_list[-1] = 255
                    return '.'.join([str(octet) for octet in ip_list])
            else:
                ip_list[-1] -= 1
                return '.'.join([str(octet) for octet in ip_list])
        else:
            raise ValueError('Invalid input: ' % upper_or_lower)

    def pop_highest(self) -> str:
        """
        Removes and returns the highest IP in the IP Range
        :return:
        """
        if not self._list: return ''
        highest_ip: str
        if type(self._list[-1]) is str:
            highest_ip = self._list[-1]
            del self._list[-1]
            return highest_ip
        if type(self._list[-1]) is tuple:
            highest_ip = self._list[-1][1]
            if IPRange._different_by_one(self._list[-1][0], self._list[-1][1]):
                self._list[-1] = self._list[-1][0]
                return highest_ip
            self._list[-1] = list(self._list[-1])
            self._list[-1][1] = IPRange.get_next_ip(self._list[-1][1], 'lower')
            self._list[-1] = tuple(self._list[-1])
            return highest_ip

    def peek_highest(self) -> str:
        """
        Returns the highest IP in the IP Range
        :return:
        """
        if not self._list: return ''
        if type(self._list[-1]) is str: return self._list[-1]
        if type(self._list[-1]) is tuple: return self._list[-1][1]

    def peek_lowest(self) -> str:
        """
        Returns the lowest IP in the IP Range
        :return:
        """
        if not self._list: return ''
        if type(self._list[0]) is str: return self._list[0]
        if type(self._list[0]) is tuple: return self._list[0][0]

    def eliminate_range(self, range: 'IPRange') -> bool:
        """
        Removes all of the IPs from the IP Range
        :param ip_range: The given range which should be elminated from this IP range
        :type ip_range: IPRange
        :return: True if the method eliminated at least one of this IP range's IP address. False if nothing was removed.
        """
        return False

    def eliminate_ip(self, ip: str) -> bool:
        """
        Removes a single IP from the IP Range
        :param ip: IP to eliminate in the IP Range if it exists logically
        :type ip: str
        :return: Whether or not the given IP was found and eliminated. False if not found or not eliminated
        :rtype: bool
        """

    def to_dict(self) -> dict:
        """
        Gives the dictionary object notation of this IP Range.
        :return:
        """
        return {'ip_range_list': self._list}