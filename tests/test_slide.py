import pytest


@pytest.mark.sphinx(testroot='slideshare.net')
def test_slideshare(app):
    app.build()

    content = (app.outdir / 'index.html').read_text()
    assert '<iframe src="https://www.slideshare.net/slideshow/embed_code/key/ziw24LtuPZYtyL"' in content
    assert ('<a href="http://www.slideshare.net/TakeshiKomiya/blockdiag-a-simple-diagram-generator"'
            ' title="blockdiag - a simple diagram generator" target="_blank">'
            'blockdiag - a simple diagram generator</a>' in content)
    assert '<a href="https://www.slideshare.net/TakeshiKomiya" target="_blank">Takeshi Komiya</a>' in content
