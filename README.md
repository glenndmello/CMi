# CMi

CMi is pronounced "See me!", because it wants you to. It's a Mac-based media center like for example XBMC, Boxee, etc. 

![CMi version 2.0](https://github.com/boxed/CMi/raw/master/screenshots/2013-04-21_1.png)


## Why I wasn't satisfied with existing systems

Short version: death by a thousand paper cuts.

Longer version: XBMC was the closest to an acceptable system but I still had to write tons of python to sit in front of it just so it would understand the files I was downloading. Then it had all these annoying issues like when you press play there is no visual indication that you actually pressed a button until the video starts playing, so you hit play again and then that pauses the video when it does eventually show up. Oh and the GUI where up on the remote moves you some random direction because the skin doesn't handle these things. Blech.

## What does it do?

* It scans your download folder and automatically figures out if you have episodes from TV shows or movies in there and will handle that correctly. Without any configuration. At all.
* It keeps track of what you've watched.
* Even if you get a power outage it will still remember where you were in the video when you restart the video.
* It will automatically clear out old files by sending them to the trash (not deleting them without a trace!)
* It will show you the weather :P
* It has some nice animations that were heavily inspired by Microsofts Metro style.
* It has a plugin API: https://github.com/boxed/CMi/wiki/Plugin-API

## Installing

1. <a href="https://github.com/boxed/CMi/releases">Download the binary</a>. 
2. Run it (you might need to right-click the file and choose "Run" since I haven't signed the binary).
3. There is no 3!

## Building

1. After cloning the repository, run "git submodule update --init" to get the dependencies.
2. Open up CMi.xcodeproject and hit build.
3. There is no 3!
