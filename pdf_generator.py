from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
import tempfile

def make_weekly_pdf(username, start, end, steps_by_day, water_ml):
    path = Path(tempfile.gettempdir()) / f'nutriwell_report_{start.isoformat()}_{end.isoformat()}.pdf'
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=1.8*cm, leftMargin=1.8*cm, topMargin=1.8*cm, bottomMargin=1.8*cm)
    styles = getSampleStyleSheet()
    story = [Paragraph('NutriWell — Weekly Activity Report', styles['Title']), Spacer(1, 10),
             Paragraph(f'User: {username}', styles['Normal']),
             Paragraph(f'Period: {start.isoformat()} to {end.isoformat()}', styles['Normal']), Spacer(1, 14)]
    data = [['Date', 'Recorded steps']] + [[day, f'{steps:,}'] for day, steps in steps_by_day.items()]
    table = Table(data, colWidths=[8*cm, 6*cm])
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1f6b4f')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.5,colors.lightgrey),('PADDING',(0,0),(-1,-1),8)]))
    story.extend([table, Spacer(1, 14), Paragraph(f'Total recorded steps: {sum(steps_by_day.values()):,}', styles['Heading2']),
                  Paragraph(f'Total water logged: {water_ml/1000:.1f} litres. This is a record of entries, not a prescribed hydration target.', styles['Normal']), Spacer(1, 14),
                  Paragraph('Note: The report summarizes recorded data only. NutriWell is not a substitute for medical advice.', styles['Italic'])])
    doc.build(story)
    return str(path)
