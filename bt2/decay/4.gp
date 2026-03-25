reset
set terminal pngcairo size 700,600 enhanced font "serif,10"
set output "images/4-gnuplot.png"

set title "Yeu cau 4: ln(delta N) ti le thuan voi ln(N)"
set xlabel "ln(N)"
set ylabel "ln(delta N)"

set grid
set key bottom right

lambda = 0.005
theory(x) = x + log(lambda)

plot "data/data_4_lnN_lnDN.dat" u 1:2 with points pt 7 ps 0.4 lc rgb "red" title "Simulation Data", \
     theory(x) with lines lw 2 dt 2 lc rgb "black" title "Ly thuyet (Slope=1)"
