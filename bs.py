import numpy as np
def binomial_price(S,K,T,r,sigma, steps=500, call=True, american=False, q=0.0):
    S,K,T,r, sigma,q=map(float,(S,K,T,r,sigma,q))
    if steps<1 or T<=0 or sigma <=0:
        payoff=max(0.0,(S-K) if call else (K-S))
        return payoff
    dt=T/steps
    u=np.exp(sigma)