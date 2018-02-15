from rest_framework.throttling import AnonRateThrottle


class BurstRateThrottle(AnonRateThrottle):
    scope = 'burst'
    rate = '2/min'

  
class SustainedRateThrottle(AnonRateThrottle):
    scope = 'sustained'
    rate = '15/day'
