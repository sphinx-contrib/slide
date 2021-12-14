slide extension README
=======================

This is a sphinx extension for embedding your presentation slides.

This extension enable you to embed your slides on slideshare_ and other sites.
Following code is sample::

   .. slide:: https://www.slideshare.net/TakeshiKomiya/blockdiag-a-simple-diagram-generator


.. _slideshare: https://www.slideshare.net/


Setting
=======

You can get archive file at https://github.com/tk0miya/sphinxcontrib-slide

Install
-------

.. code-block:: console

   $ pip install sphinxcontrib-slide


Configure Sphinx
----------------

To enable this extension, add ``sphinxcontrib.slide`` module to extensions 
option at :file:`conf.py`.

.. code-block:: python

   # Enabled extensions
   extensions = ['sphinxcontrib.slide']


Directive
=========

``.. slide:: [URL]``

   This directive insert slide interface into the generated document.
   sphinxcontrib-slide supports presentations on slideshare, googledocs, speakerdeck and slides.com.

   Examples::

      .. slide:: https://www.slideshare.net/TakeshiKomiya/blockdiag-a-simple-diagram-generator
