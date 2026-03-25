
set title "Do thi Logarit cua so hat va toc do phan ra (Gnuplot)"
set xlabel "Thoi gian (t)"
set ylabel "Gia tri Logarit"
set grid
set key outside

plot "phong_xa_data.dat" u 1:(log($2)) with lines title "ln(N(t))" lw 2, \
     "phong_xa_data.dat" u 1:(log($3 + 1e-9)) with lines title "ln(Delta N / Delta t)" lw 1.5
    