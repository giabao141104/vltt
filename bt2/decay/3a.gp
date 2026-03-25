reset
set terminal pngcairo size 800,500 enhanced font "serif,10"
set output "images/3a-gnuplot.png"

set title "3a. Do doc khong doi voi N0 khac nhau"
set xlabel "Thoi gian"
set ylabel "ln(N)"
set grid linestyle 0 lc rgb "gray80"
set key top right spacing 1.2
set tics in

plot "data/data_3a_N0_5000.dat"  u 1:(log($2)) w l lw 2 title "N0=5000", \
     "data/data_3a_N0_10000.dat" u 1:(log($2)) w l lw 2 title "N0=10000", \
     "data/data_3a_N0_20000.dat" u 1:(log($2)) w l lw 2 title "N0=20000"
