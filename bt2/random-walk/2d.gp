reset
set terminal windows size 1100, 500 font "Serif,10"
set multiplot layout 1, 2 title "Random Walk 2D"

set title "7 Random Walks"
set size square
set xrange [-40:40]
set yrange [-40:40]
set tics in
set xzeroaxis lt -1 lc "black"
set yzeroaxis lt -1 lc "black"
plot "random_walk_2D.dat" i 0 w l lw 0.8 notitle, \
     "random_walk_2D.dat" i 1 w l lw 0.8 notitle, \
     "random_walk_2D.dat" i 2 w l lw 0.8 notitle, \
     "random_walk_2D.dat" i 3 w l lw 0.8 notitle, \
     "random_walk_2D.dat" i 4 w l lw 0.8 notitle, \
     "random_walk_2D.dat" i 5 w l lw 0.8 notitle, \
     "random_walk_2D.dat" i 6 w l lw 0.8 notitle

set title "Distance vs. Steps"
set size square
set xrange [0:300]
set yrange [0:300]
set xlabel "{/Symbol \326}N"
set ylabel "R"
set grid
set key left top
set key spacing 1.2
plot "rw_2D.dat" u 1:2 w l lc "red" lw 1.5 title "Simulation", \
     x w l lc rgb "blue" lw 4 title "Theory" alpha 0.5

unset multiplot
pause mouse close