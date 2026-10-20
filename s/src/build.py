# Inlines the logo so index.html is one self-contained file. Run inside src/, then copy index.html up one folder.
import base64
src = open('src.html', encoding='utf-8').read()
logo = base64.b64encode(open('logo64.png', 'rb').read()).decode()
out = src.replace('__LOGO__', logo)
open('index.html', 'w', encoding='utf-8').write(out)
print(len(out.encode()), 'bytes')
