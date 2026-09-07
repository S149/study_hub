import sys, json, re, os

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "") or data.get("tool_response", {}).get("filePath", "")
if not path.endswith("index.html"):
    sys.exit(0)

try:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
except OSError:
    sys.exit(0)

void_tags = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}

skip_ranges = [m.span() for m in re.finditer(
    r"<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>|<!--.*?-->", html, re.S
)]

def in_skip(i):
    return any(a <= i < b for a, b in skip_ranges)

tag_re = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>")
counts = {}
for m in tag_re.finditer(html):
    if in_skip(m.start()):
        continue
    closing, name, selfclose = m.group(1), m.group(2).lower(), m.group(3)
    if name in void_tags or selfclose:
        continue
    c = counts.setdefault(name, [0, 0])
    if closing:
        c[1] += 1
    else:
        c[0] += 1

current_diffs = {name: open_c - close_c for name, (open_c, close_c) in counts.items()}

baseline_path = os.path.join(os.path.dirname(__file__), "html_tag_baseline.json")
try:
    with open(baseline_path, "r", encoding="utf-8") as f:
        baseline = json.load(f)
except OSError:
    baseline = {}

regressions = []
for name, diff in current_diffs.items():
    base = baseline.get(name, 0)
    if diff != base:
        regressions.append(f"<{name}>: open-close diff is {diff}, was {base} in the known-good baseline")

if regressions:
    print(json.dumps({
        "systemMessage": "index.html tag balance regressed vs baseline (possible broken markup):\n" + "\n".join(regressions[:10])
    }))
sys.exit(0)
