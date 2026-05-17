# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_17:10:20_UTC-green)

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

**Latest saved flight:** 2026-05-17 17:10:20 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-17 17:10:20 UTC

- **86,397** saved flights
- **30,947** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **86,397** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,068,487.8 tonnes** estimated CO2 emissions
- **61,941,323 km** total distance flown
- **869 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3702 |
| 2 | SkyWest Airlines | 3186 |
| 3 | IndiGo | 1865 |
| 4 | EJA | 1623 |
| 5 | American Airlines | 1323 |
| 6 | Southwest Airlines | 1252 |
| 7 | Lufthansa | 1096 |
| 8 | ENY | 1068 |
| 9 | Delta Air Lines | 942 |
| 10 | Vueling | 824 |
| 11 | AXM | 782 |
| 12 | LATAM Airlines | 780 |
| 13 | WIF | 738 |
| 14 | AZU | 675 |
| 15 | Swiss International | 672 |
| 16 | All Nippon Airways | 666 |
| 17 | LXJ | 632 |
| 18 | QLK | 625 |
| 19 | Alaska Airlines | 611 |
| 20 | easyJet | 571 |
| 21 | EJU | 555 |
| 22 | Cathay Pacific | 549 |
| 23 | AEE | 541 |
| 24 | VIV | 516 |
| 25 | Air France | 509 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 457 |
| 28 | AXB | 454 |
| 29 | MXY | 432 |
| 30 | AIQ | 426 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 70618 |
| 2 | 🇪🇸 ES | 6133 |
| 3 | 🇮🇳 IN | 5829 |
| 4 | 🇦🇺 AU | 5477 |
| 5 | 🇩🇪 DE | 4827 |
| 6 | 🇮🇹 IT | 4784 |
| 7 | 🇧🇷 BR | 4737 |
| 8 | 🇯🇵 JP | 4320 |
| 9 | 🇨🇦 CA | 4282 |
| 10 | 🇬🇧 GB | 3696 |
| 11 | 🇫🇷 FR | 3461 |
| 12 | 🇨🇴 CO | 2912 |
| 13 | 🇲🇽 MX | 2655 |
| 14 | 🇬🇷 GR | 2517 |
| 15 | 🇳🇴 NO | 2389 |
| 16 | 🇨🇭 CH | 2301 |
| 17 | 🇲🇾 MY | 1964 |
| 18 | 🇿🇦 ZA | 1621 |
| 19 | 🇹🇷 TR | 1562 |
| 20 | 🇳🇿 NZ | 1505 |
| 21 | 🇹🇭 TH | 1502 |
| 22 | 🇵🇱 PL | 1438 |
| 23 | 🇵🇭 PH | 1352 |
| 24 | 🇰🇷 KR | 1352 |
| 25 | 🇬🇹 GT | 1295 |
| 26 | 🇲🇦 MA | 1007 |
| 27 | 🇲🇴 MO | 1007 |
| 28 | 🇲🇪 ME | 902 |
| 29 | 🇳🇱 NL | 884 |
| 30 | 🇭🇷 HR | 777 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1884 |
| 2 | Denver International Airport |  | US | 1447 |
| 3 | Tokyo International Airport |  | JP | 1443 |
| 4 | Indira Gandhi International Airport |  | IN | 1251 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1201 |
| 6 | Frankfurt am Main International Airport |  | DE | 1108 |
| 7 | Harry Reid International Airport |  | US | 1093 |
| 8 | Zurich Airport |  | CH | 1031 |
| 9 | Macau International Airport |  | MO | 1007 |
| 10 | Guaymaral Airport |  | CO | 989 |
| 11 | La Aurora Airport |  | GT | 983 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 953 |
| 13 | El Dorado International Airport |  | CO | 931 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 868 |
| 15 | Chicago O'Hare International Airport |  | US | 830 |
| 16 | Madrid Barajas International Airport |  | ES | 789 |
| 17 | Kuala Lumpur International Airport |  | MY | 780 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 743 |
| 19 | Capua Airport |  | IT | 721 |
| 20 | Salt Lake City International Airport |  | US | 718 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 715 |
| 22 | Malpensa International Airport |  | IT | 712 |
| 23 | Bengaluru International Airport |  | IN | 706 |
| 24 | Charles de Gaulle International Airport |  | FR | 676 |
| 25 | Charlotte/Douglas International Airport |  | US | 668 |
| 26 | Congonhas Airport |  | BR | 664 |
| 27 | Tenerife Norte Airport |  | ES | 636 |
| 28 | Daniel K Inouye International Airport |  | US | 631 |
| 29 | Ninoy Aquino International Airport |  | PH | 619 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 584 |
| 32 | Barcelona International Airport |  | ES | 579 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 576 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 557 |
| 35 | Vitoria/Foronda Airport |  | ES | 552 |
| 36 | Don Mueang International Airport |  | TH | 544 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 543 |
| 38 | Amsterdam Airport Schiphol |  | NL | 539 |
| 39 | O. R. Tambo International Airport |  | ZA | 510 |
| 40 | Calgary International Airport |  | CA | 504 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 408 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 320 | 21m | 244 km | 1,347.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 276 | 1h 8m | 706 km | 3,360.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 230 | 1h 26m | 910 km | 3,609.2 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 221 | 14m | 114 km | 433.5 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 219 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 200 | 1h 10m | 770 km | 2,656.8 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 182 | 26m | 275 km | 862.4 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 146 | 21m | 99 km | 250.1 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 135 | 31m | 369 km | 859.3 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 130 | 27m | 152 km | 339.7 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 126 | 20m | 147 km | 318.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 124 | 14m | 154 km | 328.6 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 121 | 20m | 250 km | 522.6 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 111 | 1h 42m | 1,423 km | 2,724.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 110 | 18m | 144 km | 273.6 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 109 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 104 | 1h 41m | 1,156 km | 2,074.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N34HF |  | Newark Liberty International Airport (KEWR) | Brookhaven Airport (KHWV) | 2026-05-17 16:32 UTC | 2026-05-17 17:10 UTC | 38m |
| N52719 |  | Bent-Wing Airport (59NY) | Finger Lakes Regional Airport (K0G7) | 2026-05-17 16:28 UTC | 2026-05-17 17:06 UTC | 37m |
| CGXXJ | CGX | Edmonton / Cooking Lake Airport (CEZ3) | Edmonton / Josephburg Airport (CFB6) | 2026-05-17 16:56 UTC | 2026-05-17 17:04 UTC | 7m |
| N341WB |  | Albuquerque International Sunport Airport (KABQ) | Ohkay Owingeh Airport (KE14) | 2026-05-17 16:44 UTC | 2026-05-17 17:03 UTC | 19m |
| PHX395 | PHX | Ottawa / Macdonald-Cartier International Airport (CYOW) | Toronto Pearson International Airport (CYYZ) | 2026-05-17 16:23 UTC | 2026-05-17 17:02 UTC | 38m |
| OXF4955 | OXF | Falcon Field (KFFZ) | Four Pillars Airport (AZ21) | 2026-05-17 15:28 UTC | 2026-05-17 17:02 UTC | 1h 33m |
| N224LA |  | Whiteman Airport (KWHP) | Van Nuys Airport (KVNY) | 2026-05-17 16:05 UTC | 2026-05-17 17:02 UTC | 56m |
| HAWK286 | HAW | Kingsville Nas Airport (KNQI) | XS51 (XS51) | 2026-05-17 16:46 UTC | 2026-05-17 16:59 UTC | 13m |
| N541S |  | Huntsville International-Carl T Jones Field (KHSV) | Segars Field (K15M) | 2026-05-17 16:46 UTC | 2026-05-17 16:59 UTC | 13m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-17 16:42 UTC | 2026-05-17 16:57 UTC | 15m |
| N173AW |  | Flying Cloud Airport (KFCM) | Airlake Airport (KLVN) | 2026-05-17 15:41 UTC | 2026-05-17 16:55 UTC | 1h 13m |
| TGRIO | TGR | La Aurora Airport (MGGT) | Esquipulas Airport (MGES) | 2026-05-17 16:31 UTC | 2026-05-17 16:52 UTC | 20m |
| N415XT |  | John C Tune Airport (KJWN) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-05-17 13:13 UTC | 2026-05-17 16:50 UTC | 3h 37m |
| FFL503 | FFL | Las Cruces International Airport (KLRU) | X Bar 1 Ranch (Lower) Airport (AZ97) | 2026-05-17 15:34 UTC | 2026-05-17 16:49 UTC | 1h 14m |
| LXJ439 | LXJ | Indianapolis International Airport (KIND) | Colonel James Jabara Airport (KAAO) | 2026-05-17 15:18 UTC | 2026-05-17 16:47 UTC | 1h 29m |
| N441EH |  | Odessa-Schlemeyer Field (KODO) | K2E3 (K2E3) | 2026-05-17 14:13 UTC | 2026-05-17 16:43 UTC | 2h 29m |
| RYR1963 | Ryanair | Memmingen Allgau Airport (EDJA) | Sepurine Training Base (LD57) | 2026-05-17 15:57 UTC | 2026-05-17 16:42 UTC | 44m |
| N692DA |  | Hermanos Serdan International Airport (MMPB) | Hermanos Serdan International Airport (MMPB) | 2026-05-17 16:26 UTC | 2026-05-17 16:40 UTC | 13m |
| CHX29 | CHX | Hamburg Airport (EDDH) | Hamburg Airport (EDDH) | 2026-05-17 16:35 UTC | 2026-05-17 16:39 UTC | 3m |
| DTA124 | DTA | Quatro De Fevereiro Airport (FNLU) | Soyo Airport (FNSO) | 2026-05-17 16:02 UTC | 2026-05-17 16:36 UTC | 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
