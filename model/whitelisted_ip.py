from model import ip_range


class WhitelistedIP(ip_range.IPRange):
    """
    An approved list of IP addresses where the analyst has permission to access.
    Must be mutually exclusive from Blacklisted IP. Cannot be editted

    """

    def __init__(self, ip_list: list[tuple] or list[str]):
        ip_range.IPRange.__init__(self, '0.0.0.0', '0.0.0.0')
        self._list = ip_list

    '''
    No editing.
    '''
    def insert_range(self, given_lower: str, given_upper: str) -> 'WhitelistedIP':
        return self

    def insert_ip(self, ip: str) -> 'WhitelistedIP':
        return self

    def pop_lowest(self) -> str:
        return ''

    def pop_highest(self) -> str:
        return ''

    def clear_list(self) -> 'WhitelistedIP':
        return self

    def eliminate_ip(self, ip: str) -> bool:
        return False

    def eliminate_range(self, range: 'ip_range.IPRange') -> bool:
        return False
