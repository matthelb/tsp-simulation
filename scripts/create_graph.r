library(tools)

f_n <- function(data_frame) {
  return (abs((data_frame$T.../1000 - data_frame$T../1000) - (data_frame$T./1000 - data_frame$T/1000))) 
}

read_csvs <- function(dir) {
  x <- c()
  y <- c()
  for (file in list.files(dir)) {
    dat <- read.csv(file)
    x <- c(x, as.integer(basename(file_path_sans_ext(file))))
    y <- c(y, mean(f_n(dat)))
  }
  return (list(x, y))
}
