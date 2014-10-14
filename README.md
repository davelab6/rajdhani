Rajdhani
========

Rajdhani is an open source type family supporting both Devanagari and Latin scripts. The family was developed for use in headlines and other display-sized text. Its initial release includes five weights.

The letterforms are modularised; their squared and condensed appearance may be interpreted as being technical or even futuristic. Typically round bowls and other letterform elements have straight sides in Rajdhani. Its stroke terminals typically end in flat line segments that terminate either on a horizontal or a vertical, rather than on a diagonal. Their corners are slightly rounded, giving stroke-endings a softer feeling, rather than a pointy one.

Satya Rajpurohit and Jyotish Sonowal developed the Devanagari part in the Rajdhani family together, while the Latin was designed by Shiva Nalleperumal. The Indian Type Foundry first published the family in 2014.

## Boilerplate

Rajdhani’s working directory, including build scripts and OpenType features files, is inheriteded from [the common code base](https://github.com/itfoundry/boilerplate-gfd) we built for Google Fonts projects.

## Dependencies

- [Adobe Font Development Kit for OpenType (AFDKO)](http://www.adobe.com/devnet/opentype/afdko.html), version 2.5 build 63209 (Sep 18 2014) or newer.
- Extra Python [scripts](https://github.com/adobe-type-tools/python-scripts) and [modules](https://github.com/adobe-type-tools/python-modules) for AFDKO, to be placed in the directory `FDK/Tools/osx`).
- [RoboFab](http://robofab.org/)

## Build

Run `python build.py` to build OTFs from UFO masters. For details, see `build.py` and the module `itfgfd.py`.
