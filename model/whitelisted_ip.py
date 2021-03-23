from model import ip_range


class WhitelistedIP(ip_range.IPRange):
    """
    An approved list of IP addresses where the analyst has permission to access.
    Must be mutually exclusive from Blacklisted IP. Cannot be editted

    """

    def __init__(self):
        pass