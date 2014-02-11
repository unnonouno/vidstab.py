============
 vidstab.py
============

A simple script for vide stabilization using ffmpeg and vid.stab.


Requirement
===========

- vid.stab (http://public.hronopik.de/)
- ffmepg (http://www.ffmpeg.org/)

Compile and install ffmpeg with vid.stab (with --enable-libvidstab).


Usage
=====

::

   stab.py [--vcodec VCODEC] [--acodec ACODEC] -i INPUT -o OUTPUT

--vcodec VCODEC  video codec (default="copy", run `ffmpeg -codecs` to show available codecs)
--acodec ACODEC  audio codec (default="copy", run `ffmpeg -codecs` to show available codecs)
-i INPUT, --input INPUT  input video file name
-o OUTPUT, --output OUTPUT  output video file name


License
=======

This script is distributed under the MIT license.
