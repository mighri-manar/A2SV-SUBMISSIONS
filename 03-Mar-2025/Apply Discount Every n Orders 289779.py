# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.x = discount
        self.m = defaultdict(int)
        for i in range(len(products)):
            self.m[products[i]] = prices[i]
        self.c = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.c += 1
        bill = 0
        for i in range(len(product)):
            bill += self.m[product[i]] * amount[i]
        if (self.c % self.n == 0):
            disc = (self.x/100) * bill
            bill -= disc
        return bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)