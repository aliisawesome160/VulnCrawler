⸻

VulnCrawler – Website Crawler & Tech Auditor

VulnCrawler is a Python-based website crawler and analyzer that scans any site you specify, maps its internal links, detects technologies (like JavaScript libraries and frameworks), and checks if they’re outdated or potentially vulnerable.

This tool is for educational and auditing purposes only — designed for developers, researchers, and site owners who want to analyze their sites and improve security hygiene.

⸻

Features
	•	Crawls a website up to 2 levels deep and collects all internal links.
	•	Detects technologies used by the site (via Wappalyzer).
	•	Identifies JavaScript libraries and versions from script tags.
	•	Compares versions against a list of known outdated/vulnerable releases.
	•	Provides a summary report of findings in the terminal.

⸻

Installation
	1.	Clone the repo:

git clone https://github.com/<your-username>/SiteSleuth.git
cd SiteSleuth


	2.	Install dependencies:

pip install -r requirements.txt


	3.	(Optional) Set up a virtual environment for isolation:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate



⸻

Usage

Run the tool directly from your terminal:

python site_checker.py

Enter a website URL when prompted (must include http:// or https://):

Enter the website URL (with http/https): https://example.com

The script will:
	1.	Crawl the target site.
	2.	Collect internal links (up to 2 levels deep).
	3.	Detect what technologies and JS libraries the site is running.
	4.	Check for outdated JavaScript versions (based on a static vulnerability list).
	5.	Print results in your terminal.

Example Output:

[*] Crawling site: https://example.com
[*] Found 42 internal links.
[*] Detecting technologies...
Technologies: ['Nginx', 'Bootstrap', 'jQuery']

[*] Checking JS library versions...
jquery - version 1.8 on https://example.com/js/vendor/jquery.min.js => ⚠ OUTDATED
bootstrap - version 5.3 on https://example.com/js/bootstrap.min.js => OK

[+] Scan complete.


⸻

Disclaimer

This tool is intended only for legal, authorized security assessments and educational use.
Do not use this tool to scan or audit websites without the owner’s explicit permission.
The developer is not responsible for any misuse.

⸻
