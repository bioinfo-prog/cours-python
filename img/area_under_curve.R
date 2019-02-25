# define Gaussian function
f = function(x) return( (2*pi)^-.5 * exp(-x^2/2) )

# define coors
x = seq(-4, 4, .1)
y = f(x)
# plot
plot(x, y, type="l", lwd=2, xlab="x", ylab="f(x)")
abline(h=0, v=0)

# draw area (source: https://stackoverflow.com/questions/36948624/shade-area-under-a-curve)
BEGIN = 1
END = 2
polygon(c(x[x>=BEGIN & x<=END], END, BEGIN), c(y[x>=BEGIN & x<=END], 0, 0), col=gray(.2), density=20)

# add vertical lines
for (i in seq(-4, 4)) {
    segments(i, 0, i, f(i))
}