reset
set terminal windows size 1100, 500 font "Serif,10"
set multiplot layout 1, 2 title "Random Walk 3D"

set title "7 Random Walks (3D Paths)"
set border 4095 lc "black" lw 0.5

unset wall

set xyplane at 0
set view 60, 30, 1.0, 1.0
set size square

set xrange [-40:40]
set yrange [-40:40]
set zrange [-40:40]
set xtics 20
set ytics 20
set ztics 20

set xlabel "X"
set ylabel "Y"
set zlabel "Z"

set grid lc "gray" lt 1 lw 0.2

splot "walks_3D.dat" i 0 w l lw 1.2 notitle, \
      "walks_3D.dat" i 1 w l lw 1.2 notitle, \
      "walks_3D.dat" i 2 w l lw 1.2 notitle, \
      "walks_3D.dat" i 3 w l lw 1.2 notitle, \
      "walks_3D.dat" i 4 w l lw 1.2 notitle, \
      "walks_3D.dat" i 5 w l lw 1.2 notitle, \
      "walks_3D.dat" i 6 w l lw 1.2 notitle

set title "Distance R vs sqrt(N)"
set size square
set xrange [0:300]
set yrange [0:300]
set xtics 100
set ytics 100
set xlabel "{/Symbol \326}N"
set ylabel "R"
set grid lc "gray" lt 1 lw 0.2

set key left top
set key spacing 1.2

plot "rw_3D.dat" u 1:2 w l lc "red" lw 1.5 title "Simulation", \
     x w l lc "blue" lw 3 title "Theory" alpha 0.5

unset multiplot
pause mouse close