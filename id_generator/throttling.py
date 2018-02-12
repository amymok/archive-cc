from rest_framework.throttling import AnonRateThrottle

class BurstRateThrottle(AnonRateThrottle):
    scope = 'burst'
    rate = '60/min'

  
class SustainedRateThrottle(AnonRateThrottle):
    scope = 'sustained'
    rate = '1000/day'