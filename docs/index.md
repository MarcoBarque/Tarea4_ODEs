# Aproximation of ordinary differential equations
**By Marco Barquero(C30970) and Andres Chacon (C32026)**

In physics is common to encounter differential equations that have no analitical solution. This kind of differential equations are resolved by using aproximations. An example of one these equations is:

$$ \frac{dy}{dx}=x^4y^2+\frac{x}{y^3} $$

In general, the methods that will be described in this article can only be used if the differential equations has the form:

$$ \frac{dy}{dx}=f(x,y) $$

For these methods, the equation described before must satisfy two conditions:

- The function \(f\), must be a function of \(x\) and \(y\), so \(f=f(x,y)\).
- The dependant variable evaluated in \(x=x_{0}\) must exist and be a known value. So \(y(x=x_{0})=y_{0}\). 

The numeric methods for the aproximation of the differential equations are:

- Euler's method
- Runge Kutta method of second order
- Runge Kutta method of fourth order

It is important to mention that all these methods have an associated error, the margin of the error is determinated by the magnitude of the 'steps'. The step is the value of the amount of change of the independet variable, in the optimal case these steps would be inifitesimal so the derivative of the function could be calculated, however, it would be impossible to compute an aproximation with infitesimal steps. So, is important to consider the value of the steps acordingly to the method that will be used and the precision required.

## Euler's method

This aproximation is based on the Taylor Series of a function \(y(x+h)\), where \(h\) is the 'step' mentiond before. One can assume that the step \(h\) is inifitesimal, so the Taylor Series of the function can be aproximated to:

$$ y(x+h)=y(x)+hf(x,y) $$

This method is the least precise of the three but is the fastest because requieres just one calculation per iteration. To be as precise as the Runge Kutta method it needs smaller steps and therefore a lot more iterations. 

## Runge Kutta Method

The method will be described for second and fourth order. This method requires more time to be computed, but the precision gained in the aproximation is worth it depending on the size of interval and the function \(f(x,y)\).

#### Second Order (RK2)

As in Euler's method, this aproximation is obtained from the Taylor Series of a function \(y(x+h)\). The value of the function in a given iteration is decribed by:

$$ y(x+h)=y(x)+hk_{2} $$

Where \(k_{i}\) are calculated as:

- \(k_{1}= f(x,y)\)
- \(k_{2}= f(x+\frac{h}{2}, y+\frac{k_{1}}{2})\)

#### Fourth Order (RK4)

This method is the most precise of the three, if possible, one should use this method. The reason why it is not always viable is because it requieres more calculations per iteration. The aproximation of \(y(x+h)\) through this method is:

$$y(x+h)=y(x)+\frac{h}{6}(k_{1}+2k_{2}+2k_{3}+k_{4})$$

Where \(k_{i}\) are:

- \(k_{1} = f(x,y)\)
- \(k_{2} = f(x+\frac{h}{2}, y+\frac{k_{1}}{2})\)
- \(k_{3} = f(x+\frac{h}{2}, y+\frac{k_{2}}{2})\)
- \(k_{4} = f(x+h,y+k_{3})\)


