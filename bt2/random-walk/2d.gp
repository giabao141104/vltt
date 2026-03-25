reset
set terminal pngcairo size 800,400
set output "images/2d-gnuplot.png"
set multiplot layout 1, 2 title "Random Walk 2D"

set title "7 Random Walks"
set size square
set xrange [-40:40]
set yrange [-40:40]
set tics in
set xzeroaxis lt -1 lc "black"
set yzeroaxis lt -1 lc "black"
plot "data/2d-steps.dat" i 0 w l lw 0.8 notitle, \
     "data/2d-steps.dat" i 1 w l lw 0.8 notitle, \
     "data/2d-steps.dat" i 2 w l lw 0.8 notitle, \
     "data/2d-steps.dat" i 3 w l lw 0.8 notitle, \
     "data/2d-steps.dat" i 4 w l lw 0.8 notitle, \
     "data/2d-steps.dat" i 5 w l lw 0.8 notitle, \
     "data/2d-steps.dat" i 6 w l lw 0.8 notitle

set title "Distance vs. Steps"
set size square
set xrange [0:300]
set yrange [0:300]
set xlabel "{/Symbol \326}N"
set ylabel "R"
set grid
set key left top
set key spacing 1.2
plot "data/2d-distance.dat" u 1:2 w l lc "red" lw 1.5 title "Simulation", \
     x w l lc rgb "blue" lw 4 title "Theory"

unset multiplot
