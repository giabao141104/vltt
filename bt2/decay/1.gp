reset
set terminal pngcairo size 800,400
set output "images/1-gnuplot.png"
set title "Do thi Logarit cua so hat va toc do phan ra (Gnuplot)"
set xlabel "Thoi gian (t)"
set ylabel "Gia tri Logarit"
set grid
set key outside

plot "data/phong_xa_data.dat" u 1:(log($2)) with lines title "ln(N(t))" lw 2, \
     "data/phong_xa_data.dat" u 1:(log($3 + 1e-9)) with lines title "ln(Delta N / Delta t)" lw 1.5
    
