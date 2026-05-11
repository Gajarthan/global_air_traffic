# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_18:52:47_UTC-green)

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

**Latest saved flight:** 2026-05-11 18:52:47 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-11 18:52:47 UTC

- **78,211** saved flights
- **28,545** unique routes
- **128** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **78,211** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **968,999.6 tonnes** estimated CO2 emissions
- **56,173,888 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3367 |
| 2 | SkyWest Airlines | 2912 |
| 3 | IndiGo | 1732 |
| 4 | EJA | 1442 |
| 5 | American Airlines | 1219 |
| 6 | Southwest Airlines | 1151 |
| 7 | Lufthansa | 1023 |
| 8 | ENY | 976 |
| 9 | Delta Air Lines | 852 |
| 10 | Vueling | 750 |
| 11 | AXM | 721 |
| 12 | LATAM Airlines | 713 |
| 13 | WIF | 675 |
| 14 | All Nippon Airways | 627 |
| 15 | AZU | 619 |
| 16 | Swiss International | 598 |
| 17 | QLK | 591 |
| 18 | LXJ | 569 |
| 19 | Alaska Airlines | 550 |
| 20 | easyJet | 523 |
| 21 | AEE | 508 |
| 22 | EJU | 508 |
| 23 | Cathay Pacific | 499 |
| 24 | VIV | 466 |
| 25 | Air France | 462 |
| 26 | Japan Airlines | 449 |
| 27 | AXB | 435 |
| 28 | CXK | 401 |
| 29 | MXY | 392 |
| 30 | AIQ | 387 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 63284 |
| 2 | 🇪🇸 ES | 5607 |
| 3 | 🇮🇳 IN | 5438 |
| 4 | 🇦🇺 AU | 5037 |
| 5 | 🇩🇪 DE | 4432 |
| 6 | 🇧🇷 BR | 4338 |
| 7 | 🇮🇹 IT | 4327 |
| 8 | 🇯🇵 JP | 4031 |
| 9 | 🇨🇦 CA | 3873 |
| 10 | 🇬🇧 GB | 3365 |
| 11 | 🇫🇷 FR | 3108 |
| 12 | 🇨🇴 CO | 2700 |
| 13 | 🇲🇽 MX | 2386 |
| 14 | 🇬🇷 GR | 2312 |
| 15 | 🇳🇴 NO | 2142 |
| 16 | 🇨🇭 CH | 2109 |
| 17 | 🇲🇾 MY | 1808 |
| 18 | 🇿🇦 ZA | 1486 |
| 19 | 🇹🇷 TR | 1418 |
| 20 | 🇳🇿 NZ | 1396 |
| 21 | 🇹🇭 TH | 1386 |
| 22 | 🇵🇱 PL | 1306 |
| 23 | 🇵🇭 PH | 1244 |
| 24 | 🇰🇷 KR | 1218 |
| 25 | 🇬🇹 GT | 1210 |
| 26 | 🇲🇦 MA | 923 |
| 27 | 🇲🇴 MO | 915 |
| 28 | 🇲🇪 ME | 838 |
| 29 | 🇳🇱 NL | 816 |
| 30 | 🇭🇷 HR | 681 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1726 |
| 2 | Tokyo International Airport |  | JP | 1355 |
| 3 | Denver International Airport |  | US | 1307 |
| 4 | Indira Gandhi International Airport |  | IN | 1153 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1134 |
| 6 | Frankfurt am Main International Airport |  | DE | 1027 |
| 7 | Harry Reid International Airport |  | US | 971 |
| 8 | Zurich Airport |  | CH | 925 |
| 9 | Macau International Airport |  | MO | 915 |
| 10 | La Aurora Airport |  | GT | 910 |
| 11 | Guaymaral Airport |  | CO | 892 |
| 12 | El Dorado International Airport |  | CO | 879 |
| 13 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 862 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 791 |
| 15 | Chicago O'Hare International Airport |  | US | 761 |
| 16 | Kuala Lumpur International Airport |  | MY | 726 |
| 17 | Madrid Barajas International Airport |  | ES | 723 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 693 |
| 19 | Malpensa International Airport |  | IT | 678 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 674 |
| 21 | Bengaluru International Airport |  | IN | 672 |
| 22 | Salt Lake City International Airport |  | US | 642 |
| 23 | Capua Airport |  | IT | 625 |
| 24 | Charlotte/Douglas International Airport |  | US | 617 |
| 25 | Charles de Gaulle International Airport |  | FR | 616 |
| 26 | Congonhas Airport |  | BR | 614 |
| 27 | Tenerife Norte Airport |  | ES | 584 |
| 28 | Daniel K Inouye International Airport |  | US | 567 |
| 29 | Ninoy Aquino International Airport |  | PH | 566 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 557 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 529 |
| 32 | Barcelona International Airport |  | ES | 528 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 526 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 512 |
| 35 | Vitoria/Foronda Airport |  | ES | 497 |
| 36 | Don Mueang International Airport |  | TH | 494 |
| 37 | Amsterdam Airport Schiphol |  | NL | 492 |
| 38 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 484 |
| 39 | O. R. Tambo International Airport |  | ZA | 468 |
| 40 | Calgary International Airport |  | CA | 463 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 371 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 281 | 21m | 244 km | 1,183.2 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 271 | 1h 8m | 706 km | 3,299.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 224 | 24m | 225 km | 869.0 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 216 | 28m | 304 km | 1,132.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 209 | 1h 27m | 910 km | 3,279.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 198 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 185 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 184 | 19m | 165 km | 523.4 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 173 | 1h 12m | 770 km | 2,298.2 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 166 | 26m | 275 km | 786.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 140 | 20m | 99 km | 239.8 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 136 | 44m | 452 km | 1,059.9 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 124 | 31m | 369 km | 789.3 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 119 | 27m | 215 km | 440.7 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 119 | 27m | 152 km | 311.0 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 115 | 20m | 147 km | 291.0 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 114 | 20m | 250 km | 492.4 t |
| 20 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 113 | 58m | - | - |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 111 | 14m | 154 km | 294.1 t |
| 22 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 105 | 54m | 546 km | 988.6 t |
| 23 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 104 | 1h 42m | 1,423 km | 2,552.3 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 104 | 1h 2m | 695 km | 1,246.7 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 103 | 57m | 493 km | 876.3 t |
| 26 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 102 | 23m | 55 km | 96.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |
| 28 | Bodø Airport (ENBO) | ENEN (ENEN) | 98 | 13m | - | - |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 98 | 12m | - | - |
| 30 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 98 | 18m | 144 km | 243.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N6539H |  | Hayward Executive Airport (KHWD) | Tracy Municipal Airport (KTCY) | 2026-05-11 18:15 UTC | 2026-05-11 18:52 UTC | 37m |
| N824US |  | Bolingbrook's Clow International Airport (K1C5) | Wix Airport (03IL) | 2026-05-11 18:28 UTC | 2026-05-11 18:52 UTC | 24m |
| N719HT |  | Rancho Magdalena Airport (NM01) | Rancho Magdalena Airport (NM01) | 2026-05-11 18:40 UTC | 2026-05-11 18:51 UTC | 10m |
| N350MW |  | KU77 (KU77) | KU77 (KU77) | 2026-05-11 16:24 UTC | 2026-05-11 18:51 UTC | 2h 26m |
| N797NA |  | Dubuque Regional Airport (KDBQ) | Dubuque Regional Airport (KDBQ) | 2026-05-11 18:20 UTC | 2026-05-11 18:49 UTC | 29m |
| DAL2972 | Delta Air Lines | Dallas-Fort Worth International Airport (KDFW) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 16:43 UTC | 2026-05-11 18:49 UTC | 2h 6m |
| GXA618 | GXA | Detroit Metro Wayne County Airport (KDTW) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 17:17 UTC | 2026-05-11 18:45 UTC | 1h 28m |
| N187ER |  | Long Beach (Daugherty Field) Airport (KLGB) | Long Beach (Daugherty Field) Airport (KLGB) | 2026-05-11 17:52 UTC | 2026-05-11 18:44 UTC | 52m |
| N866US |  | Brigham City Regional Airport (KBMC) | Preston Airport (KU10) | 2026-05-11 18:28 UTC | 2026-05-11 18:44 UTC | 16m |
| N92DV |  | Erie Municipal Airport (KEIK) | Vance Brand Airport (KLMO) | 2026-05-11 18:08 UTC | 2026-05-11 18:43 UTC | 35m |
| N5226L |  | Orlando Executive Airport (KORL) | Leesburg International Airport (KLEE) | 2026-05-11 17:52 UTC | 2026-05-11 18:43 UTC | 50m |
| N45941 |  | Erie Municipal Airport (KEIK) | Erie Municipal Airport (KEIK) | 2026-05-11 18:23 UTC | 2026-05-11 18:41 UTC | 18m |
| N254EK |  | Palo Alto Airport (KPAO) | Sacramento Executive Airport (KSAC) | 2026-05-11 17:56 UTC | 2026-05-11 18:41 UTC | 44m |
| N270AD |  | Beverly Regional Airport (KBVY) | Concord Municipal Airport (KCON) | 2026-05-11 18:09 UTC | 2026-05-11 18:40 UTC | 31m |
| DAL171 | Delta Air Lines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 18:25 UTC | 2026-05-11 18:36 UTC | 10m |
| N792BP |  | Portland International Airport (KPDX) | West Ranch Airport (79WT) | 2026-05-11 18:12 UTC | 2026-05-11 18:36 UTC | 23m |
| N357LP |  | Witham Field (KSUA) | Mountain Empire Airport (KMKJ) | 2026-05-11 16:28 UTC | 2026-05-11 18:34 UTC | 2h 5m |
| VAR856 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-05-11 17:35 UTC | 2026-05-11 18:32 UTC | 56m |
| DAL2864 | Delta Air Lines | Newark Liberty International Airport (KEWR) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 15:57 UTC | 2026-05-11 18:32 UTC | 2h 34m |
| AAL3236 | American Airlines | Phoenix Sky Harbor International Airport (KPHX) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-05-11 15:49 UTC | 2026-05-11 18:31 UTC | 2h 41m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
