""" 
This code performs visualization of the results of the admixture analysis for the wolf and dog genomic data. 
The script reads the data from the ADMIXTURE analysis (.qopt file), organizes the samples into groups according to their origin (e.g. DOG, WOLF_SK, etc.), 
and produces a bar chart showing the admixture proportions for each sample.
The code also adds spaces between groups for better visual separation and labels each group with a box and label.
"""

# q <- read.table("../result_filtred4/merged_wolves_all_gl_ngs_rep2_k3.qopt")
# q <- read.table("../result_filtred4/merged_wolves_all_gl_ngs_rep2_k3.qopt")
# q <- read.table("../result_filtred4/merged_wolves_all_gl_ngs_rep6_k4.qopt")
# q <- read.table("../result_filtred4/merged_wolves_all_gl_ngs_rep2_k3.qopt")
# q <- read.table("../result_filtred4/merged_wolves_all_gl_ngs_rep1_k5.qopt")
# q <- read.table("../result_filtred4/merged_wolves_all_gl_ngs_rep2_k6.qopt")

q <- read.table("../result_filtred4/merged_wolves_all_gl_ngs_rep8_k8.qopt")
pop2 <- read.table("../new_id_filtred.txt", header = FALSE)

# group identification by prefix (e.g. DOG, WOLF_SK, etc.)
create_labels <- function(names) {
  sapply(names, function(name) {
    if (grepl("DOG", name)) {
      return("DOG")
    } else if (grepl("HYBRID_F1", name)) {
      return("HYBRID_F1")
    } else if (grepl("HYBRID_F2", name)) {
      return("HYBRID_F2")
    } else if (grepl("WOLF_CZ", name)) {
      return("WOLF_CZ")
    } else if (grepl("WOLF_DE", name)) {
      return("WOLF_DE")
    } else if (grepl("WOLF_PL", name)) {
      return("WOLF_PL")
    } else if (grepl("WOLF_SK", name)) {
      return("WOLF_SK")
    } else if (grepl("WOLF_UA", name)) {
      return("WOLF_UA")
    } else if (grepl("WOLF_IT", name)) {
      return("WOLF_IT")
    } else if (grepl("WOLF_AT", name)) {
      return("WOLF_AT")
    } else {
      return(name)
    }
  })
}

# using the function to create labels
labels <- create_labels(pop2$V1)

# data arrangement based on groups
unique_labels <- unique(labels)
ord <- order(match(labels, unique_labels))
q_ordered <- q[ord, ]
labels_ordered <- labels[ord]
pop2_ordered <- pop2$V1[ord]

# adding empty columns between groups
q_with_spaces <- c()
labels_with_spaces <- c()
last_label <- labels_ordered[1]
frame_positions <- list(start = integer(), end = integer())
group_start <- 1  # inicializace startu skupiny

for (i in seq_len(length(labels_ordered))) {
  current_label <- labels_ordered[i]
  if (current_label != last_label) {
    q_with_spaces <- rbind(q_with_spaces, rep(NA, ncol(q_ordered)))  # přidání prázdného řádku
    labels_with_spaces <- c(labels_with_spaces, "")  # prázdný label pro zajištění oddělení skupin
    frame_positions$end <- c(frame_positions$end, nrow(q_with_spaces) - 1)  # ukládá konec skupiny
    frame_positions$start <- c(frame_positions$start, nrow(q_with_spaces) + 1)  # ukládá začátek nové skupiny
    group_start <- nrow(q_with_spaces) + 1  # aktualizace startu nové skupiny
    last_label <- current_label  # aktualizace posledního labelu
  }
  q_with_spaces <- rbind(q_with_spaces, q_ordered[i, ])
  labels_with_spaces <- c(labels_with_spaces, "")
}

frame_positions$end <- c(frame_positions$end, nrow(q_with_spaces))  # pozice pro konec poslední skupiny

# generating PDF
pdf("plot_K8_combined__.pdf", width=18, height=8)
par(mar=c(10, 5, 2, 1))  # nastavení okrajů pro lepší čitelnost popisků

# creating a barplot with gaps between groups
bp <- barplot(t(q_with_spaces), 
              col = 1:10, 
              names.arg = labels_with_spaces, 
              las = 2, 
              space = 0, 
              border = NA, 
              ylab = "Admixture proportions for K=8", 
              cex.names = 0.6)

# adding labels and frames around groups
for (i in seq_along(frame_positions$start)) {
  group_start <- frame_positions$start[i]
  group_end <- frame_positions$end[i]
  rect(bp[group_start] - 0.5, -0.05, bp[group_end] + 0.5, 1.05, border = "black", lwd = 2)
  

  group_start <- frame_positions$end[i-1]
  group_end <- frame_positions$start[i]
  if (i == 1)
  {
    group_start <- 1
    group_end <- frame_positions$start[i]
  }
  print(i)
  print(group_start)
  print(group_end)
  print(mean(c(bp[group_start], bp[group_end])))
  text(mean(c(bp[group_start], bp[group_end])), -0.1, labels=unique_labels[i], xpd=TRUE, srt = 45, adj = 1, cex=1.2)
}
  group_start <- 119
  group_end <- 119
text(mean(c(bp[group_start], bp[group_end])), -0.1, labels="WOLF_AT", xpd=TRUE, srt = 45, adj = 1, cex=1.2)

dev.off()
