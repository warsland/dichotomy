def dichotomy(a,b,accurate,f):
    time=0;
    print(str(time)+ " a= "+str(a)+ ", b= "+str(b));
    while a<b:
        mid = a + abs(b-a)/2.0;
        if abs(b-a) < accurate:
            return mid;
        if f(mid)*f(b) < 0:
            a = mid;
        if f(a)*f(mid) < 0:
            b=mid;
        time+=1;
        print(str(time)+ " a= "+str(a)+ ", b= "+str(b));

s = dichotomy(1.0,1.5,1e-2,lambda x: x**3-x-1 );
print("answer= "+str(s));
