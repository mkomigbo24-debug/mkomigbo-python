from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
c = canvas.Canvas("MkomIgbo_CH_Fallacy_Thesis.pdf", pagesize=A4)
c.setFont("Helvetica-Bold", 20)
c.drawString(1*inch, 10*inch, "MKOM IGBO - CH FALLACY PROOF")
c.setFont("Helvetica", 12)
c.drawString(1*inch, 9.5*inch, "Thesis: Standard 36-letter Igbo orthography collapsed distinct phonemes")
c.drawString(1*inch, 9.2*inch, "Core Proof: cuo /kʷo/ (mould soil) - u is labialization /ʷ/ not vowel")
c.drawString(1*inch, 8.9*inch, "Therefore ch = c + h (aspiration), NOT a single letter!")
c.drawString(1*inch, 8.5*inch, "Missing: zh /ʒ/ azhịa (market), gh /ɣ/ aghara, ts /t͡s/ tsara (answer)")
c.drawString(1*inch, 8.2*inch, "Tone: ákwá (egg) vs àkwà (cloth) vs ákwà (cry) - meaning changes")
c.drawString(1*inch, 7.8*inch, "Platform: mkomigbo.com - 6 domains, 43 present alphabets")
c.drawString(1*inch, 7.5*inch, "Built: Aba, Abia State, NG - 2026")
c.drawString(1*inch, 7.0*inch, "GitHub: github.com/mkomigbo24-debug/mkomigbo-python")
c.drawString(1*inch, 6.5*inch, "Live: 127.0.0.1:8000/ - 200 OK - All 6 apps working")
c.save()
print("PDF created: MkomIgbo_CH_Fallacy_Thesis.pdf")