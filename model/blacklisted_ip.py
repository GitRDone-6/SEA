from model import ip_range


class BlacklistedIP(ip_range.IPRange):
    """
    A Range of IP's not to be scanned. This IP Range cannot be editted
    """

    def __init__(self):
        ip_range.IPRange.__init__(self)
        pass
