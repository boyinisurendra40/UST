import time
import random

def stock_price_manipulator(base_price, volatility, steps):
    current_price = base_price
    
    for _ in range(steps):
        fluctuation = random.uniform(-volatility, volatility)
        current_price += current_price * fluctuation
        print(f"Stock price: {current_price:.2f}")
        time.sleep(1)

stock_price_manipulator(200, 0.03, 10)
