reset
set terminal pngcairo size 800,500 enhanced font "serif,10"
set output "images/3b-gnuplot.png"

set title "3b. Do doc thay doi theo Lambda"
set xlabel "Thoi gian"
set ylabel "ln(N)"
set grid linestyle 0 lc rgb "gray80"
set key top right spacing 1.2
set tics in

plot "data/data_3b_lambda_0.005.dat" u 1:(log($2)) w l lw 2 title "lambda=0.005", \
     "data/data_3b_lambda_0.01.dat"   u 1:(log($2)) w l lw 2 title "lambda=0.01", \
     "data/data_3b_lambda_0.015.dat"  u 1:(log($2)) w l lw 2 title "lambda=0.015"
