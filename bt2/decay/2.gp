reset
set terminal pngcairo size 800, 500
set output "images/2-gnuplot.png"

set title "Radioactive Decay: Stochastic (Small N) vs. Exponential (Large N)"
set xlabel "Time (t)"
set ylabel "log10[N(t)]"

set grid linestyle 0 lc rgb "gray80"
set key top right
set tics in

plot "data/ket_qua_tong_hop.dat" u 1:(log10($2)) w steps title "N0 = 10", \
     "data/ket_qua_tong_hop.dat" u 1:(log10($3)) w steps title "N0 = 100", \
     "data/ket_qua_tong_hop.dat" u 1:(log10($4)) w steps title "N0 = 1000", \
     "data/ket_qua_tong_hop.dat" u 1:(log10($5)) w steps title "N0 = 10000", \
     "data/ket_qua_tong_hop.dat" u 1:(log10($6)) w steps title "N0 = 100000"
