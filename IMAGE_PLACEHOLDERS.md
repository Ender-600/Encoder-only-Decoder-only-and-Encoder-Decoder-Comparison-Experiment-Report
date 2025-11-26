# Image Placeholders for E³ Mini-Benchmark Project

This document lists all the placeholder images referenced in the `index.html` file that you'll need to create or replace.

## Required Images

### 1. **Pareto Frontier Plot** (Hero/Teaser Section)
- **Path:** `static/images/pareto_frontier.png`
- **Description:** Scatter plot showing Accuracy (Y-axis) vs. Energy Consumption (X-axis)
- **Content:** 
  - Blue dots/markers: Encoder-only models (BERT)
  - Red dots/markers: Decoder-only models (GPT-2)
  - Green dots/markers (optional): Encoder-Decoder models (T5)
  - Should clearly show the 5×-10× energy gap
- **Dimensions:** ~900-1200px wide, high-quality
- **Purpose:** Main hero image that captures the core finding

---

### 2. **Energy Comparison Bar Chart** (Experiment 1)
- **Path:** `static/images/results_energy.png`
- **Description:** Bar chart comparing energy consumption per sample
- **Content:**
  - X-axis: Model types (BERT vs GPT-2 vs T5)
  - Y-axis: Energy per sample (Joules or Wh)
  - Should show ~8.7× difference between BERT and GPT-2
- **Dimensions:** ~800-1000px wide
- **Purpose:** Visualize "The Cost of Generality"

---

### 3. **VRAM Growth Curve** (Experiment 2)
- **Path:** `static/images/results_vram.png`
- **Description:** Line graph showing VRAM usage vs. context length
- **Content:**
  - X-axis: Context length (tokens: 512, 1K, 2K, 4K, 8K)
  - Y-axis: VRAM usage (GB)
  - Blue line: Encoder-only (linear growth)
  - Red line: Decoder-only (exponential growth, OOM marker at 4K)
  - Horizontal line indicating V100 memory limit (~16GB)
- **Dimensions:** ~800-1000px wide
- **Purpose:** Demonstrate "The KV-Cache Bottleneck"

---

### 4. **Training Loss Curves** (Experiment 3)
- **Path:** `static/images/results_loss_curves.png`
- **Description:** Multi-line graph showing normalized loss over training steps
- **Content:**
  - X-axis: Training steps (0-5000)
  - Y-axis: Normalized validation loss
  - Multiple colored lines for different architectures
  - BERT should converge ~2× faster than GPT-2
- **Dimensions:** ~800-1000px wide
- **Purpose:** Show training efficiency differences

---

### 5. **Social Preview Image** (Optional, for SEO)
- **Path:** `static/images/social_preview.png`
- **Description:** Open Graph preview image for social media sharing
- **Content:** Eye-catching visual with project title and key metric
- **Dimensions:** 1200×630px (Facebook/Twitter requirement)
- **Purpose:** Better link previews when shared on social media

---

## Quick Generation Tips

### Using Python (Matplotlib/Seaborn)
```python
import matplotlib.pyplot as plt
import numpy as np

# Example: Pareto Frontier
fig, ax = plt.subplots(figsize=(10, 6))
# Encoder-only (BERT variants)
bert_energy = [1.2, 1.5, 2.1]
bert_accuracy = [88.5, 89.2, 90.1]
ax.scatter(bert_energy, bert_accuracy, s=150, c='blue', label='Encoder-only', alpha=0.7)

# Decoder-only (GPT-2 variants)
gpt_energy = [8.5, 10.2, 12.7]
gpt_accuracy = [87.8, 89.5, 90.3]
ax.scatter(gpt_energy, gpt_accuracy, s=150, c='red', label='Decoder-only', alpha=0.7)

ax.set_xlabel('Energy Consumption (Wh)', fontsize=14)
ax.set_ylabel('Accuracy (%)', fontsize=14)
ax.set_title('Accuracy vs Energy: The Generality Tax', fontsize=16, fontweight='bold')
ax.legend(fontsize=12)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('static/images/pareto_frontier.png', dpi=150, bbox_inches='tight')
```

### Using R (ggplot2)
```r
library(ggplot2)
data <- data.frame(
  model = c(rep("BERT", 3), rep("GPT-2", 3)),
  energy = c(1.2, 1.5, 2.1, 8.5, 10.2, 12.7),
  accuracy = c(88.5, 89.2, 90.1, 87.8, 89.5, 90.3)
)
ggplot(data, aes(x=energy, y=accuracy, color=model)) +
  geom_point(size=5, alpha=0.7) +
  labs(title="Accuracy vs Energy: The Generality Tax",
       x="Energy Consumption (Wh)", y="Accuracy (%)") +
  theme_minimal(base_size=14)
ggsave("static/images/pareto_frontier.png", width=10, height=6, dpi=150)
```

### Using Online Tools
- **Plotly Chart Studio:** https://chart-studio.plotly.com/
- **Flourish:** https://flourish.studio/
- **Datawrapper:** https://www.datawrapper.de/

---

## Color Scheme Recommendations

To maintain visual consistency with the website's gradient themes:

- **Encoder-only (BERT):** `#667eea` → `#764ba2` (Purple gradient)
- **Decoder-only (GPT-2):** `#f093fb` → `#f5576c` (Pink/Red gradient)
- **Encoder-Decoder (T5):** `#4facfe` → `#00f2fe` (Blue/Cyan gradient)
- **Background:** White or light gray (`#f7fafc`)
- **Text:** Dark gray (`#2d3748`)

---

## Fallback: Using Placeholder Services

If you need temporary placeholders while creating actual visualizations:

```bash
# Download colored placeholders
curl -o static/images/pareto_frontier.png "https://via.placeholder.com/1200x600/667eea/FFFFFF?text=Pareto+Frontier+Plot"
curl -o static/images/results_energy.png "https://via.placeholder.com/1000x600/f093fb/FFFFFF?text=Energy+Comparison"
curl -o static/images/results_vram.png "https://via.placeholder.com/1000x600/4facfe/FFFFFF?text=VRAM+Scaling"
curl -o static/images/results_loss_curves.png "https://via.placeholder.com/1000x600/34d399/FFFFFF?text=Loss+Curves"
```

---

## Next Steps

1. ✅ HTML structure is complete
2. 📊 Create/gather experimental result visualizations
3. 🎨 Replace placeholder images in `static/images/`
4. 📄 Add actual PDF paper to `static/pdfs/e3_benchmark_paper.pdf`
5. 🔗 Update GitHub and HuggingFace links with real URLs
6. 🚀 Deploy to hosting platform (GitHub Pages, Netlify, Vercel, etc.)

---

**Note:** All image paths use relative URLs, so you can test locally by opening `index.html` in a browser once you've placed images in the correct directories.

