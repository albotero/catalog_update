#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os
import re

def get_fruits():
    res = {}

    for filename in os.listdir():
        with open(filename, 'r') as file:
            if not re.search(r'\.txt$', filename):
                continue
            name = file.readline().strip()
            qty = file.readline().strip()
            res[name] = qty

    return res

def generate_report(src, filename, title):
    os.chdir(src)

    report = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    final = []
    empty_line = Spacer(1,20)

    final.append(Paragraph(title, styles["h1"]))

    for fruit, qty in get_fruits().items():
        final.append(empty_line)
        final.append(Paragraph('name: ' + fruit, styles['BodyText']))
        final.append(Paragraph('weight: ' + qty, styles['BodyText']))

    report.build(final)
