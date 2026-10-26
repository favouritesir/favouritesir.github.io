import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls
from pathlib import Path

BASE_DIR = Path(r"D:\Drive\gub221902131\My Drive\my\Code\GITHUB\favouritesir.github.io")
OUT_DOCX_DOWNLOADS = Path(r"D:\Downloads\CV of Ashikur Rahman.docx")
OUT_DOCX_PORTFOLIO = BASE_DIR / "assets" / "cv" / "CV of Ashikur Rahman.docx"
PHOTO_PATH = BASE_DIR / "assets" / "img" / "ashikur_rahman.png"

# Color Palette: Deep Teal & Charcoal Slate
COLOR_PRIMARY = RGBColor(15, 118, 110)      # #0f766e Teal
COLOR_DARK = RGBColor(15, 23, 42)          # #0f172a Slate dark
COLOR_MUTED = RGBColor(71, 85, 105)        # #475569 Muted
COLOR_TEAL_HEX = "0f766e"
COLOR_LIGHT_BG_HEX = "f0fdfa"
COLOR_BORDER_HEX = "cbd5e1"

def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def add_hyperlink(paragraph, url, text, color=COLOR_TEAL_HEX, underline=True, bold=False):
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)
    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    if color:
        c = OxmlElement('w:color')
        c.set(qn('w:val'), color)
        rPr.append(c)
    if underline:
        u = OxmlElement('w:u')
        u.set(qn('w:val'), 'single')
        rPr.append(u)
    if bold:
        b = OxmlElement('w:b')
        rPr.append(b)
    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink

def build_cv():
    doc = docx.Document()

    # Page Margins (0.5 inch / 36 pt for compact elegance)
    for section in doc.sections:
        section.top_margin = Inches(0.45)
        section.bottom_margin = Inches(0.45)
        section.left_margin = Inches(0.55)
        section.right_margin = Inches(0.55)

    # Styles Setup
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Segoe UI'
    normal_style.font.size = Pt(9.5)
    normal_style.font.color.rgb = COLOR_DARK

    # ==========================================
    # HEADER SECTION: Table with Name + Photo
    # ==========================================
    header_table = doc.add_table(rows=1, cols=2)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    header_table.autofit = False

    col_text, col_photo = header_table.rows[0].cells
    col_text.width = Inches(5.8)
    col_photo.width = Inches(1.4)
    col_photo.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    # Name & Title
    p_name = col_text.paragraphs[0]
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(2)
    run_name = p_name.add_run("ASHIKUR RAHMAN")
    run_name.font.size = Pt(20)
    run_name.font.bold = True
    run_name.font.color.rgb = COLOR_DARK

    p_title = col_text.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(6)
    run_title = p_title.add_run("Software Engineer • Algorithm Researcher • Systems Architect")
    run_title.font.size = Pt(10)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY

    # Clickable Contact Information Row
    p_contact = col_text.add_paragraph()
    p_contact.paragraph_format.space_before = Pt(0)
    p_contact.paragraph_format.space_after = Pt(4)
    p_contact.paragraph_format.line_spacing = 1.25

    p_contact.add_run("🌐 Portfolio: ")
    add_hyperlink(p_contact, "http://favouritesir.me", "favouritesir.me", bold=True)
    p_contact.add_run("  •  ✉️ ")
    add_hyperlink(p_contact, "mailto:ashikur.gub@gmail.com", "ashikur.gub@gmail.com")
    p_contact.add_run("  •  📱 ")
    add_hyperlink(p_contact, "tel:+8801962579305", "+880 1962-579305")
    p_contact.add_run("\n🐙 GitHub: ")
    add_hyperlink(p_contact, "https://github.com/favouritesir", "github.com/favouritesir")
    p_contact.add_run("  •  💼 LinkedIn: ")
    add_hyperlink(p_contact, "https://linkedin.com/in/favouritesir", "linkedin.com/in/favouritesir")
    p_contact.add_run("  •  📍 Gazipur / Dhaka, Bangladesh")

    # Add Profile Photo
    if PHOTO_PATH.exists():
        p_photo = col_photo.paragraphs[0]
        p_photo.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_photo.paragraph_format.space_before = Pt(0)
        p_photo.paragraph_format.space_after = Pt(0)
        run_img = p_photo.add_run()
        run_img.add_picture(str(PHOTO_PATH), width=Inches(1.25))

    # Divider Line
    p_line = doc.add_paragraph()
    p_line.paragraph_format.space_before = Pt(4)
    p_line.paragraph_format.space_after = Pt(8)
    p_line_border = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="1" w:color="{COLOR_TEAL_HEX}"/></w:pBdr>')
    p_line._p.get_or_add_pPr().append(p_line_border)

    # Executive Summary
    p_summary = doc.add_paragraph()
    p_summary.paragraph_format.space_before = Pt(0)
    p_summary.paragraph_format.space_after = Pt(10)
    p_summary.paragraph_format.line_spacing = 1.15
    run_sum = p_summary.add_run(
        "Computer Science & Engineering graduate from Green University of Bangladesh. Conceived, proved, and published novel algorithmic paradigms indexed with permanent CERN/Zenodo DOIs. Architect of zero-cost, high-concurrency real-time cloud management platforms, developer NPM utilities, and embedded IoT networking firmware. Proven track record in academic mentorship, systems operations, and production software delivery."
    )
    run_sum.font.size = Pt(9.2)
    run_sum.font.color.rgb = COLOR_MUTED

    # Helper for Section Titles
    def add_section_header(title_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(f"■  {title_text.upper()}")
        run.font.size = Pt(10.5)
        run.font.bold = True
        run.font.color.rgb = COLOR_PRIMARY
        # Subtle bottom border
        bdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="1" w:color="{COLOR_BORDER_HEX}"/></w:pBdr>')
        p._p.get_or_add_pPr().append(bdr)

    # ==========================================
    # 1. PUBLISHED RESEARCH PREPRINTS (CERN / ZENODO DOIS)
    # ==========================================
    add_section_header("Published Research Preprints (CERN / Zenodo DOIs)")

    # Research Item 1
    p_r1 = doc.add_paragraph()
    p_r1.paragraph_format.space_before = Pt(2)
    p_r1.paragraph_format.space_after = Pt(1)
    run_r1_title = p_r1.add_run("Cloud Sort: An Overhead Caller-Buffer Merge Paradigm  |  ")
    run_r1_title.font.bold = True
    add_hyperlink(p_r1, "https://doi.org/10.5281/zenodo.23665548", "DOI: 10.5281/zenodo.23665548", bold=True)
    p_r1.add_run("  •  ")
    add_hyperlink(p_r1, "https://github.com/favouritesir/created_by_me/tree/main/%E2%9C%85%20cloud%20merge%20sort", "GitHub Benchmarks")

    p_r1_desc = doc.add_paragraph()
    p_r1_desc.paragraph_format.space_before = Pt(0)
    p_r1_desc.paragraph_format.space_after = Pt(6)
    p_r1_desc.paragraph_format.line_spacing = 1.15
    p_r1_desc.add_run(
        "• Conceived at Dept. of CSE, Green University of Bangladesh (Conceived 2023, Published Oct 2026).\n"
        "• Invented an asymmetric in-situ merge sort reducing auxiliary space to ⌈N/2⌉ elements with zero dynamic heap allocations (malloc/free).\n"
        "• Proved inductive read-before-write safety (wp_t ≤ rp_t) and formulated the Zero-Move Right Tail Property, eliminating 25.0% of physical SRAM data writes.\n"
        "• Verified across 10,000 differential random array trials against V8 TimSort and benchmarked on ATmega328P architecture."
    )
    p_r1_desc.runs[0].font.size = Pt(8.8)

    # Research Item 2
    p_r2 = doc.add_paragraph()
    p_r2.paragraph_format.space_before = Pt(3)
    p_r2.paragraph_format.space_after = Pt(1)
    run_r2_title = p_r2.add_run("An Optimal In-Situ Dual-Pointer Algorithm for Infix-to-Prefix Transformation  |  ")
    run_r2_title.font.bold = True
    add_hyperlink(p_r2, "https://doi.org/10.5281/zenodo.23657544", "DOI: 10.5281/zenodo.23657544", bold=True)
    p_r2.add_run("  •  ")
    add_hyperlink(p_r2, "https://github.com/favouritesir/created_by_me/tree/main/%E2%9C%85%20infix%20to%20prefix", "GitHub Source")

    p_r2_desc = doc.add_paragraph()
    p_r2_desc.paragraph_format.space_before = Pt(0)
    p_r2_desc.paragraph_format.space_after = Pt(8)
    p_r2_desc.paragraph_format.line_spacing = 1.15
    p_r2_desc.add_run(
        "• Conceived at Dept. of CSE, Green University of Bangladesh (Fall 2022, Published Oct 2026).\n"
        "• Formulated an optimal right-to-left single-pass conversion algorithm achieving O(1) auxiliary string space.\n"
        "• Eliminates conventional textbook triple-pass string reversal overhead, saving over 60% SRAM on embedded architectures."
    )
    p_r2_desc.runs[0].font.size = Pt(8.8)

    # ==========================================
    # 2. FEATURED PRODUCTION & ENGINEERING PROJECTS
    # ==========================================
    add_section_header("Featured Production & Engineering Projects")

    # Project 1: SUPER Fill
    p_p1 = doc.add_paragraph()
    p_p1.paragraph_format.space_before = Pt(2)
    p_p1.paragraph_format.space_after = Pt(1)
    run_p1_title = p_p1.add_run("SUPER Fill — Form Engine & Dynamic Workspace  |  ")
    run_p1_title.font.bold = True
    p_p1.add_run("IDP 1 Lab Project (CSE 324, Green University of Bangladesh)")

    p_p1_desc = doc.add_paragraph()
    p_p1_desc.paragraph_format.space_before = Pt(0)
    p_p1_desc.paragraph_format.space_after = Pt(6)
    p_p1_desc.paragraph_format.line_spacing = 1.15
    p_p1_desc.add_run(
        "• Cloud-native application integrating a robust form engine with a dynamic Notion-style collaborative workspace for tasks and quizzes.\n"
        "• Authored comprehensive architectural specifications: Level 0/1 DFDs, UML Sequence & Class models, and full vector UI mockups."
    )
    p_p1_desc.runs[0].font.size = Pt(8.8)

    # Project 2: Demo PMS / AdisFee
    p_p2 = doc.add_paragraph()
    p_p2.paragraph_format.space_before = Pt(2)
    p_p2.paragraph_format.space_after = Pt(1)
    run_p2_title = p_p2.add_run("Demo PMS & AdisFee Cloud Platform (Live Serverless WebApp)  |  ")
    run_p2_title.font.bold = True
    add_hyperlink(p_p2, "https://demopms.blogspot.com", "Live Demo (demopms)", bold=True)
    p_p2.add_run("  •  ")
    add_hyperlink(p_p2, "https://adisfee.blospot.com", "Production (adisfee)")

    p_p2_desc = doc.add_paragraph()
    p_p2_desc.paragraph_format.space_before = Pt(0)
    p_p2_desc.paragraph_format.space_after = Pt(6)
    p_p2_desc.paragraph_format.line_spacing = 1.15
    p_p2_desc.add_run(
        "• Architected an enterprise-grade school accounting and fee platform powered by Google Apps Script serverless backends with zero recurring cloud cost.\n"
        "• Engineered instant real-time state synchronization across independent browser tabs without WebSockets or dedicated servers.\n"
        "• Integrated cryptographic OTP-based authentication and role-based permissions."
    )
    p_p2_desc.runs[0].font.size = Pt(8.8)

    # Project 3: Json-Boundary
    p_p3 = doc.add_paragraph()
    p_p3.paragraph_format.space_before = Pt(2)
    p_p3.paragraph_format.space_after = Pt(1)
    run_p3_title = p_p3.add_run("Json-Boundary — Published NPM Package  |  ")
    run_p3_title.font.bold = True
    add_hyperlink(p_p3, "https://www.npmjs.com/package/json-boundary", "npmjs.com/package/json-boundary", bold=True)
    p_p3.add_run("  •  ")
    add_hyperlink(p_p3, "https://github.com/favouritesir/Json-Boundary", "GitHub Source")

    p_p3_desc = doc.add_paragraph()
    p_p3_desc.paragraph_format.space_before = Pt(0)
    p_p3_desc.paragraph_format.space_after = Pt(6)
    p_p3_desc.paragraph_format.line_spacing = 1.15
    p_p3_desc.add_run(
        "• Created an ultra-fast zero-dependency TypeScript library for scanning boundary indexes in JSON payloads, conceived to automate dynamic Prisma ORM where clause generation."
    )
    p_p3_desc.runs[0].font.size = Pt(8.8)

    # Project 4: My-mini-DNS & mTask
    p_p4 = doc.add_paragraph()
    p_p4.paragraph_format.space_before = Pt(2)
    p_p4.paragraph_format.space_after = Pt(1)
    run_p4_title = p_p4.add_run("My-mini-DNS (ESP IoT)  &  mTask (Interactive Bash TUI)  |  ")
    run_p4_title.font.bold = True
    add_hyperlink(p_p4, "https://github.com/favouritesir/My-mini-DNS", "DNS Repo")
    p_p4.add_run("  •  ")
    add_hyperlink(p_p4, "https://github.com/favouritesir/mTask", "mTask Repo")

    p_p4_desc = doc.add_paragraph()
    p_p4_desc.paragraph_format.space_before = Pt(0)
    p_p4_desc.paragraph_format.space_after = Pt(8)
    p_p4_desc.paragraph_format.line_spacing = 1.15
    p_p4_desc.add_run(
        "• My-mini-DNS: Custom C++ DNS firmware on ESP8266/ESP32 intercepting local network domains while passing upstream internet queries.\n"
        "• mTask: Terminal-based task dashboard in pure POSIX Bash with ANSI escape navigation and process control (OS coursework).\n"
        "• Don Entry & Automation: Automated cloud donation ledger on Google Apps Script with public video documentation."
    )
    p_p4_desc.runs[0].font.size = Pt(8.8)

    # ==========================================
    # 3. PROFESSIONAL EXPERIENCE & LEADERSHIP
    # ==========================================
    add_section_header("Professional Experience & Leadership")

    # Experience 1
    p_e1 = doc.add_paragraph()
    p_e1.paragraph_format.space_before = Pt(2)
    p_e1.paragraph_format.space_after = Pt(1)
    p_e1.add_run("Technical Advisor & Academic Systems Lead (7+ Years)  |  Alor Dishary Ideal School  |  2017 — Present").font.bold = True

    p_e1_desc = doc.add_paragraph()
    p_e1_desc.paragraph_format.space_before = Pt(0)
    p_e1_desc.paragraph_format.space_after = Pt(6)
    p_e1_desc.paragraph_format.line_spacing = 1.15
    p_e1_desc.add_run(
        "• Architected computerized grading systems, digital student records, and automated administrative fee collection pipelines.\n"
        "• Designed specialized academic curricula, interactive question sheets, and STEM learning materials.\n"
        "• Taught advanced Computer Science, Physics, Chemistry, and Mathematics, mentoring hundreds of students through secondary academic cycles."
    )
    p_e1_desc.runs[0].font.size = Pt(8.8)

    # Experience 2
    p_e2 = doc.add_paragraph()
    p_e2.paragraph_format.space_before = Pt(2)
    p_e2.paragraph_format.space_after = Pt(1)
    p_e2.add_run("Founder & Platform Architect  |  BD Smart Book (").font.bold = True
    add_hyperlink(p_e2, "https://bdsmartbook.com", "bdsmartbook.com", bold=True)
    p_e2.add_run(")  |  2021 — Present").font.bold = True

    p_e2_desc = doc.add_paragraph()
    p_e2_desc.paragraph_format.space_before = Pt(0)
    p_e2_desc.paragraph_format.space_after = Pt(6)
    p_e2_desc.paragraph_format.line_spacing = 1.15
    p_e2_desc.add_run(
        "• Founded an online educational publication platform providing digitized smart learning materials.\n"
        "• Engineered interactive smart books automated via Google Apps Script cloud pipelines (Demo: docs.google.com smart book export)."
    )
    p_e2_desc.runs[0].font.size = Pt(8.8)

    # Experience 3
    p_e3 = doc.add_paragraph()
    p_e3.paragraph_format.space_before = Pt(2)
    p_e3.paragraph_format.space_after = Pt(1)
    p_e3.add_run("Commercial Software Development Trainee  |  Itransition Group  |  Certified Nov 2024").font.bold = True

    p_e3_desc = doc.add_paragraph()
    p_e3_desc.paragraph_format.space_before = Pt(0)
    p_e3_desc.paragraph_format.space_after = Pt(8)
    p_e3_desc.paragraph_format.line_spacing = 1.15
    p_e3_desc.add_run(
        "• Completed intensive corporate training in commercial JavaScript/TypeScript development, mastering enterprise coding practices, code reviews, and production software patterns."
    )
    p_e3_desc.runs[0].font.size = Pt(8.8)

    # ==========================================
    # 4. TECHNICAL SKILLS MATRIX
    # ==========================================
    add_section_header("Technical Skills Matrix")

    skills_table = doc.add_table(rows=4, cols=2)
    skills_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    skills_table.autofit = False

    skills_data = [
        ("Algorithms & Core Systems:", "C, C++, In-Situ Algorithms, Asymmetric Memory Models, Pointer Discipline, ATmega328P Microcontroller"),
        ("Languages & Runtimes:", "JavaScript (ES6+), TypeScript, Node.js, Python, Java, Bash / Linux Shell, C# / .NET"),
        ("Web & Frameworks:", "React.js, Vue.js, Electron.js, Three.js / WebGL, HTML5, CSS3, Responsive UI/UX"),
        ("Cloud, Serverless & Data:", "Google Apps Script, Real-Time Sync, MySQL, Prisma ORM, ESP8266/ESP32, Git & GitHub")
    ]

    for i, (cat, val) in enumerate(skills_data):
        row = skills_table.rows[i]
        c0, c1 = row.cells
        c0.width = Inches(2.2)
        c1.width = Inches(5.0)

        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(1)
        p0.paragraph_format.space_after = Pt(1)
        r0 = p0.add_run(cat)
        r0.font.bold = True
        r0.font.size = Pt(8.8)
        r0.font.color.rgb = COLOR_PRIMARY

        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(1)
        p1.paragraph_format.space_after = Pt(1)
        r1 = p1.add_run(val)
        r1.font.size = Pt(8.8)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(4)
    p_spacer.paragraph_format.space_after = Pt(4)

    # ==========================================
    # 5. EDUCATION
    # ==========================================
    add_section_header("Education")

    edu_table = doc.add_table(rows=4, cols=4)
    edu_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    edu_table.autofit = False

    col_widths = [Inches(2.2), Inches(2.5), Inches(1.5), Inches(1.0)]

    headers = ["Degree / Certificate", "Institution", "Group / Department", "Year / Result"]
    hdr_row = edu_table.rows[0]
    for j, h_text in enumerate(headers):
        cell = hdr_row.cells[j]
        cell.width = col_widths[j]
        set_cell_background(cell, COLOR_LIGHT_BG_HEX)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(h_text)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = COLOR_PRIMARY

    edu_rows = [
        ("B.Sc in CSE (Completed)", "Green University of Bangladesh", "Computer Science & Engineering", "4-Year (8 Sem)"),
        ("H.S.C (Higher Secondary)", "Gazipur City College", "Science", "2018 (GPA 3.33)"),
        ("S.S.C (Secondary School)", "Gazipur City Model School", "Science", "2016 (GPA 4.78)")
    ]

    for i, (deg, inst, grp, yr) in enumerate(edu_rows):
        row = edu_table.rows[i + 1]
        for j, val in enumerate([deg, inst, grp, yr]):
            cell = row.cells[j]
            cell.width = col_widths[j]
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if j == 0:
                r.font.bold = True

    # Save to Downloads & Portfolio
    doc.save(str(OUT_DOCX_DOWNLOADS))
    doc.save(str(OUT_DOCX_PORTFOLIO))

    print(f"SUCCESS: Created DOCX CV ({OUT_DOCX_DOWNLOADS.stat().st_size} bytes) at {OUT_DOCX_DOWNLOADS}")

if __name__ == "__main__":
    build_cv()
