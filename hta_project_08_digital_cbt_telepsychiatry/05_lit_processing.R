# Digital CBT / Tele-psychiatry HTA – literature processing
library(tidyverse)
dir.create("output", showWarnings = FALSE)
if (file.exists("data/digital_cbt_search_results.csv")) {
  refs <- read_csv("data/digital_cbt_search_results.csv")
  refs_clean <- refs %>% distinct(title, .keep_all = TRUE)
  write_csv(refs_clean, "output/digital_cbt_screening_sheet.csv")
} else {
  tibble(title=character(), year=integer(), source=character()) %>%
    write_csv("output/digital_cbt_screening_sheet.csv")
}
