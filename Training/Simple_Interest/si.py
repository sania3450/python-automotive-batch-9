import calculator

def calculate_si(p, r, t):
    p_r = calculator.mul(p, r)
    p_r_t = calculator.mul(p_r, t)
    si = calculator.div(p_r_t, 100)
    return si

p=float(input("Enter Principal: "))
r=float(input("Enter Rate of Interest: "))
t=float(input("Enter Time (years): "))

result=calculate_si(p,r,t)
print("Simple Interest =", result)