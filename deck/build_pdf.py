"""Build the PDF reading copy from the reviewed slide PNGs.

Usage: python3 deck/build_pdf.py /absolute/path/to/rendered-slides
Requires reportlab. The editable original is the accompanying PowerPoint.
"""
from pathlib import Path
import argparse
from reportlab.pdfgen import canvas

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('rendered_slides', type=Path)
args = parser.parse_args()
slides = [args.rendered_slides / f'slide-{i}.png' for i in range(1, 17)]
missing = [str(p) for p in slides if not p.is_file()]
if missing:
    raise FileNotFoundError(', '.join(missing))
output = Path(__file__).resolve().parent / 'AI-Incumbent-Portfolio.pdf'
pdf = canvas.Canvas(str(output), pagesize=(960, 540), pageCompression=1)
pdf.setTitle('AI Incumbent Portfolio | The incumbent advantage')
pdf.setAuthor('AI Incumbent Portfolio')
pdf.setSubject('Research universe v0.1 | 11 September 2026')
for number, slide in enumerate(slides, 1):
    pdf.drawImage(str(slide), 0, 0, width=960, height=540)
    pdf.bookmarkPage(f'slide-{number}')
    pdf.addOutlineEntry(f'Slide {number}', f'slide-{number}', level=0)
    if number == 16:
        pdf.linkURL('https://github.com/Darainer/AI-incumbent-Portfolio',
                    (280, 119, 906, 169), relative=0)
    pdf.showPage()
pdf.save()
print(output)
