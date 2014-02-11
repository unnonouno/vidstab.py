============
 vidstab.py
============

A simple script for vide stabilization using ffmpeg and vid.stab.


Requirement
===========

- vid.stab (http://public.hronopik.de/)
- ffmepg (http://www.ffmpeg.org/)

Compile and install ffmpeg with vid.stab (with --enable-libvidstab).

Note that homebrew's ffmpeg does not support vid.stab.
Install it manually from its source.

Install guide for Mac users
---------------------------

Download source codes of vid.stab and ffmpeg.

Install vid.stab to `/usr/local`.

::

   cd /path/to/source/of/vid.stab
   cmake .
   make
   sudo make install

Set `PKG_CONFIG_PATH` that is used in the configure script of ffmpeg.

::

   export PKG_CONFIG_PATH=/usr/loca/lib/pkgconfig

ffmpeg-2.1.3 contains a bug.
It cannot be compiled with vid.stab-0.98.
Apply this patch.

  https://trac.ffmpeg.org/attachment/ticket/3296/vidstab_fix.patch

Install ffmpeg with vid.stab to `/usr/local`.
If you want to enable x264, add `--enable-libx264` option to configure, and you can install x264 with homebrew.

::

   cd /path/to/source/of/ffmpeg
   ./configure --enable-libvidstab --enable-gpl
   make
   sudo make install


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
