install.packages('igraph')
library(igraph)
help(graph)
vo_huong <-make_graph( ~ A-B-C-D-A, E-A:B:C:D)
plot(vo_huong)

