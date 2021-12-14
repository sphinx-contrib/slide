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


@pytest.mark.sphinx(testroot='docs.google.com')
def test_googledocs(app):
    app.build()

    content = (app.outdir / 'index.html').read_text()
    assert ('<iframe src="https://docs.google.com/presentation/embed?id=1GzGae1_uB05-8tJZChOJdTuuP4XFJWuak7etHKEvJqQ"'
            in content)


@pytest.mark.sphinx(testroot='speakerdeck.com')
def test_speakerdeck(app):
    app.build()

    content = (app.outdir / 'index.html').read_text()
    assert '<script async="async" class="speakerdeck-embed" data-id="c353292856a24fafa657f06778477ee1"' in content


@pytest.mark.sphinx(testroot='slides.com')
def test_slides_com(app):
    app.build()

    content = (app.outdir / 'index.html').read_text()
    assert '<iframe src="//slides.com/rtrajano/sphinx-and-read-the-docs/embed"' in content
