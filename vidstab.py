#!/usr/bin/env python

# Copyright (c) 2014 Yuya Unno.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
from subprocess import check_call

parser = argparse.ArgumentParser()
parser.add_argument(
    '--vcodec', default='copy',
    help='video codec (default="copy", run `ffmpeg -codecs` to show available codecs)')
parser.add_argument(
    '--acodec', default='copy',
    help='audio codec (default="copy", run `ffmpeg -codecs` to show available codecs)')
parser.add_argument(
    '-i', '--input', required=True,
    help='input video file name')
parser.add_argument(
    '-o', '--output', required=True,
    help='oputput video file name')

args = parser.parse_args()

check_call([
        'ffmpeg',
        '-i', args.input,
        '-vf', 'vidstabdetect',
        '-an', '-f', 'null', '-',
        ])
check_call([
        'ffmpeg',
        '-i', args.input,
        '-vf', 'vidstabdetect',
        '-vcodec', args.vcodec,
        '-acodec', args.acodec,
        args.output,
        ])
