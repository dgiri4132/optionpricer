import numpy as np
def binomial_price(S,K,T,r,sigma, steps=500, call=True, american=False, q=0.0):
    S,K,T,r, sigma,q=map(float,(S,K,T,r,sigma,q))
    if steps<1 or T<=0 or sigma <=0:
        payoff=max(0.0,(S-K) if call else (K-S))
        return payoff
    dt=T/steps
    u=np.exp(sigma*np.sqrt(dt))
    d=1.0/u
    disc=np.exp(-r*dt)
    q_rn=(np.exp((r-q)*dt)-d)/(u-d)
    i=np.arange(steps+1)
    S_T=S*(u**(steps-i))*(d**i)
    V=np.maximum(S_T-K,0.0) if call else np.maximum(K-S_T,0.0)
    for n in range(steps-1,-1,-1):
        V=disc*(q_rn*V[:-1]+(1.0-q_rn)*V[1:])
        if american:
            i=np.arange(n+1)
            S_n=S*(u**(n-i))*(d**i)
            exercise=np.maximum(S_n-K,0.0) if call else np.maximum(K-S_n,0.0)
            V=np.maximum(V,exercise)
    return float(V[0])
