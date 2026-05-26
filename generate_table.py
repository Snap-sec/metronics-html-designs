import re

rows = [
    {
        "assessment": "Business Logic Security Testing – Q4 (6KPA)",
        "time": "22 weeks ago",
        "state": "Remediation",
        "state_color": "green",
        "vulns": [("orange", 9), ("blue", 6)],
        "progress": 80
    },
    {
        "assessment": "Data Leakage & Exposure Assessment – Q4 (6KPA)",
        "time": "22 weeks ago",
        "state": "New",
        "state_color": "blue",
        "vulns": [("orange", 9), ("blue", 1)],
        "progress": 60
    },
    {
        "assessment": "Third-Party / Vendor Risk Assessment – Q4 (6KPA)",
        "time": "23 weeks ago",
        "state": "New",
        "state_color": "blue",
        "vulns": [("red", 2), ("orange", 10), ("blue", 5)],
        "progress": 53
    },
    {
        "assessment": "Continuous Attack Surface Monitoring (ASM) (6KPA)",
        "time": "23 weeks ago",
        "state": "Testing Ongoing",
        "state_color": "yellow",
        "vulns": [("red", 3), ("orange", 9), ("blue", 13)],
        "progress": 76
    },
    {
        "assessment": "Incident Response Tabletop Exercise – Q3 (6KPA)",
        "time": "24 weeks ago",
        "state": "Remediation",
        "state_color": "green",
        "vulns": [("red", 3), ("orange", 8), ("blue", 7)],
        "progress": 50
    },
    {
        "assessment": "Phishing Simulation & Awareness Campaign – Q3 (6KPA)",
        "time": "24 weeks ago",
        "state": "Remediation",
        "state_color": "green",
        "vulns": [("red", 3), ("orange", 8), ("blue", 5)],
        "progress": 75
    },
    {
        "assessment": "Purple Team Exercise (6KPA)",
        "time": "24 weeks ago",
        "state": "Testing Ongoing",
        "state_color": "yellow",
        "vulns": [("red", 3), ("orange", 10), ("blue", 10)],
        "progress": 70
    },
    {
        "assessment": "Blue Team Readiness Assessment – Q3 (6KPA)",
        "time": "25 weeks ago",
        "state": "Testing Ongoing",
        "state_color": "yellow",
        "vulns": [("red", 1), ("orange", 7), ("blue", 10)],
        "progress": 61
    },
    {
        "assessment": "Red Team Exercise (6KPA)",
        "time": "25 weeks ago",
        "state": "Remediation",
        "state_color": "green",
        "vulns": [("red", 1), ("orange", 10), ("blue", 7)],
        "progress": 72
    },
    {
        "assessment": "CI/CD Pipeline Security Assessment – Q2 (6KPA)",
        "time": "26 weeks ago",
        "state": "Remediation",
        "state_color": "green",
        "vulns": [("red", 2), ("orange", 5), ("blue", 7)],
        "progress": 57
    },
    {
        "assessment": "Privileged Access Review – Q2 (6KPA)",
        "time": "26 weeks ago",
        "state": "Remediation",
        "state_color": "green",
        "vulns": [("red", 2), ("orange", 4), ("blue", 10)],
        "progress": 63
    }
]

def get_state_classes(color):
    if color == "green":
        return "bg-green-100 text-green-600"
    elif color == "blue":
        return "bg-blue-100 text-blue-600"
    elif color == "yellow":
        return "bg-yellow-100 text-yellow-600"
    return ""

def get_dot_color(color):
    if color == "red":
        return "bg-red-500"
    if color == "orange":
        return "bg-orange-500"
    if color == "blue":
        return "bg-blue-500"
    return "bg-gray-500"

table_html = """
<table class="kt-table table-fixed kt-table-border" data-kt-datatable-table="true">
   <thead>
      <tr>
         <th class="w-[450px]">
            <span class="kt-table-col">
               <span class="kt-table-col-label">Assessment</span>
               <span class="kt-table-col-sort"></span>
            </span>
         </th>
         <th class="w-[200px]">
            <span class="kt-table-col">
               <span class="kt-table-col-label">State</span>
               <span class="kt-table-col-sort"></span>
            </span>
         </th>
         <th class="w-[300px]">
            <span class="kt-table-col">
               <span class="kt-table-col-label">Vulnerabilities</span>
               <span class="kt-table-col-sort"></span>
            </span>
         </th>
         <th class="w-[200px]">
            <span class="kt-table-col">
               <span class="kt-table-col-label">Remediation Progress</span>
               <span class="kt-table-col-sort"></span>
            </span>
         </th>
      </tr>
   </thead>
   <tbody>
"""

for row in rows:
    vuln_html = ""
    for v in row["vulns"]:
        vuln_html += f'<span class="flex items-center gap-1.5"><span class="size-1.5 rounded-full {get_dot_color(v[0])}"></span><span class="text-xs font-medium text-gray-700">{v[1]}</span></span>'
    
    # Let's wrap the vulns in a pill container like the screenshot (light gray border, rounded)
    # The screenshot shows them together in one pill or separate pills?
    # It looks like they are separate or maybe in one container with a white background and subtle border.
    # Actually, in the screenshot, all vulns for a row are inside one single pill-like box with a very subtle background/border.
    # We will use `<div class="inline-flex items-center gap-3 px-2.5 py-1 rounded border border-gray-200 bg-gray-50/50">`
    vuln_container = f'<div class="inline-flex items-center gap-3 px-2.5 py-1 rounded border border-gray-200 bg-gray-50/50">{vuln_html}</div>'

    progress_bar = f"""
    <div class="flex flex-col gap-1 w-full max-w-[120px]">
        <div class="flex justify-between items-center text-2xs font-medium text-gray-500">
            <span>{row["progress"]}% resolved</span>
        </div>
        <div class="w-full bg-gray-100 rounded-full h-1.5">
            <div class="bg-blue-600 h-1.5 rounded-full" style="width: {row["progress"]}%"></div>
        </div>
    </div>
    """

    state_badge = f'<span class="inline-flex items-center px-2.5 py-1 rounded text-xs font-medium {get_state_classes(row["state_color"])}">{row["state"]}</span>'

    table_html += f"""
      <tr>
         <td>
            <div class="flex flex-col gap-1.5">
               <a class="leading-none font-medium text-sm text-foreground hover:text-primary" href="#">{row["assessment"]}</a>
               <span class="text-sm text-secondary-foreground font-normal">{row["time"]}</span>
            </div>
         </td>
         <td>
            {state_badge}
         </td>
         <td>
            {vuln_container}
         </td>
         <td>
            {progress_bar}
         </td>
      </tr>
"""

table_html += """
   </tbody>
</table>
"""

with open('/home/imran/Desktop/devCurrent/Metronics-html/assessments.html', 'r') as f:
    content = f.read()

start = content.find('<table class="kt-table table-fixed kt-table-border"')
end = content.find('</table>', start) + len('</table>')

new_content = content[:start] + table_html + content[end:]

with open('/home/imran/Desktop/devCurrent/Metronics-html/assessments.html', 'w') as f:
    f.write(new_content)

print("Replacement complete.")
