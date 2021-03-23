class IPRange:
    """
    This class is capable of providing logical representation of the IP Range
    groups. This class was produced by Jose Eduardo Soto to generalize Whitelisted IP and
    Blacklisted IP. Scanned IP is another candidate for a useful subclass for our Scan Result
    class. It is a data structure for knowing the logical IP ranges. As opposed to having an
    entire set of IP Addresses.
    """

    def __init__(self):
        pass

    def mutually_exclusive(self, ip_range):
        """
        Checks if the IP is mutually exclusive.
        :param ip_range:
        :return:
        """
        pass

    def pop_lowest(self):
        """
        Removes and returns the lowest IP in the IP Range
        :return:
        """
        pass

    def pop_highest(self):
        """
        Removes and returns the highest IP in the IP Range
        :return:
        """
        pass

    def peek_highest(self):
        """
        Returns the highest IP in the IP Range
        :return:
        """
        pass

    def peek_lowest(self):
        """
        Returns the lowest IP in the IP Range
        :return:
        """
        pass

    def remove_(self, ip_range):
        """
        Removes all of the IPs from the IP Range
        :param ip_range:
        :return:
        """
        pass