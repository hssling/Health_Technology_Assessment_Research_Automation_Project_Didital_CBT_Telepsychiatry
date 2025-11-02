# Vaccines HTA – literature processing
library(tidyverse)
dir.create("output", showWarnings = FALSE)
if (file.exists("data/vaccines_search_results.csv")) {
  refs <- read_csv("data/vaccines_search_results.csv")
  refs_clean <- refs %>% distinct(title, .keep_all = TRUE)
  write_csv(refs_clean, "output/vaccines_screening_sheet.csv")
} else {
  tibble(title=character(), year=integer(), source=character()) %>%
    write_csv("output/vaccines_screening_sheet.csv")
}
