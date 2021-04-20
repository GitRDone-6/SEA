from model import ip_range


class WhitelistedIP(ip_range.IPRange):
    """
    An approved list of IP addresses where the analyst has permission to access.
    Must be mutually exclusive from Blacklisted IP. Cannot be editted

    """

    def __init__(self):
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
