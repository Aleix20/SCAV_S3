# SCAV_S3
 
Vdeos escalats en el repositori

## Task 1 Creem videos amb encode VP8, Vp9, h265, AV1
Hem utilitzat videos de qualitat 480p d'uns 20s (20s per eficiència al fer els codecs)

· vp8_480p.webm
· vp9_480p.webm
· h265_480p.mp4
· av1_480p.mkv

## Task 2 (4in1.py)
Example: 4in1.mp4
En aquest script fem una comparativa de 4 vídeos. Els posem tots en un i comparem.

El vídeo que acabem de fer, tindrà el seu propi bitrate. Aleshores, no podem comparar els bitrates dels 4 codecs, ja que realment tenen el mateix en aquest vídeo.

Un dels fets que podem analitzar, si ens fixem molt, és la qualitat que té cada codec. Podem veure que av1 segurament té la pitjor qualitat, vp8 i vp9 les millors i h265 podríem dir que està entremig.

Comentari: av1 internament quan fa el codec tarda moltíssim, deu ser per l'algorisme que utilitza.


## Task 3 (converterInterface.py)
Tkinter converter, on hem d'escollir un arxiu mp4 i aplicar una nova escala o codec.
