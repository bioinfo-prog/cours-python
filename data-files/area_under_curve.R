f = function(x) return( (2*pi)^-.5 * exp(-x^2/2) )

x = seq(-4, 4, .1)
y = f(x)

plot(x, y, type="l", lwd=2, xlab="x", ylab="f(x)")
abline(h=0, v=0)

BEGIN = .5
END = 2
# draw area : https://stackoverflow.com/questions/36948624/shade-area-under-a-curve
polygon(c(x[x>=BEGIN & x<=END], END, BEGIN), c(y[x>=BEGIN & x<=END], 0, 0), col=gray(.2), density=20)