tcpser-trace-convert
====================


What is this?
-------------

This script extracts the bytes in trace data from [tcpser](https://github.com/go4retro/tcpser). It then decodes the data to utf-8 and saves it in a text file. This process is useful for capturing ANSI or other data sent by a bulletin board system (BBS).


How do I use it?
----------------

First, you need to obtain clean trace data. I recommend running `tcpser` with the `-tS` and `-l0` flags, then save the terminal output to a text file. For example, here's the command I use when running tcpser on my Mac for use with an Atari ST emulator:

```
./tcpser -l0 -v 25232 -s 19200 -tS
```

Running tcpser with those flags should produce trace data in the Mac terminal, formatted like this:
```
2024-06-29 13:07:44:123145390972928:TRACE:SR->|00b0|3a 57 3e 38 2c 37 38 2c 47 55 41 52 44 49 41 4e|:W>8,78,GUARDIAN|
2024-06-29 13:07:44:123145390972928:TRACE:SR->|00c0|20 4f 46 20 46 4f 52 45 56 45 52 40 0d 0a 47 23| OF FOREVER@..G#|
```

Copy that trace data from your console or terminal, then paste it into a text editor. Save the file with a name like `trace-capture.txt`.

Finally, run my Python script. You must specify the input filename, and you can optionally provide an output filename.

```
python3 convert.py trace-capture.txt output.txt
```

Caveats
-------

Please note: This is my quick-and-dirty solution for capturing and re-using "Instant Graphics and Sound" data from my own BBS. I believe it should also work for capturing ANSI art and other data. But I make no promises.

(There's also a pretty good chance there will be line-ending issues if you run this script on Windows. I'm a Mac user and have not tested this in a Win environment.)
