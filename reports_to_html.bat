::jupyter nbconvert --execute --to html main.ipynb    --output docs/index.html        --HTMLExporter.theme=dark

::jupyter nbconvert --execute --to html main.ipynb --template misc/custom.tpl --output docs/index.html --HTMLExporter.theme=dark 

:: main version 
::jupyter nbconvert --execute --to html main.ipynb    --output docs/index.html        --HTMLExporter.theme=dark 
jupyter nbconvert --execute --to html main.ipynb    --output docs/index.html        --HTMLExporter.theme=dark 


:: jupyter nbconvert --execute --to slides main.ipynb --output docs/index.html --HTMLExporter.theme=dark --post serve
