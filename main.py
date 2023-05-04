import BoxPlot
import pareto
import pieChart
import polygon
import Mediana

# use online generator №54
# GENERATION OPTIONS
# Mu (mean) = 25
# Sigma (standard deviation) = 1.7

# Quantity of numbers = 148
# Number of decimal places (round) = 0

x = [24, 27, 28, 26, 24, 25, 24, 23, 22, 28, 28, 24, 24, 22, 24, 26, 28, 25, 23, 24, 22, 25, 26, 25, 26, 25, 24, 24, 25,
     21, 26, 28, 22, 26, 23, 24, 24, 23, 25, 27, 25, 22, 29, 25, 27, 24, 24, 23, 27, 25, 28, 25, 24, 27, 24, 28, 26, 26,
     25, 26, 23, 26, 25, 25, 27, 26, 23, 28, 26, 28, 26, 25, 23, 23, 26, 25, 25, 26, 27, 24, 28, 25, 25, 24, 25, 25, 28,
     22, 24, 25, 28, 27, 30, 24, 22, 27, 25, 25, 25, 27, 27, 24, 23, 26, 21, 23, 24, 28, 23, 22, 22, 24, 28, 27, 26, 24,
     23, 25, 25, 26, 24, 26, 27, 24, 26, 24, 24, 26, 23, 26, 28, 25, 25, 25, 28, 26, 29, 25, 26, 25, 25, 26, 25, 26, 25,
     26, 22, 26]

polygon.polygonAndHistogram(x)
BoxPlot.box(x)
pareto.pareto(x)
pieChart.pie(x)

Mediana.mean(x)
print()
Mediana.median(x)
print()
Mediana.mode(x)
print()
Mediana.variance(x)