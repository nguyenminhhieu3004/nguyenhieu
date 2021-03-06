quickSort <- function(arr) {
  mid <- sample(arr, 1)
  left <- c()
  right <- c()
  lapply(arr[arr != mid], function(d) {
    if (d < mid) {
      left <<- c(left, d)
    }
    else {
      right <<- c(right, d)
    }
  })
  
  if (length(left) > 1) {
    left <- quickSort(left)
  }
  
  if (length(right) > 1) {
    right <- quickSort(right)
  }
  c(left, mid, right)
}
a = c(-35,6,7,1,0,398,1000,-99)
quickSort(a)