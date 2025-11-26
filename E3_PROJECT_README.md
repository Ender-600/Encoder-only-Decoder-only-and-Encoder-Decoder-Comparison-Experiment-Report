# E³-Mini Benchmark: Project Page

## Overview

This is a high-quality academic project page for the **E³ Mini-Benchmark** research project, which evaluates transformer architectures across three dimensions:
- **Efficiency** (Throughput & Latency)
- **Energy** (Power & Carbon Footprint)  
- **Effectiveness** (Accuracy & Generalization)

## 🎯 What's Been Implemented

### ✅ Complete Sections

1. **Hero Section**
   - Project title: "E³-Mini Benchmark: The End Game of Architecture Wars?"
   - Subtitle emphasizing the three-dimensional evaluation
   - Author placeholders (customize with your names)
   - Quick links: Paper (PDF), Code (GitHub), Data (HuggingFace)

2. **Teaser Figure**
   - Replaced video with a key Pareto Frontier plot
   - Caption explaining the "Generality Tax" (5×-10× energy premium)

3. **Abstract**
   - Comprehensive summary of core findings
   - Three key phenomena highlighted:
     - The Generality Tax
     - The KV-Cache Bottleneck
     - Sample Inefficiency

4. **Methodology (E³ Framework)**
   - Three beautiful gradient cards explaining each dimension
   - Visual hierarchy with icons and clear metrics

5. **Experimental Results**
   - **Experiment 1:** Energy comparison (classification task)
   - **Experiment 2:** VRAM scaling (context stress test)
   - **Experiment 3:** Training convergence (loss curves)
   - Each experiment includes:
     - Visual placeholder for chart/graph
     - Key insight summary
     - Practical implication callout box

6. **Key Takeaways**
   - Four-quadrant summary with recommendations
   - Icon-enhanced sections for readability

7. **BibTeX Citation**
   - Pre-formatted citation for the 2025 publication
   - Copy-to-clipboard functionality

8. **SEO & Meta Tags**
   - Comprehensive Open Graph tags for social sharing
   - Twitter Card metadata
   - Academic citation metadata (Google Scholar compatibility)
   - Structured JSON-LD data for search engines

### 🗑️ Removed/Commented Out

- "More Works" dropdown (can be re-enabled if needed)
- Poster section (uncomment in HTML if you have a poster PDF)
- Video carousel section

## 📂 Project Structure

```
Encoder-only-Decoder-only-and-Encoder-Decoder-Comparison-Experiment-Report/
├── index.html                  # Main project page (READY TO USE)
├── E3_PROJECT_README.md        # This file
├── IMAGE_PLACEHOLDERS.md       # Guide for creating visualizations
├── static/
│   ├── css/                    # Stylesheets (Bulma framework)
│   ├── js/                     # JavaScript for interactions
│   ├── images/                 # 📊 ADD YOUR VISUALIZATIONS HERE
│   │   ├── pareto_frontier.png         (Teaser image)
│   │   ├── results_energy.png          (Experiment 1)
│   │   ├── results_vram.png            (Experiment 2)
│   │   └── results_loss_curves.png     (Experiment 3)
│   ├── pdfs/                   # 📄 ADD YOUR PAPER HERE
│   │   └── e3_benchmark_paper.pdf
│   └── videos/                 # (Optional)
```

## 🚀 Quick Start Guide

### Step 1: Customize Author Information

Open `index.html` and find these lines (~line 247):

```html
<span class="author-block">
  <a href="#" target="_blank">Your Name</a><sup>1</sup>,</span>
```

Replace with your actual names and links (personal websites, Google Scholar, etc.).

### Step 2: Update Institution & Links

Find these sections:
- Institution name (~line 261)
- GitHub repository URL (~line 297)
- HuggingFace dataset URL (~line 304)
- PDF paper path (~line 291)

### Step 3: Add Visualizations

See `IMAGE_PLACEHOLDERS.md` for detailed instructions on creating:
1. Pareto Frontier plot (main teaser)
2. Energy comparison bar chart
3. VRAM scaling line graph
4. Training loss curves

**Quick placeholder generation:**
```bash
cd static/images/
# Using placeholder service temporarily
curl -o pareto_frontier.png "https://via.placeholder.com/1200x600/667eea/FFFFFF?text=Pareto+Frontier"
curl -o results_energy.png "https://via.placeholder.com/1000x600/f093fb/FFFFFF?text=Energy+Results"
curl -o results_vram.png "https://via.placeholder.com/1000x600/4facfe/FFFFFF?text=VRAM+Scaling"
curl -o results_loss_curves.png "https://via.placeholder.com/1000x600/34d399/FFFFFF?text=Loss+Curves"
```

### Step 4: Add Your Paper PDF

```bash
cp /path/to/your/paper.pdf static/pdfs/e3_benchmark_paper.pdf
```

### Step 5: Test Locally

```bash
# Simple HTTP server
cd /Users/maxwell/Encoder-only-Decoder-only-and-Encoder-Decoder-Comparison-Experiment-Report
python3 -m http.server 8000

# Then open: http://localhost:8000
```

### Step 6: Deploy

**Option A: GitHub Pages** (Recommended)
```bash
git init
git add .
git commit -m "Initial commit: E³ Mini-Benchmark project page"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/e3-benchmark.git
git push -u origin main

# Enable GitHub Pages in repository settings
# Your site will be at: https://YOUR_USERNAME.github.io/e3-benchmark/
```

**Option B: Netlify**
1. Drag & drop the entire folder to [netlify.com/drop](https://app.netlify.com/drop)
2. Get instant URL like `https://e3-benchmark-xyz.netlify.app`

**Option C: Vercel**
```bash
npm install -g vercel
vercel deploy
```

## 🎨 Design Features

- **Responsive Design:** Works perfectly on mobile, tablet, and desktop
- **Modern Gradients:** Purple, pink, and blue themes matching ML research aesthetics
- **Accessibility:** ARIA labels, semantic HTML, keyboard navigation
- **Performance:** Lazy loading images, deferred JavaScript, preconnect hints
- **SEO Optimized:** Meta tags for Google Scholar, Twitter, Facebook

## 📝 Customization Tips

### Changing Colors

Find the gradient definitions in the Methodology section (~line 355):

```html
<!-- Efficiency (Purple) -->
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

<!-- Energy (Pink/Red) -->
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);

<!-- Effectiveness (Blue) -->
background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
```

Replace hex codes with your preferred colors.

### Adding More Experiments

Copy the experiment box template (~line 404) and modify:

```html
<div class="box" style="margin-bottom: 3rem; border-radius: 12px;">
  <h3 class="title is-4">Experiment 4: Your Title</h3>
  <div class="columns">
    <div class="column is-two-thirds">
      <figure class="image">
        <img src="static/images/your_result.png" alt="Description"/>
      </figure>
    </div>
    <div class="column is-one-third">
      <div class="content">
        <p><strong>Key Insight:</strong> Your finding here</p>
      </div>
    </div>
  </div>
</div>
```

### Re-enabling "More Works" Dropdown

Uncomment lines 189-235 in `index.html` and update with your related papers.

## 🐛 Troubleshooting

### Images Not Loading
- Check file paths are relative: `static/images/filename.png`
- Ensure images are in correct directory
- Verify file extensions match (case-sensitive on Linux/Mac)

### Styling Looks Broken
- Ensure all CSS files are present in `static/css/`
- Check browser console for 404 errors
- Clear browser cache (Cmd+Shift+R on Mac)

### BibTeX Copy Button Not Working
- Ensure `static/js/index.js` is loaded
- Check browser console for JavaScript errors

## 📚 Technical Stack

- **Framework:** Bulma CSS (modern, responsive)
- **Icons:** Font Awesome 5
- **Academic Icons:** Academicons (arXiv, Google Scholar)
- **JavaScript:** Vanilla JS (no dependencies)
- **Fonts:** Inter (Google Fonts)

## 📄 License

This template is licensed under CC BY-SA 4.0. Credit to:
- [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template)
- [Nerfies](https://nerfies.github.io) (original inspiration)

## 🤝 Contributing

Found a bug or want to improve the template? 
1. Fork the repository
2. Make your changes
3. Submit a pull request

## 📧 Contact

For questions about the E³ Mini-Benchmark research:
- Email: your.email@institution.edu
- Twitter: @E3Benchmark
- GitHub Issues: [github.com/your-username/e3-benchmark/issues](https://github.com/your-username/e3-benchmark/issues)

---

**Built with ❤️ for transparent and reproducible ML research.**

