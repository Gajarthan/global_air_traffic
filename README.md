# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_09:00:04_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-05-17 09:00:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 09:00:04 UTC

- **85,728** saved flights
- **30,752** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **85,728** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,059,959.5 tonnes** estimated CO2 emissions
- **61,446,928 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3669 |
| 2 | SkyWest Airlines | 3172 |
| 3 | IndiGo | 1846 |
| 4 | EJA | 1612 |
| 5 | American Airlines | 1318 |
| 6 | Southwest Airlines | 1246 |
| 7 | Lufthansa | 1085 |
| 8 | ENY | 1063 |
| 9 | Delta Air Lines | 936 |
| 10 | Vueling | 812 |
| 11 | AXM | 778 |
| 12 | LATAM Airlines | 778 |
| 13 | WIF | 734 |
| 14 | AZU | 668 |
| 15 | All Nippon Airways | 664 |
| 16 | Swiss International | 664 |
| 17 | LXJ | 628 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 611 |
| 20 | easyJet | 565 |
| 21 | Cathay Pacific | 545 |
| 22 | EJU | 542 |
| 23 | AEE | 539 |
| 24 | VIV | 515 |
| 25 | Air France | 500 |
| 26 | Japan Airlines | 477 |
| 27 | CXK | 453 |
| 28 | AXB | 452 |
| 29 | MXY | 427 |
| 30 | AIQ | 421 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70218 |
| 2 | 🇪🇸 ES | 6056 |
| 3 | 🇮🇳 IN | 5784 |
| 4 | 🇦🇺 AU | 5469 |
| 5 | 🇩🇪 DE | 4771 |
| 6 | 🇮🇹 IT | 4712 |
| 7 | 🇧🇷 BR | 4711 |
| 8 | 🇯🇵 JP | 4305 |
| 9 | 🇨🇦 CA | 4257 |
| 10 | 🇬🇧 GB | 3649 |
| 11 | 🇫🇷 FR | 3400 |
| 12 | 🇨🇴 CO | 2878 |
| 13 | 🇲🇽 MX | 2641 |
| 14 | 🇬🇷 GR | 2487 |
| 15 | 🇳🇴 NO | 2375 |
| 16 | 🇨🇭 CH | 2259 |
| 17 | 🇲🇾 MY | 1950 |
| 18 | 🇿🇦 ZA | 1603 |
| 19 | 🇹🇷 TR | 1536 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1492 |
| 22 | 🇵🇱 PL | 1418 |
| 23 | 🇵🇭 PH | 1348 |
| 24 | 🇰🇷 KR | 1334 |
| 25 | 🇬🇹 GT | 1290 |
| 26 | 🇲🇴 MO | 1000 |
| 27 | 🇲🇦 MA | 995 |
| 28 | 🇲🇪 ME | 894 |
| 29 | 🇳🇱 NL | 871 |
| 30 | 🇭🇷 HR | 763 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1874 |
| 2 | Denver International Airport |  | US | 1442 |
| 3 | Tokyo International Airport |  | JP | 1436 |
| 4 | Indira Gandhi International Airport |  | IN | 1241 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1193 |
| 6 | Frankfurt am Main International Airport |  | DE | 1096 |
| 7 | Harry Reid International Airport |  | US | 1083 |
| 8 | Zurich Airport |  | CH | 1017 |
| 9 | Macau International Airport |  | MO | 1000 |
| 10 | La Aurora Airport |  | GT | 979 |
| 11 | Guaymaral Airport |  | CO | 974 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 946 |
| 13 | El Dorado International Airport |  | CO | 926 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 864 |
| 15 | Chicago O'Hare International Airport |  | US | 828 |
| 16 | Madrid Barajas International Airport |  | ES | 781 |
| 17 | Kuala Lumpur International Airport |  | MY | 774 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 739 |
| 19 | Sydney Kingsford Smith International Airport |  | AU | 715 |
| 20 | Salt Lake City International Airport |  | US | 711 |
| 21 | Malpensa International Airport |  | IT | 709 |
| 22 | Capua Airport |  | IT | 702 |
| 23 | Bengaluru International Airport |  | IN | 701 |
| 24 | Charles de Gaulle International Airport |  | FR | 667 |
| 25 | Charlotte/Douglas International Airport |  | US | 665 |
| 26 | Congonhas Airport |  | BR | 661 |
| 27 | Daniel K Inouye International Airport |  | US | 630 |
| 28 | Tenerife Norte Airport |  | ES | 624 |
| 29 | Ninoy Aquino International Airport |  | PH | 617 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 582 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 573 |
| 33 | Barcelona International Airport |  | ES | 572 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 551 |
| 35 | Vitoria/Foronda Airport |  | ES | 542 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 541 |
| 37 | Don Mueang International Airport |  | TH | 538 |
| 38 | Amsterdam Airport Schiphol |  | NL | 531 |
| 39 | O. R. Tambo International Airport |  | ZA | 506 |
| 40 | Calgary International Airport |  | CA | 501 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 404 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 319 | 21m | 244 km | 1,343.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 228 | 1h 26m | 910 km | 3,577.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 225 | 28m | 304 km | 1,179.5 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 220 | 14m | 114 km | 431.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 197 | 1h 11m | 770 km | 2,617.0 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 192 | 19m | 165 km | 546.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 178 | 26m | 275 km | 843.5 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 134 | 31m | 369 km | 852.9 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 128 | 27m | 152 km | 334.5 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 125 | 20m | 147 km | 316.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 123 | 14m | 154 km | 325.9 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 122 | 23m | 55 km | 116.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 108 | 18m | 144 km | 268.6 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 105 | 12m | - | - |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 52m | 1,304 km | 2,339.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| FIN99 | Finnair | Helsinki Vantaa Airport (EFHK) | Zhuhai Airport (ZGSD) | 2026-05-16 21:47 UTC | 2026-05-17 09:00 UTC | 11h 12m |
| IGO565 | IndiGo | Lokpriya Gopinath Bordoloi International Airport (VEGT) | Ludhiana Airport (VILD) | 2026-05-17 03:18 UTC | 2026-05-17 08:56 UTC | 5h 38m |
| IGO6454 | IndiGo | Indira Gandhi International Airport (VIDP) | Dehradun Airport (VIDN) | 2026-05-17 08:26 UTC | 2026-05-17 08:56 UTC | 30m |
| IGO2747 | IndiGo | Indira Gandhi International Airport (VIDP) | Jallowal Airport (VI88) | 2026-05-17 08:18 UTC | 2026-05-17 08:56 UTC | 37m |
| THY65 | Turkish Airlines | Suvarnabhumi Airport (VTBS) | Ludhiana Airport (VILD) | 2026-05-17 04:53 UTC | 2026-05-17 08:56 UTC | 4h 2m |
| FGKDM | FGK | Lyon Corbas Airport (LFHJ) | Lyon Corbas Airport (LFHJ) | 2026-05-17 07:11 UTC | 2026-05-17 08:47 UTC | 1h 36m |
| DKYTH | DKY | Aspres-sur-Buech Airport (LFNJ) | Courchevel Airport (LFLJ) | 2026-05-17 07:49 UTC | 2026-05-17 08:37 UTC | 47m |
| HBWAK | HBW | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-05-17 08:27 UTC | 2026-05-17 08:30 UTC | 2m |
| ANE96KM | ANE | Madrid Barajas International Airport (LEMD) | Melilla Airport (GEML) | 2026-05-17 07:10 UTC | 2026-05-17 08:27 UTC | 1h 16m |
| DMDQI | DMD | Lauf-Lillinghof Airport (EDQI) | Lauf-Lillinghof Airport (EDQI) | 2026-05-17 07:57 UTC | 2026-05-17 08:19 UTC | 22m |
| HBWAK | HBW | Locarno Airport (LSZL) | Locarno Airport (LSZL) | 2026-05-17 08:01 UTC | 2026-05-17 08:16 UTC | 15m |
| N224AM |  | China Lake Naws (Armitage Field) Airport (KNID) | Inyokern Airport (KIYK) | 2026-05-17 08:00 UTC | 2026-05-17 08:12 UTC | 12m |
| GCPSS | GCP | Netheravon Airfield (EGDN) | Thruxton Aerodrome (EGHO) | 2026-05-17 08:01 UTC | 2026-05-17 08:12 UTC | 10m |
| OKLCZ | OKL | M. R. Stefanik Airport (LZIB) | Livno Brda Bosni Airport (LQLV) | 2026-05-17 07:06 UTC | 2026-05-17 08:09 UTC | 1h 3m |
| HBZTO | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-05-17 07:55 UTC | 2026-05-17 08:07 UTC | 12m |
| IBX60 | IBX | Fukuoka Airport (RJFF) | Akeno Airport (RJOE) | 2026-05-17 07:17 UTC | 2026-05-17 08:02 UTC | 45m |
| THY39P | Turkish Airlines | Melsbroek Air Base (EBMB) | Tekirdag Corlu Airport (LTBU) | 2026-05-17 05:29 UTC | 2026-05-17 07:59 UTC | 2h 29m |
| CEB192 | CEB | Ninoy Aquino International Airport (RPLL) | Loakan Airport (RPUB) | 2026-05-17 07:37 UTC | 2026-05-17 07:57 UTC | 19m |
| LLR516 | LLR | Cochin International Airport (VOCI) | Salem Airport (VOSM) | 2026-05-17 07:22 UTC | 2026-05-17 07:55 UTC | 33m |
| VLG7KA | Vueling | Sevilla Airport (LEZL) | Vitoria/Foronda Airport (LEVT) | 2026-05-17 07:01 UTC | 2026-05-17 07:55 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
