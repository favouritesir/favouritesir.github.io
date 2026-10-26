import subprocess
from pathlib import Path

BASE_DIR = Path(r"D:\Drive\gub221902131\My Drive\my\Code\GITHUB\favouritesir.github.io")
EDGE_BIN = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PHOTO_PATH = (BASE_DIR / "assets" / "img" / "ashikur_rahman.png").as_uri()

CV_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CV of Ashikur Rahman</title>
  <style>
    @page {{
      size: A4;
      margin: 0;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      background: #ffffff;
      font-size: 9pt;
      line-height: 1.38;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    .page {{
      width: 210mm;
      height: 297mm;
      position: relative;
      page-break-after: always;
      display: grid;
      grid-template-columns: 69mm 141mm;
      overflow: hidden;
      background: #ffffff;
    }}
    .page:last-child {{
      page-break-after: avoid;
    }}

    /* Sidebar */
    .sidebar {{
      background: #0f766e;
      color: #f0fdfa;
      padding: 16mm 7mm 14mm 8mm;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .avatar-wrap {{
      text-align: center;
      margin-bottom: 4px;
    }}
    .avatar {{
      width: 38mm;
      height: 38mm;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid #5eead4;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }}
    .sidebar-section {{
      margin-bottom: 6px;
    }}
    .sidebar-title {{
      font-size: 9.5pt;
      text-transform: uppercase;
      font-weight: 800;
      letter-spacing: 0.8px;
      color: #99f6e4;
      border-bottom: 1.5px solid rgba(153, 246, 228, 0.4);
      padding-bottom: 3px;
      margin-bottom: 7px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}
    .side-item {{
      margin-bottom: 6px;
      font-size: 8.2pt;
    }}
    .side-item strong {{
      color: #ffffff;
      display: block;
      font-size: 8.5pt;
    }}
    .side-item span {{
      color: #ccfbf1;
    }}
    .contact-list {{
      list-style: none;
      font-size: 8.2pt;
    }}
    .contact-list li {{
      margin-bottom: 6px;
      word-break: break-all;
      display: flex;
      align-items: flex-start;
      gap: 6px;
    }}
    .contact-list a {{
      color: #ffffff;
      text-decoration: none;
      font-weight: 600;
    }}
    .contact-icon {{
      color: #5eead4;
      font-weight: bold;
      min-width: 13px;
    }}
    .skill-category-title {{
      font-size: 8.4pt;
      font-weight: 700;
      color: #ffffff;
      margin-top: 5px;
      margin-bottom: 3px;
    }}
    .skill-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
      margin-bottom: 6px;
    }}
    .skill-pill {{
      background: rgba(255, 255, 255, 0.15);
      color: #f0fdfa;
      padding: 2px 6px;
      border-radius: 3px;
      font-size: 7.6pt;
      font-weight: 500;
    }}

    /* Main Content */
    .main {{
      padding: 14mm 10mm 12mm 10mm;
      display: flex;
      flex-direction: column;
    }}
    .header {{
      border-bottom: 2px solid #0f766e;
      padding-bottom: 8px;
      margin-bottom: 10px;
    }}
    .header h1 {{
      font-size: 22pt;
      font-weight: 900;
      color: #0f172a;
      letter-spacing: -0.5px;
      line-height: 1.1;
    }}
    .header h1 span {{
      color: #0f766e;
    }}
    .header .subtitle {{
      font-size: 10pt;
      font-weight: 700;
      color: #0d9488;
      margin-top: 3px;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }}
    .header .summary {{
      font-size: 8.5pt;
      color: #475569;
      margin-top: 6px;
      line-height: 1.35;
      text-align: justify;
    }}

    .section-block {{
      margin-bottom: 11px;
    }}
    .section-title {{
      font-size: 10.5pt;
      font-weight: 800;
      color: #0f766e;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      border-bottom: 1.5px solid #cbd5e1;
      padding-bottom: 2px;
      margin-bottom: 7px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .section-title::before {{
      content: '';
      display: inline-block;
      width: 7px;
      height: 7px;
      background: #0f766e;
      border-radius: 1px;
    }}

    /* Items */
    .item {{
      margin-bottom: 7px;
    }}
    .item-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 1px;
    }}
    .item-title {{
      font-size: 9.2pt;
      font-weight: 800;
      color: #0f172a;
    }}
    .item-doi {{
      font-size: 7.8pt;
      font-family: monospace;
      background: #f1f5f9;
      color: #0f766e;
      padding: 1px 5px;
      border-radius: 3px;
      border: 1px solid #cbd5e1;
      text-decoration: none;
      font-weight: bold;
    }}
    .item-meta {{
      font-size: 8.2pt;
      color: #0d9488;
      font-weight: 600;
      margin-bottom: 2px;
    }}
    .item-desc {{
      font-size: 8.2pt;
      color: #334155;
      line-height: 1.32;
      text-align: justify;
    }}
    .item-bullets {{
      list-style-type: disc;
      margin-left: 14px;
      font-size: 8.2pt;
      color: #334155;
      margin-top: 2px;
    }}
    .item-bullets li {{
      margin-bottom: 2px;
      line-height: 1.3;
    }}

    /* Education Table */
    .edu-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 8.2pt;
      margin-top: 3px;
    }}
    .edu-table th, .edu-table td {{
      padding: 4px 6px;
      text-align: left;
      border-bottom: 1px solid #e2e8f0;
    }}
    .edu-table th {{
      background: #f8fafc;
      font-weight: 700;
      color: #0f766e;
    }}
    .edu-table td strong {{
      color: #0f172a;
    }}

    /* Footer stamp */
    .page-footer {{
      margin-top: auto;
      font-size: 7.5pt;
      color: #94a3b8;
      text-align: center;
      border-top: 1px solid #e2e8f0;
      padding-top: 4px;
    }}
  </style>
</head>
<body>

  <!-- ==================== PAGE 1 ==================== -->
  <div class="page">
    <!-- Sidebar Page 1 -->
    <div class="sidebar">
      <div class="avatar-wrap">
        <img src="{PHOTO_PATH}" alt="Ashikur Rahman" class="avatar">
      </div>

      <div class="sidebar-section">
        <div class="sidebar-title">Contact &amp; Profiles</div>
        <ul class="contact-list">
          <li><span class="contact-icon">&#9679;</span> <span><strong>Email:</strong> <a href="mailto:ashikur.gub@gmail.com">ashikur.gub@gmail.com</a></span></li>
          <li><span class="contact-icon">&#9679;</span> <span><strong>Phone:</strong> +880 1962-579305</span></li>
          <li><span class="contact-icon">&#9679;</span> <span><strong>Portfolio:</strong> <a href="http://favouritesir.me">favouritesir.me</a></span></li>
          <li><span class="contact-icon">&#9679;</span> <span><strong>GitHub:</strong> <a href="https://github.com/favouritesir">github.com/favouritesir</a></span></li>
          <li><span class="contact-icon">&#9679;</span> <span><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/favouritesir">linkedin.com/in/favouritesir</a></span></li>
          <li><span class="contact-icon">&#9679;</span> <span><strong>Location:</strong> Gazipur / Dhaka, Bangladesh</span></li>
        </ul>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-title">Core Technical Skills</div>
        
        <div class="skill-category-title">Algorithms &amp; Low-Level</div>
        <div class="skill-pills">
          <span class="skill-pill">C / C++</span>
          <span class="skill-pill">Pointer In-Situ</span>
          <span class="skill-pill">Asymmetric Space</span>
          <span class="skill-pill">ATmega328P</span>
        </div>

        <div class="skill-category-title">Languages &amp; Runtimes</div>
        <div class="skill-pills">
          <span class="skill-pill">JavaScript (ES6+)</span>
          <span class="skill-pill">TypeScript</span>
          <span class="skill-pill">Node.js</span>
          <span class="skill-pill">Python</span>
          <span class="skill-pill">Java</span>
          <span class="skill-pill">Bash / Shell</span>
        </div>

        <div class="skill-category-title">Web &amp; Frameworks</div>
        <div class="skill-pills">
          <span class="skill-pill">React.js</span>
          <span class="skill-pill">Vue.js</span>
          <span class="skill-pill">Electron.js</span>
          <span class="skill-pill">Three.js</span>
          <span class="skill-pill">HTML5 / CSS3</span>
        </div>

        <div class="skill-category-title">Cloud, Serverless &amp; Data</div>
        <div class="skill-pills">
          <span class="skill-pill">Google Apps Script</span>
          <span class="skill-pill">Real-Time Sync</span>
          <span class="skill-pill">MySQL</span>
          <span class="skill-pill">Prisma ORM</span>
          <span class="skill-pill">Git / GitHub</span>
        </div>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-title">Languages</div>
        <div class="side-item"><strong>Bengali:</strong> <span>Native Proficiency</span></div>
        <div class="side-item"><strong>English:</strong> <span>Full Professional Working</span></div>
      </div>
    </div>

    <!-- Main Content Page 1 -->
    <div class="main">
      <div class="header">
        <h1>ASHIKUR <span>RAHMAN</span></h1>
        <div class="subtitle">Software Engineer &bull; Algorithm Researcher &bull; Systems Architect</div>
        <p class="summary">
          Computer Science &amp; Engineering graduate from Green University of Bangladesh. Conceived, proved, and published novel algorithmic paradigms indexed with permanent CERN/Zenodo DOIs. Architect of zero-cost, high-concurrency real-time cloud management platforms, developer NPM utilities, and embedded IoT networking firmware. Proven track record in academic mentorship, systems operations, and production software delivery.
        </p>
      </div>

      <!-- Published Research Section -->
      <div class="section-block">
        <div class="section-title">Published Research Preprints (CERN / Zenodo DOIs)</div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">Cloud Sort: An Overhead Caller-Buffer Merge Paradigm</span>
            <a href="https://doi.org/10.5281/zenodo.23665548" class="item-doi">DOI: 10.5281/zenodo.23665548</a>
          </div>
          <div class="item-meta">Conceived at Dept. of CSE, Green University of Bangladesh &bull; Published Oct 2026</div>
          <p class="item-desc">
            Invented an asymmetric in-situ merge sort reducing auxiliary space to &lceil;N/2&rceil; elements with zero dynamic heap allocations (<code>malloc</code>/<code>free</code>). Proved inductive read-before-write safety (<i>wp<sub>t</sub> &le; rp<sub>t</sub></i>) and formulated the <strong>Zero-Move Right Tail Property</strong>, eliminating 25.0% of physical SRAM data bus writes. Audited against QuickSort, Standard Merge, and TimSort: achieves 10%–67% faster throughput than textbook merge with 0% extra key comparisons. Verified across 10,000 differential random array trials and micro-benchmarked on ATmega328P.
          </p>
        </div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">In-Situ Dual-Pointer Algorithm for Infix-to-Prefix Transformation</span>
            <a href="https://doi.org/10.5281/zenodo.23657544" class="item-doi">DOI: 10.5281/zenodo.23657544</a>
          </div>
          <div class="item-meta">Conceived at Dept. of CSE, Green University of Bangladesh &bull; Published Oct 2026</div>
          <p class="item-desc">
            Formulated an optimal right-to-left single-pass conversion algorithm achieving $O(1)$ auxiliary string space. Eliminates conventional textbook triple-pass string reversal overhead, reducing memory bus operations by over 60% with full mathematical proofs.
          </p>
        </div>
      </div>

      <!-- Selected Production & Engineering Projects -->
      <div class="section-block">
        <div class="section-title">Featured Production &amp; Systems Projects</div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">Demo PMS &amp; AdisFee Cloud Platform (Live Serverless WebApp)</span>
            <span class="item-meta">demopms.blogspot.com | adisfee.blospot.com</span>
          </div>
          <ul class="item-bullets">
            <li>Architected a high-concurrency student accounting and fee collection platform powered by Google Apps Script serverless backends with zero recurring cloud hosting costs.</li>
            <li>Engineered instant real-time state synchronization across independent browser tabs without WebSockets or persistent socket servers.</li>
            <li>Integrated cryptographic OTP-based authentication and role-based operational permissions.</li>
          </ul>
        </div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">SUPER Fill — Form Engine &amp; Dynamic Workspace (IDP 1 Lab Project)</span>
            <span class="item-meta">Course: CSE 324, Green University of Bangladesh</span>
          </div>
          <ul class="item-bullets">
            <li>Designed a cloud-native platform integrating a robust form engine with a dynamic Notion-style collaborative workspace for interactive quizzes, automated grading, and tasks.</li>
            <li>Authored complete architectural specifications: DFD Level 0/1, UML sequence &amp; class diagrams, high-fidelity UI vector mockups, and comprehensive engineering reports.</li>
          </ul>
        </div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">Json-Boundary — NPM Package (TypeScript / Node.js)</span>
            <a href="https://www.npmjs.com/package/json-boundary" class="item-doi">npmjs.com/package/json-boundary</a>
          </div>
          <ul class="item-bullets">
            <li>Created an ultra-fast zero-dependency TypeScript library for scanning boundary indexes in JSON payloads, conceived to automate dynamic Prisma ORM <code>where</code> clause generation.</li>
          </ul>
        </div>
      </div>

      <div class="page-footer">Page 1 of 2 &bull; Ashikur Rahman &bull; Verified Online Portfolio: favouritesir.me</div>
    </div>
  </div>

  <!-- ==================== PAGE 2 ==================== -->
  <div class="page">
    <!-- Sidebar Page 2 -->
    <div class="sidebar">
      <div class="sidebar-section">
        <div class="sidebar-title">Certifications &amp; Honors</div>
        <div class="side-item">
          <strong>Itransition Group (Nov 2024)</strong>
          <span>Commercial Software Development — JavaScript (Corporate Remote Training)</span>
        </div>
        <div class="side-item">
          <strong>CERN / Zenodo Verified Author</strong>
          <span>2x Published DOIs for Original Data Structures &amp; Algorithms Research</span>
        </div>
        <div class="side-item">
          <strong>Founder &bull; BD Smart Book</strong>
          <span>Online Publication &amp; Automated Learning System</span>
        </div>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-title">Embedded &amp; Systems</div>
        <div class="skill-pills">
          <span class="skill-pill">ESP8266 / ESP32</span>
          <span class="skill-pill">DNS Protocols</span>
          <span class="skill-pill">Linux POSIX</span>
          <span class="skill-pill">Terminal ANSI TUI</span>
          <span class="skill-pill">Process Control</span>
        </div>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-title">Engineering Philosophy</div>
        <p style="font-size: 8pt; color: #ccfbf1; line-height: 1.35; font-style: italic;">
          "True software excellence balances theoretical rigor with physical execution — eliminating memory waste, zeroing unnecessary allocations, and building resilient zero-cost systems."
        </p>
      </div>

      <div class="sidebar-section" style="margin-top: auto;">
        <div class="sidebar-title">Online Repository</div>
        <p style="font-size: 8pt; color: #ccfbf1;">
          Full source codes, benchmarks, test vectors, and multi-language ports available on GitHub:
          <br><strong>github.com/favouritesir</strong>
        </p>
      </div>
    </div>

    <!-- Main Content Page 2 -->
    <div class="main">
      <!-- Systems Projects Continued -->
      <div class="section-block">
        <div class="section-title">Systems, IoT &amp; Automation Projects (Continued)</div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">My-mini-DNS — Custom ESP Microcontroller DNS Router</span>
            <a href="https://github.com/favouritesir/My-mini-DNS" class="item-doi">github.com/favouritesir/My-mini-DNS</a>
          </div>
          <ul class="item-bullets">
            <li>Engineered custom local DNS firmware in C++ for ESP8266/ESP32 microcontrollers.</li>
            <li>Enables dual-routing capability: intercepts and resolves private local domain names to local micro-services while transparently passing upstream internet queries to public DNS servers.</li>
          </ul>
        </div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">mTask — Interactive Terminal Task Manager (Bash / Linux)</span>
            <a href="https://github.com/favouritesir/mTask" class="item-doi">github.com/favouritesir/mTask</a>
          </div>
          <ul class="item-bullets">
            <li>Developed a terminal-based responsive task dashboard in pure POSIX Bash for Linux OS coursework.</li>
            <li>Implemented keyboard-driven navigation, ANSI escape graphics, task prioritization, and background process tracking with zero external dependencies.</li>
          </ul>
        </div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">Electron.js Task Manager &bull; Don Entry Automation</span>
            <span class="item-meta">Cross-Platform Desktop &amp; Cloud Ledger</span>
          </div>
          <ul class="item-bullets">
            <li><strong>Electron Task Manager:</strong> Built cross-platform desktop task suite with persistent local storage.</li>
            <li><strong>Don Entry:</strong> Automated financial donation and ledger entry pipelines on Google Apps Script with public multi-part video documentation (<a href="https://www.youtube.com/playlist?list=PLBUpi-NMujyW_qNiCAyxOMEKQS9MPiRU2" style="color:#0f766e;">YouTube Playlist</a>).</li>
          </ul>
        </div>
      </div>

      <!-- Professional Experience & Leadership -->
      <div class="section-block">
        <div class="section-title">Professional Experience &amp; Leadership</div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">Technical Advisor &amp; Academic Systems Lead (7+ Years)</span>
            <span class="item-meta">2017 — Present</span>
          </div>
          <div class="item-meta">Alor Dishary Ideal School &bull; Gazipur, Bangladesh</div>
          <ul class="item-bullets">
            <li>Architected and managed computerized institutional grading systems, digital student records, and automated administrative fee collection systems.</li>
            <li>Designed specialized academic curricula, interactive question sheets, and STEM learning materials.</li>
            <li>Taught advanced Computer Science, Physics, Chemistry, and General Mathematics, mentoring hundreds of students through secondary academic cycles.</li>
          </ul>
        </div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">Founder &amp; Platform Architect</span>
            <span class="item-meta">2021 — Present</span>
          </div>
          <div class="item-meta">BD Smart Book (bdsmartbook.com)</div>
          <ul class="item-bullets">
            <li>Founded an online educational publishing platform providing digitized smart learning materials.</li>
            <li>Engineered interactive smart books automated via Google Apps Script and modern responsive web interfaces.</li>
          </ul>
        </div>

        <div class="item">
          <div class="item-header">
            <span class="item-title">Commercial Software Development Trainee</span>
            <span class="item-meta">Nov 2024</span>
          </div>
          <div class="item-meta">Itransition Group (Remote Corporate Training)</div>
          <ul class="item-bullets">
            <li>Completed intensive corporate training in commercial JavaScript/TypeScript development, mastering enterprise-level coding practices, code reviews, and production software patterns.</li>
          </ul>
        </div>
      </div>

      <!-- Education Section -->
      <div class="section-block">
        <div class="section-title">Education</div>
        <table class="edu-table">
          <thead>
            <tr>
              <th>Degree / Certificate</th>
              <th>Institution</th>
              <th>Group / Department</th>
              <th>Year / Result</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>B.Sc in CSE (Completed)</strong></td>
              <td>Green University of Bangladesh</td>
              <td>Computer Science &amp; Engineering</td>
              <td>4-Year (8 Semesters)</td>
            </tr>
            <tr>
              <td><strong>H.S.C (Higher Secondary)</strong></td>
              <td>Gazipur City College</td>
              <td>Science</td>
              <td>2018 &bull; GPA: 3.33 (Dhaka)</td>
            </tr>
            <tr>
              <td><strong>S.S.C (Secondary School)</strong></td>
              <td>Gazipur City Model School</td>
              <td>Science</td>
              <td>2016 &bull; GPA: 4.78 (Dhaka)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="page-footer">Page 2 of 2 &bull; Ashikur Rahman &bull; Verified Online Portfolio: favouritesir.me</div>
    </div>
  </div>

</body>
</html>
"""

def generate():
    temp_html = BASE_DIR / "temp_cv.html"
    out_pdf_portfolio = BASE_DIR / "assets" / "cv" / "CV of Ashikur Rahman.pdf"
    out_pdf_downloads = Path(r"D:\Downloads\CV of Ashikur Rahman.pdf")

    temp_html.write_text(CV_HTML, encoding="utf-8")

    cmd = [
        EDGE_BIN,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf_portfolio}",
        temp_html.as_uri()
    ]
    subprocess.run(cmd, check=True)

    # Copy to downloads
    out_pdf_downloads.write_bytes(out_pdf_portfolio.read_bytes())

    if temp_html.exists():
        temp_html.unlink()

    print(f"SUCCESS: Generated CV ({out_pdf_portfolio.stat().st_size} bytes)")

if __name__ == "__main__":
    generate()
