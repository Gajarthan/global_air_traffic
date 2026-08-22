# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_07:48:34_UTC-green)

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

**Latest saved flight:** 2026-08-22 07:48:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 07:48:34 UTC

- **224,851** saved flights
- **70,064** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **224,851** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,708,200.6 tonnes** estimated CO2 emissions
- **156,997,137 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9007 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3801 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2878 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2140 |
| 10 | AZU | 2073 |
| 11 | Vueling | 1896 |
| 12 | Lufthansa | 1847 |
| 13 | WIF | 1788 |
| 14 | LXJ | 1776 |
| 15 | easyJet | 1551 |
| 16 | Swiss International | 1493 |
| 17 | AXM | 1482 |
| 18 | QLK | 1419 |
| 19 | United Airlines | 1417 |
| 20 | EJU | 1412 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1349 |
| 23 | GLO | 1244 |
| 24 | PGT | 1234 |
| 25 | VIV | 1231 |
| 26 | Air France | 1215 |
| 27 | WMT | 1195 |
| 28 | Wizz Air | 1157 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1119 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188717 |
| 2 | 🇪🇸 ES | 14386 |
| 3 | 🇧🇷 BR | 13051 |
| 4 | 🇦🇺 AU | 12756 |
| 5 | 🇨🇦 CA | 12478 |
| 6 | 🇮🇹 IT | 12013 |
| 7 | 🇮🇳 IN | 11846 |
| 8 | 🇩🇪 DE | 11059 |
| 9 | 🇬🇧 GB | 10523 |
| 10 | 🇨🇴 CO | 9256 |
| 11 | 🇯🇵 JP | 9146 |
| 12 | 🇫🇷 FR | 8949 |
| 13 | 🇹🇷 TR | 6561 |
| 14 | 🇬🇷 GR | 6546 |
| 15 | 🇲🇽 MX | 6259 |
| 16 | 🇨🇭 CH | 5902 |
| 17 | 🇳🇴 NO | 5564 |
| 18 | 🇲🇾 MY | 3946 |
| 19 | 🇿🇦 ZA | 3871 |
| 20 | 🇹🇭 TH | 3829 |
| 21 | 🇵🇱 PL | 3722 |
| 22 | 🇳🇿 NZ | 3136 |
| 23 | 🇵🇭 PH | 3065 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2670 |
| 26 | 🇭🇷 HR | 2513 |
| 27 | 🇲🇦 MA | 2256 |
| 28 | 🇲🇪 ME | 1997 |
| 29 | 🇳🇱 NL | 1992 |
| 30 | 🇮🇩 ID | 1936 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2737 |
| 4 | Indira Gandhi International Airport |  | IN | 2728 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2326 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2271 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1814 |
| 17 | Madrid Barajas International Airport |  | ES | 1757 |
| 18 | Capua Airport |  | IT | 1723 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1677 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1667 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1591 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1587 |
| 24 | Malpensa International Airport |  | IT | 1576 |
| 25 | Charles de Gaulle International Airport |  | FR | 1549 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1464 |
| 28 | Kuala Lumpur International Airport |  | MY | 1438 |
| 29 | Barcelona International Airport |  | ES | 1388 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1368 |
| 31 | Bengaluru International Airport |  | IN | 1339 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1328 |
| 34 | Viracopos International Airport |  | BR | 1323 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1258 |
| 38 | Oslo Gardermoen Airport |  | NO | 1252 |
| 39 | Vitoria/Foronda Airport |  | ES | 1241 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1208 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 560 | 1h 7m | 770 km | 7,439.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 553 | 24m | 225 km | 2,145.4 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 354 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 337 | 1h 50m | 1,423 km | 8,270.5 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 326 | 44m | 241 km | 1,354.1 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 299 | 21m | 250 km | 1,291.5 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 286 | 1h 38m | 1,156 km | 5,705.6 t |
| 17 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 283 | 44m | 555 km | 2,709.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 281 | 24m | 218 km | 1,058.6 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 256 | 19m | 144 km | 636.8 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| HBXBO | HBX | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-08-22 07:25 UTC | 2026-08-22 07:48 UTC | 23m |
| FJKZH | FJK | Chavenay Villepreux Airport (LFPX) | Saint-Cyr-l'Ecole Airport (LFPZ) | 2026-08-22 07:20 UTC | 2026-08-22 07:43 UTC | 23m |
| AAR713 | AAR | Incheon International Airport (RKSI) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-22 05:39 UTC | 2026-08-22 07:39 UTC | 1h 59m |
| HBKMA | HBK | Zurich Airport (LSZH) | Friedrichshafen Airport (EDNY) | 2026-08-22 06:43 UTC | 2026-08-22 07:38 UTC | 55m |
| DKYCK | DKY | EDJG (EDJG) | EDJG (EDJG) | 2026-08-22 07:36 UTC | 2026-08-22 07:37 UTC | 0m |
| HBZUZ | HBZ | Meiringen Airport (LSMM) | Reichenbach Air Base (LSGR) | 2026-08-22 07:23 UTC | 2026-08-22 07:37 UTC | 13m |
| VHRIO | VHR | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-08-22 05:57 UTC | 2026-08-22 07:28 UTC | 1h 30m |
| LBQ791 | LBQ | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Teterboro Airport (KTEB) | 2026-08-22 06:40 UTC | 2026-08-22 07:19 UTC | 38m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 06:39 UTC | 2026-08-22 07:07 UTC | 28m |
| N400DP |  | Pheasant Wings Airport (26OK) | Addison Airport (KADS) | 2026-08-22 06:06 UTC | 2026-08-22 07:07 UTC | 1h 0m |
| AUA148 | Austrian Airlines | Zurich Airport (LSZH) | Vienna International Airport (LOWW) | 2026-08-22 06:04 UTC | 2026-08-22 06:57 UTC | 53m |
| RYR66YZ | Ryanair | Vienna International Airport (LOWW) | Dublin Airport (EIDW) | 2026-08-22 04:27 UTC | 2026-08-22 06:56 UTC | 2h 28m |
| SJX821 | SJX | Kansai International Airport (RJBB) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-22 04:42 UTC | 2026-08-22 06:54 UTC | 2h 12m |
| JA123F |  | Gifu Airport (RJNG) | Okadama Airport (RJCO) | 2026-08-22 05:07 UTC | 2026-08-22 06:53 UTC | 1h 45m |
| FHSCF | FHS | Tuzla Romania Airport (LRTZ) | Tuzla Romania Airport (LRTZ) | 2026-08-22 06:46 UTC | 2026-08-22 06:47 UTC | 0m |
| SWR8HZ | Swiss International | Zurich Airport (LSZH) | Luqa Airport (LMML) | 2026-08-22 04:49 UTC | 2026-08-22 06:46 UTC | 1h 56m |
| SEJYV | SEJ | Muenster Aero Airport (LSPU) | Biella / Cerrione Airport (LILE) | 2026-08-22 06:12 UTC | 2026-08-22 06:44 UTC | 32m |
| LOG32MW | LOG | Glasgow International Airport (EGPF) | XPLO (XPLO) | 2026-08-22 06:20 UTC | 2026-08-22 06:43 UTC | 23m |
| IGO7HC | IndiGo | Bengaluru International Airport (VOBL) | Kovilpatti Airport (VO26) | 2026-08-22 05:36 UTC | 2026-08-22 06:43 UTC | 1h 6m |
| UZB274 | UZB | Erzurum International Airport (LTCE) | Ukhta Airport (UUYH) | 2026-08-21 22:01 UTC | 2026-08-22 06:43 UTC | 8h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
