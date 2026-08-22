.libPaths("D:/R_依赖包")
library(phyloseq)
library(ggplot2)
library(vegan)
data(GlobalPatterns)
ps <- GlobalPatterns
ps
sample_data(ps)
table(sample_data(ps)$SampleType)
ps_rel <- transform_sample_counts(ps, function(x) x / sum(x))
bray_dist <- distance(ps_rel, method = "bray")
pcoa <- ordinate(ps_rel, method = "PCoA", distance = bray_dist)
head(pcoa$values$Relative_eig * 100, 5)
p <- plot_ordination(
    ps_rel,
    pcoa,
    color = "SampleType",
    shape = "SampleType"
) +
    geom_point(size = 3, alpha = 0.8) +
    stat_ellipse(type = "norm", level = 0.95) +
    theme_bw(base_size = 12) +
    labs(
        title = "PCoA - Bray-Curtis Distance",
        subtitle = paste0(
            "PCoA1: ", round(pcoa$values$Relative_eig[1] * 100, 1), "%  |  ",
            "PCoA2: ", round(pcoa$values$Relative_eig[2] * 100, 1), "%"
        ),
        x = paste0("PCoA 1 (", round(pcoa$values$Relative_eig[1] * 100, 1), "%)"),
        y = paste0("PCoA 2 (", round(pcoa$values$Relative_eig[2] * 100, 1), "%)"),
        color = "样本类型",
        shape = "样本类型"
    ) +
    theme(
        legend.position = "right",
        plot.title = element_text(hjust = 0.5, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, color = "gray40")
    )

print(p)
ggsave("PCoA_BrayCurtis_SampleType.png", p, width = 9, height = 6, dpi = 150)
bray_mat <- as.matrix(bray_dist)
meta <- data.frame(sample_data(ps_rel))
set.seed(42)
permanova <- adonis2(bray_mat ~ SampleType, data = meta, permutations = 999)
cat("\n=== PERMANOVA 结果 ===\n")
print(permanova)

message("\n 图片已保存为 PCoA_BrayCurtis_SampleType.png")
