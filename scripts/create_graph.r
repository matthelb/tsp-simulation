f_n <- function(data_frame) {
  return (abs((data_frame$T.../1000 - data_frame$T../1000) - (data_frame$T./1000 - data_frame$T/1000))) 
}

read_csvs <- function(n, dir, x, y) {
  for (file in list.files(dir)) {
    dat <- read.csv(file)
    x <- c(x, n)
    y <- c(y, mean(f_n(dat)))
  }
  return (list(x, y))
}
