#!/usr/bin/env python
import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.path.split(os.getcwd())[0]) # for embedded use
sys.path.append(os.path.join(os.path.split(os.getcwd())[0], 'django')) # for development

from CMi.engine import *
# Not supported:
# Boston Legal - 420 - Patriot Acts.avi|tv show|boston legal

s = """
House.S07E23.Moving.On.HDTV.XviD-2HD.avi|tv show|house|(7, 23)
[PDTV-Xvid-Mp3-ITA] Dexter S05E11 [CR-Bt].avi|tv show|dexter|(5, 11)
Glee.S02E22.HDTV.XviD-LOL.[VTV].avi|tv show|glee|(2, 22)
The.Colbert.Report.2011.05.31.James.B.Stewart.HDTV.XviD-FQM.[VTV].avi|tv show|the colbert report|2011-05-31 00:00:00
The.Daily.Show.2011.05.31.Jimmy.Fallon.HDTV.XviD-FQM.[VTV].avi|tv show|the daily show|2011-05-31 00:00:00
(download at superseeds.org) Penn And Teller Fool Us S01E05 WS PDTV XviD-SuperS|tv show|penn and teller fool us|(1, 5)
(download at superseeds.org) Penn.And.Teller.Fool.Us.S01E07.WS.PDTV.XviD-SuperS|tv show|penn and teller fool us|(1, 7)
[ www.Speed.Cd ] - Penn.And.Teller.Fool.Us.S01E08.720p.HDTV.x264-ANGELiC|tv show|penn and teller fool us|(1, 8)
[ www.TorrentDay.com ] - Penn.And.Teller.Fool.Us.S01E04.HDTV.XviD-COHD|tv show|penn and teller fool us|(1, 4)
[ www.TorrentDay.com ] - Penn.And.Teller.Fool.Us.S01E06.HDTV.XviD-BARGE|tv show|penn and teller fool us|(1, 6)
[ www.TorrentDay.com ] - So.You.Think.You.Can.Dance.S08E18.Top.8.Perform.HDTV.XviD-FQM|tv show|so you think you can dance|(8, 18)
[ www.TorrentDay.com ] - So.You.Think.You.Can.Dance.S08E19.2.of.8.Voted.Off.HDTV.XviD-FQM|tv show|so you think you can dance|(8, 19)
Brotherhood.of.the.Rose.1989.Eng.DVDRip.XVID|movie|brotherhood of the rose|1989
Crazy.Stupid.Love.DVDRip.XviD-TWiZTED|movie|crazy stupid love|0
Friends with Benefits 2011 R5 LiNE READNFO XViD - IMAGiNE|movie|friends with benefits|2011
In Time 2011 TS XviD READNFO - MiSTERE|movie|in time|2011
So.You.Think.You.Can.Dance.S08E20.Top.6.Perform.HDTV.XviD-FQM.avi|tv show|so you think you can dance|(8, 20)
X-Men First Class 2011 R5 LiNE READNFO XViD - IMAGiNE|movie|x men first class|2011
Your Highness (2011) DVDRip XviD-MAXSPEED|movie|your highness|2011
White Collar S02E14 Payback HDTV XviD-FQM|tv show|white collar|(2, 14)
White.Collar.S02E10.Burkes.Seven.HDTV.XviD-FQM.avi|tv show|white collar|(2, 10)
Boston Legal - [S05E01] - Smoke Signals.avi|tv show|boston legal|(5, 1)
Boston Legal - 05x02 - Guardians and Gatekeepers.avi|tv show|boston legal|(5, 2)
Boston Legal - 5x2 - Dances With Wolves.avi|tv show|boston legal|(5, 2)
Boston Legal - (S05E04) - True Love.avi|tv show|boston legal|(5, 4)
Glee S03E06 Mash Off HDTV XviD-LOL [eztv]|tv show|glee|(3, 6)
Glee S03E06 Mash Off HDTV XviD-LOL [eztv].avi|tv show|glee|(3, 6)
Greys Anatomy S08E08 Heart-Shaped Box HDTV.XviD-LOL.[VTV].avi|tv show|greys anatomy|(8, 8)
House S08E05 The Confession HDTV XviD-ASAP [eztv]|tv show|house|(8, 5)
House S08E06 Parents HDTV XviD-2HD [eztv]|tv show|house|(8, 6)
House.S08E03.HDTV.XviD-LOL.avi|tv show|house|(8, 3)
House.S08E04.HDTV.XviD-LOL.avi|tv show|house|(8, 4)
30.Minutes.Or.Less.2011.BDRip-HDT.avi|movie|30 minutes or less|2011
Iron Man 2008.720p BluRay DTS x264-ESiR|movie|iron man|2008
Iron.Man.2.2010.720p.BluRay.x264-WiKi|movie|iron man 2|2010
Midnight.in.Paris.DVDRip.XviD-TARGET|movie|midnight in paris|0
Water for Elephants (2011) DVDRip XviD-MAXSPEED|movie|water for elephants|2011
Where.The.Wild.Things.Are.720p.Bluray.x264-HUBRIS|movie|where the wild things are|0
1000.Ways.To.Die.S05E22.HDTV.XviD-aAF|tv show|1000 ways to die|(5, 22)
90210.S04E10.480p.WEB-DL.x264-mSD|tv show|90210|(4, 10)
The X Files-I Want To Believe[2008]DvDrip-aXXo|movie|the x files i want to believe|2008
X-Files 1x24 - The Erlenmeyer Flask.avi|tv show|x files|(1, 24)
The.Colbert.Report.2011.06.07.Sugar.Ray.Leonard.HDTV.XviD-FQM.[VTV].avi|tv show|the colbert report|2011-06-07 00:00:00
(download at superseeds.org) Penn.And.Teller.Fool.Us.S01E07.WS.PDTV.XviD-SuperS|tv show|penn and teller fool us|(1, 7)
[ www.Speed.Cd ] - Penn.And.Teller.Fool.Us.S01E08.720p.HDTV.x264-ANGELiC|tv show|penn and teller fool us|(1, 8)
[ www.Torrenting.com ] - Triumph of the Nerds (1996)-DVDRIp Xvid-THC|movie|triumph of the nerds|1996
A.Separation.2011.LiMiTED.BDRip.XviD- LPD|movie|a separation|2011
Arthur Christmas 2011 TS AVI -THEONE1982-|movie|arthur christmas|2011
Cowboys.And.Aliens.2011.SWESUB.DVDRip.x264.AC3-snuttebullen|movie|cowboys and aliens|2011
The.Women.On.The.6th.Floor.2010.SWESUB.DVDRip.XviD-CrilleKex|movie|the women on the 6th floor|2010
X-Men The Last Stand|movie|x men the last stand|0
How I Met Your Mother S07E06 - 2011 - 720p - 200MB-sD|tv show|how i met your mother|(7, 6)
Doctor.Who.2005.6x09.Night.Terrors.720p.HDTV.x264-FoV.mkv|tv show|doctor who 2005|(6, 9)
Futurama/Season 1/S1E02.avi|tv show|futurama|(1, 2)
Futurama/Season 1/S1EP03.avi|tv show|futurama|(1, 3)
Futurama/Season 2/S2E02.avi|tv show|futurama|(2, 2)
Men in Black 2 - [2002] HDDVDRip 720p H264-3Li|movie|men in black 2|2002
Men.In.Black.1997.720p.BRRip.XviD.AC3-anoXmous|movie|men in black|1997
"""

def classify(s):
#    print s
    raw_data, classification, name, result = s.split('|')
    r = match_file(raw_data)
    r = (r[0], r[1], r[2], str(r[3]))
    if r:
        if r[0] != classification or r[2] != name or r[3] != result:
            print 'FAILED: %s\n\tFound:   \t%s\n\tExpected:\t%s' % (s, r, (classification, raw_data, name, result))
#    else:
#        print '$', s, r

for line in s.strip().split('\n'):
    classify(line)