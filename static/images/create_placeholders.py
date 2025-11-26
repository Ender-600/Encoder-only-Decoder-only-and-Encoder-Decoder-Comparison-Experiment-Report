from PIL import Image, ImageDraw, ImageFont
import sys

def create_placeholder(filename, width, height, color, text):
    # Create image with colored background
    img = Image.new('RGB', (width, height), color=color)
    draw = ImageDraw.Draw(img)
    
    # Add text
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box and center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    draw.text(position, text, fill='white', font=font)
    img.save(filename)
    print(f"Created {filename}")

# Create placeholders
create_placeholder('pareto_frontier.png', 1200, 600, '#667eea', 'Pareto Frontier Plot\n(Replace with actual)')
create_placeholder('results_energy.png', 1000, 600, '#f093fb', 'Energy Comparison\n(Experiment 1)')
create_placeholder('results_vram.png', 1000, 600, '#4facfe', 'VRAM Scaling\n(Experiment 2)')
create_placeholder('results_loss_curves.png', 1000, 600, '#34d399', 'Loss Curves\n(Experiment 3)')

print("\n✓ All placeholder images created!")
