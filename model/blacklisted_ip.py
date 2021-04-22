from model import ip_range


class BlacklistedIP(ip_range.IPRange):
    """
    A Range of IP's not to be scanned. This IP Range cannot be editted
    """

    def __init__(self):
        ip_range.IPRange.__init__(self)
        pass

    '''
    The next three methods are overridden so that they cannot be edited.
    '''
    def insert_range(self, given_lower: str, given_upper: str) -> None:
        pass

    def pop_lowest(self) -> str:
        return ''

    def pop_highest(self) -> str:
        return ''