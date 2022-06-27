from elements import Tubular, Cement
from well import well

t0 = Tubular(name = "Conductor", inD = 7.25, outD = 8, weight = 58, top = 0, low = 250)
t1 = Tubular(name = "Surface", inD = 6.25, outD = 6.75, weight = 47, top = 0, low = 2000, shoeSize = 7)
t2 = Tubular(name = "Intermediate", inD = 5.5, outD = 5.75, weight = 39, top = 0, low = 3750, shoeSize = 6, info = "")
t3 = Tubular(name = "Production", inD = 4.75, outD = 5, weight = 39, top = 0, low = 5200, shoeSize = 5.25, info = "Possible HIC.")
t4 = Tubular(name = "Liner", inD = 3.75, outD = 4, weight = 27, top = 4800, low = 6500, shoeSize = 4.5, info="")
t5 = Tubular(name = "Openhole", inD = 0, outD = 4, top = 6500, low = 6800)
c0 = Cement(top = 0, low = 2000, tub0 = t0, tub1 = t1)
c1 = Cement(top = 1800, low = 3750, tub0 = t2, tub1 = t1)
c2 = Cement(top = 3500, low = 5200, tub0 = t2, tub1 = t3)

well0 = well(name = "Cau-Dill #14-A", kop = 5000)
well0.addTubular(t0)
well0.addTubular(t1)
well0.addTubular(t2)
well0.addTubular(t3)
well0.addTubular(t4)
well0.addTubular(t5)
well0.addCement(c0)
well0.addCement(c1)
well0.addCement(c2)

# Comment to Hide Summaries
#well0.hideCementSummary()


well0.visualize()