# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_13:44:18_UTC-green)

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

**Latest saved flight:** 2026-08-14 13:44:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-14 13:44:18 UTC

- **195,194** saved flights
- **61,378** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **195,194** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,332,844.5 tonnes** estimated CO2 emissions
- **135,237,364 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7768 |
| 2 | SkyWest Airlines | 7016 |
| 3 | EJA | 3836 |
| 4 | IndiGo | 3370 |
| 5 | Southwest Airlines | 3031 |
| 6 | American Airlines | 3015 |
| 7 | ENY | 2410 |
| 8 | Delta Air Lines | 2298 |
| 9 | LATAM Airlines | 1828 |
| 10 | AZU | 1756 |
| 11 | Lufthansa | 1689 |
| 12 | Vueling | 1631 |
| 13 | WIF | 1615 |
| 14 | LXJ | 1543 |
| 15 | easyJet | 1347 |
| 16 | Swiss International | 1323 |
| 17 | AXM | 1277 |
| 18 | EJU | 1209 |
| 19 | QLK | 1208 |
| 20 | All Nippon Airways | 1184 |
| 21 | Alaska Airlines | 1158 |
| 22 | VIV | 1071 |
| 23 | GLO | 1047 |
| 24 | Air France | 1026 |
| 25 | PGT | 1017 |
| 26 | AEE | 1003 |
| 27 | United Airlines | 995 |
| 28 | CXK | 990 |
| 29 | WMT | 977 |
| 30 | Wizz Air | 968 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 165805 |
| 2 | 🇪🇸 ES | 12615 |
| 3 | 🇧🇷 BR | 11194 |
| 4 | 🇦🇺 AU | 11009 |
| 5 | 🇨🇦 CA | 10669 |
| 6 | 🇮🇳 IN | 10548 |
| 7 | 🇮🇹 IT | 10158 |
| 8 | 🇩🇪 DE | 9707 |
| 9 | 🇬🇧 GB | 9184 |
| 10 | 🇯🇵 JP | 7984 |
| 11 | 🇫🇷 FR | 7797 |
| 12 | 🇨🇴 CO | 7589 |
| 13 | 🇬🇷 GR | 5739 |
| 14 | 🇲🇽 MX | 5510 |
| 15 | 🇹🇷 TR | 5299 |
| 16 | 🇨🇭 CH | 5290 |
| 17 | 🇳🇴 NO | 5007 |
| 18 | 🇲🇾 MY | 3341 |
| 19 | 🇿🇦 ZA | 3298 |
| 20 | 🇵🇱 PL | 3225 |
| 21 | 🇹🇭 TH | 3032 |
| 22 | 🇳🇿 NZ | 2739 |
| 23 | 🇵🇭 PH | 2587 |
| 24 | 🇬🇹 GT | 2468 |
| 25 | 🇰🇷 KR | 2383 |
| 26 | 🇭🇷 HR | 2034 |
| 27 | 🇲🇦 MA | 1983 |
| 28 | 🇳🇱 NL | 1760 |
| 29 | 🇲🇪 ME | 1686 |
| 30 | 🇮🇩 ID | 1580 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4053 |
| 2 | Denver International Airport |  | US | 3185 |
| 3 | Tokyo International Airport |  | JP | 2449 |
| 4 | Guaymaral Airport |  | CO | 2417 |
| 5 | Indira Gandhi International Airport |  | IN | 2383 |
| 6 | Harry Reid International Airport |  | US | 2253 |
| 7 | Zurich Airport |  | CH | 2067 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2066 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2016 |
| 10 | La Aurora Airport |  | GT | 1898 |
| 11 | El Dorado International Airport |  | CO | 1780 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1746 |
| 13 | Salt Lake City International Airport |  | US | 1734 |
| 14 | Chicago O'Hare International Airport |  | US | 1702 |
| 15 | Frankfurt am Main International Airport |  | DE | 1653 |
| 16 | Congonhas Airport |  | BR | 1630 |
| 17 | Madrid Barajas International Airport |  | ES | 1538 |
| 18 | Macau International Airport |  | MO | 1531 |
| 19 | Capua Airport |  | IT | 1496 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1493 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1437 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1399 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1362 |
| 24 | Malpensa International Airport |  | IT | 1354 |
| 25 | Charles de Gaulle International Airport |  | FR | 1340 |
| 26 | Charlotte/Douglas International Airport |  | US | 1291 |
| 27 | Kuala Lumpur International Airport |  | MY | 1245 |
| 28 | Bengaluru International Airport |  | IN | 1239 |
| 29 | Ninoy Aquino International Airport |  | PH | 1223 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1215 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1197 |
| 32 | Barcelona International Airport |  | ES | 1173 |
| 33 | Viracopos International Airport |  | BR | 1130 |
| 34 | Seattle-Tacoma International Airport |  | US | 1121 |
| 35 | Calgary International Airport |  | CA | 1112 |
| 36 | Reno/Tahoe International Airport |  | US | 1104 |
| 37 | Oslo Gardermoen Airport |  | NO | 1102 |
| 38 | Daniel K Inouye International Airport |  | US | 1087 |
| 39 | Vitoria/Foronda Airport |  | ES | 1070 |
| 40 | Tenerife Norte Airport |  | ES | 1069 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 998 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 715 | 21m | 244 km | 3,010.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 474 | 1h 7m | 770 km | 6,296.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 455 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 453 | 24m | 225 km | 1,757.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 335 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 328 | 27m | 275 km | 1,554.3 t |
| 8 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 321 | 8m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 304 | 1h 7m | 706 km | 3,701.2 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 292 | 44m | 241 km | 1,212.9 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 281 | 1h 49m | 1,423 km | 6,896.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 277 | 22m | 55 km | 263.3 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 243 | 27m | 215 km | 900.0 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 239 | 24m | 218 km | 900.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 237 | 1h 15m | 961 km | 3,928.4 t |
| 22 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 236 | 19m | 99 km | 404.3 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 236 | 12m | - | - |
| 24 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 233 | 50m | 556 km | 2,233.5 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 230 | 1h 38m | 1,156 km | 4,588.4 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 229 | 19m | 144 km | 569.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 222 | 31m | 369 km | 1,413.1 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 212 | 28m | 152 km | 554.0 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 211 | 1h 3m | 695 km | 2,529.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MTU93 | MTU | Bomar Field/Shelbyville Municipal Airport (KSYI) | Lebanon Municipal Airport (KM54) | 2026-08-14 13:14 UTC | 2026-08-14 13:44 UTC | 29m |
| N53068 |  | Bentonville Municipal/Louise M Thaden Field (KVBT) | Bentonville Municipal/Louise M Thaden Field (KVBT) | 2026-08-14 12:42 UTC | 2026-08-14 13:38 UTC | 55m |
| AIP1842 | AIP | Denver International Airport (KDEN) | 1CO7 (1CO7) | 2026-08-14 13:02 UTC | 2026-08-14 13:29 UTC | 26m |
| SCA42 | SCA | Scottsdale Airport (KSDL) | Scottsdale Airport (KSDL) | 2026-08-14 13:07 UTC | 2026-08-14 13:28 UTC | 21m |
| N2649J |  | Witham Field (KSUA) | Witham Field (KSUA) | 2026-08-14 12:14 UTC | 2026-08-14 13:25 UTC | 1h 11m |
| N187ND |  | Lm Ranch Airport (TA93) | Campbell Field (06XS) | 2026-08-14 12:49 UTC | 2026-08-14 13:25 UTC | 35m |
| BPX298 | BPX | Daytona Beach International Airport (KDAB) | The 2A Ranch Airport (0FD0) | 2026-08-14 12:16 UTC | 2026-08-14 13:20 UTC | 1h 3m |
| XSR732 | XSR | Kansas City Downtown/Wheeler Field (KMKC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-14 12:02 UTC | 2026-08-14 13:19 UTC | 1h 17m |
| MILAN78 | MIL | Bordeaux-Merignac (BA 106) Airport (LFBD) | Beziers-Vias Airport (LFMU) | 2026-08-14 12:20 UTC | 2026-08-14 13:19 UTC | 59m |
| N172NF |  | Albuquerque International Sunport Airport (KABQ) | 55NM (55NM) | 2026-08-14 12:48 UTC | 2026-08-14 13:17 UTC | 29m |
| TVQ6168 | TVQ | M. R. Stefanik Airport (LZIB) | Karain Airport (LTXE) | 2026-08-14 11:08 UTC | 2026-08-14 13:17 UTC | 2h 9m |
| CJT490 | CJT | Louisville Muhammad Ali International Airport (KSDF) | Vancouver International Airport (CYVR) | 2026-08-14 08:59 UTC | 2026-08-14 13:14 UTC | 4h 15m |
| VJT503 | VJT | Mikonos Airport (LGMK) | Karain Airport (LTXE) | 2026-08-14 12:28 UTC | 2026-08-14 13:13 UTC | 45m |
| N889BA |  | Conroe/North Houston Regional Airport (KCXO) | Lauderdale Airport (49TA) | 2026-08-14 12:54 UTC | 2026-08-14 13:13 UTC | 19m |
| GSFLA | GSF | Southampton Airport (EGHI) | Isle of Wight / Sandown Airport (EGHN) | 2026-08-14 12:56 UTC | 2026-08-14 13:10 UTC | 14m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-14 12:52 UTC | 2026-08-14 13:08 UTC | 16m |
| GKA262 | GKA | Laurinburg/Maxton Airport (KMEB) | Laurinburg/Maxton Airport (KMEB) | 2026-08-14 12:49 UTC | 2026-08-14 13:01 UTC | 12m |
| SXS4UA | SXS | London Stansted Airport (EGSS) | Karain Airport (LTXE) | 2026-08-14 09:09 UTC | 2026-08-14 12:59 UTC | 3h 49m |
| HK5182G |  | Enrique Olaya Herrera Airport (SKMD) | SKAN (SKAN) | 2026-08-14 12:34 UTC | 2026-08-14 12:58 UTC | 24m |
| N6868P |  | Flying Cloud Airport (KFCM) | Robertson Field (MY56) | 2026-08-14 12:19 UTC | 2026-08-14 12:58 UTC | 38m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
