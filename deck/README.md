# Investor presentation

- [Editable PowerPoint](AI-Incumbent-Portfolio.pptx)
- [PDF reading copy](AI-Incumbent-Portfolio.pdf)
- [Speaker notes and source links](speaker-notes.md)
- [Presentation build source](build_deck.mjs)

The 16-slide deck presents an original investment hypothesis, its economic mechanisms, selected evidence, a financial sensitivity and the first research queue. It does not claim a track record, target return, current undervaluation or completed company diligence.

Tables, chart and foreground text remain native editable presentation objects. The PDF is a rendered reading copy. Relevant source URLs and limitations are in the PowerPoint notes and accompanying Markdown. The generated cover is conceptual artwork, not a photograph of a real facility.

## Rebuilding

`build_deck.mjs` uses JavaScript ES modules with `@oai/artifact-tool` and the Presentations skill's finalization helpers. It requires that runtime rather than a generic Node installation alone. Set absolute `REPO_DIR`, `TMP_DIR`, `SKILL_DIR` and `RUNTIME_PYTHON`, and provide the corresponding runtime Node modules in a private build directory. Export to a new filename if a prior final exists. The research files remain fully usable without the presentation runtime.

The cover asset is [incumbent-cover.jpg](assets/incumbent-cover.jpg). It was created with the built-in image-generation tool. The prompt requested a quiet editorial illustration of a physical archive beside precision industrial equipment, near-black charcoal with restrained warm highlights, detailed on the right and clear negative space on the left. No company logos, performance claims or real facility identification were requested.

After rendering and reviewing the 16 final PowerPoint slides, run `python3 deck/build_pdf.py /absolute/path/to/rendered-slides` from the repository root. The PDF script requires ReportLab and expects `slide-1.png` through `slide-16.png`. The PDF preserves the reviewed slide appearance; use the PowerPoint for editable text, tables, chart data and speaker notes.
