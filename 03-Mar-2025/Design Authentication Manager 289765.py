# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.record = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.record[tokenId] = currentTime
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.record:
            if self.record[tokenId] + self.ttl > currentTime:
                self.record[tokenId] = currentTime
    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for time in self.record.values() if time <= currentTime < time + self.ttl)



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)