png("sin2ori.png")
x = seq(-pi, pi, .01)
plot(x,sin(x),ty="l",lwd=3,col=gray(0.5))
abline(h=0)
abline(v=0)
#points(0,0,pch="X",cex=2)

for (i in seq(-3, 3, 1)){
    points(i,sin(i),pch="x")
    segments(i,sin(i),0,0,lty=2)
}
dev.off()