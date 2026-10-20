import base64,sys
src=open('src.html',encoding='utf-8').read()
logo=base64.b64encode(open('logo64.png','rb').read()).decode()
lib=open('giflib.min.js',encoding='utf-8').read()
out=src.replace('__LOGO__',logo).replace('__GIFLIB__',lib)
open('index.html','w',encoding='utf-8').write(out)
print(len(out.encode()))
