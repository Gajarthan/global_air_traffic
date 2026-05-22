# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_15:07:26_UTC-green)

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

**Latest saved flight:** 2026-05-22 15:07:26 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-22 15:07:26 UTC

- **91,328** saved flights
- **32,458** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **91,328** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,125,536.2 tonnes** estimated CO2 emissions
- **65,248,474 km** total distance flown
- **868 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3886 |
| 2 | SkyWest Airlines | 3376 |
| 3 | IndiGo | 1910 |
| 4 | EJA | 1726 |
| 5 | American Airlines | 1388 |
| 6 | Southwest Airlines | 1323 |
| 7 | ENY | 1123 |
| 8 | Lufthansa | 1121 |
| 9 | Delta Air Lines | 999 |
| 10 | Vueling | 870 |
| 11 | LATAM Airlines | 818 |
| 12 | AXM | 806 |
| 13 | WIF | 799 |
| 14 | AZU | 724 |
| 15 | Swiss International | 691 |
| 16 | LXJ | 687 |
| 17 | All Nippon Airways | 685 |
| 18 | Alaska Airlines | 644 |
| 19 | QLK | 644 |
| 20 | easyJet | 595 |
| 21 | EJU | 584 |
| 22 | Cathay Pacific | 580 |
| 23 | AEE | 557 |
| 24 | VIV | 542 |
| 25 | Air France | 533 |
| 26 | Japan Airlines | 484 |
| 27 | CXK | 481 |
| 28 | MXY | 469 |
| 29 | AXB | 465 |
| 30 | AIQ | 442 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 75289 |
| 2 | 🇪🇸 ES | 6459 |
| 3 | 🇮🇳 IN | 6004 |
| 4 | 🇦🇺 AU | 5690 |
| 5 | 🇩🇪 DE | 5027 |
| 6 | 🇧🇷 BR | 4999 |
| 7 | 🇮🇹 IT | 4994 |
| 8 | 🇨🇦 CA | 4594 |
| 9 | 🇯🇵 JP | 4444 |
| 10 | 🇬🇧 GB | 3900 |
| 11 | 🇫🇷 FR | 3679 |
| 12 | 🇨🇴 CO | 3149 |
| 13 | 🇲🇽 MX | 2815 |
| 14 | 🇬🇷 GR | 2617 |
| 15 | 🇳🇴 NO | 2552 |
| 16 | 🇨🇭 CH | 2398 |
| 17 | 🇲🇾 MY | 2033 |
| 18 | 🇹🇷 TR | 1662 |
| 19 | 🇿🇦 ZA | 1661 |
| 20 | 🇳🇿 NZ | 1571 |
| 21 | 🇹🇭 TH | 1550 |
| 22 | 🇵🇱 PL | 1497 |
| 23 | 🇰🇷 KR | 1449 |
| 24 | 🇵🇭 PH | 1398 |
| 25 | 🇬🇹 GT | 1366 |
| 26 | 🇲🇦 MA | 1050 |
| 27 | 🇲🇴 MO | 1035 |
| 28 | 🇳🇱 NL | 925 |
| 29 | 🇲🇪 ME | 922 |
| 30 | 🇭🇷 HR | 828 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1987 |
| 2 | Denver International Airport |  | US | 1529 |
| 3 | Tokyo International Airport |  | JP | 1480 |
| 4 | Indira Gandhi International Airport |  | IN | 1302 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1228 |
| 6 | Harry Reid International Airport |  | US | 1169 |
| 7 | Frankfurt am Main International Airport |  | DE | 1131 |
| 8 | Guaymaral Airport |  | CO | 1087 |
| 9 | Zurich Airport |  | CH | 1074 |
| 10 | La Aurora Airport |  | GT | 1044 |
| 11 | Macau International Airport |  | MO | 1035 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1002 |
| 13 | El Dorado International Airport |  | CO | 995 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 921 |
| 15 | Chicago O'Hare International Airport |  | US | 876 |
| 16 | Madrid Barajas International Airport |  | ES | 828 |
| 17 | Kuala Lumpur International Airport |  | MY | 805 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 776 |
| 19 | Salt Lake City International Airport |  | US | 766 |
| 20 | Capua Airport |  | IT | 761 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 739 |
| 22 | Malpensa International Airport |  | IT | 732 |
| 23 | Bengaluru International Airport |  | IN | 721 |
| 24 | Charles de Gaulle International Airport |  | FR | 711 |
| 25 | Charlotte/Douglas International Airport |  | US | 702 |
| 26 | Congonhas Airport |  | BR | 698 |
| 27 | Daniel K Inouye International Airport |  | US | 666 |
| 28 | Tenerife Norte Airport |  | ES | 662 |
| 29 | Ninoy Aquino International Airport |  | PH | 641 |
| 30 | Barcelona International Airport |  | ES | 615 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 605 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 597 |
| 33 | Netaji Subhash Chandra Bose International Airport |  | IN | 597 |
| 34 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 576 |
| 35 | Vitoria/Foronda Airport |  | ES | 575 |
| 36 | Don Mueang International Airport |  | TH | 569 |
| 37 | John Paul II International Airport Kraków-Balice Airport |  | PL | 566 |
| 38 | Amsterdam Airport Schiphol |  | NL | 566 |
| 39 | Calgary International Airport |  | CA | 543 |
| 40 | O. R. Tambo International Airport |  | ZA | 525 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 445 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 339 | 21m | 244 km | 1,427.4 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 251 | 24m | 225 km | 973.8 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 238 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 236 | 14m | 114 km | 462.9 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 235 | 1h 26m | 910 km | 3,687.7 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 232 | 28m | 304 km | 1,216.2 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 211 | 1h 10m | 770 km | 2,803.0 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 201 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 199 | 19m | 165 km | 566.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 188 | 26m | 275 km | 890.9 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 149 | 21m | 99 km | 255.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 138 | 31m | 369 km | 878.4 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 135 | 27m | 215 km | 500.0 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 135 | 22m | 55 km | 128.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 134 | 27m | 152 km | 350.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 132 | 14m | 154 km | 349.7 t |
| 20 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 124 | 20m | 250 km | 535.6 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 120 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 118 | 18m | 144 km | 293.5 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 25 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 26 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 112 | 1h 40m | 1,156 km | 2,234.4 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 111 | 1h 18m | 961 km | 1,839.9 t |
| 30 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 110 | 12m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N311VA |  | Portsmouth International At Pease Airport (KPSM) | Meadowbrook Airport (6MA2) | 2026-05-22 14:20 UTC | 2026-05-22 15:07 UTC | 47m |
| HBZYR | HBZ | Mengen-Hohentengen Airport (EDTM) | Mengen-Hohentengen Airport (EDTM) | 2026-05-22 14:30 UTC | 2026-05-22 15:06 UTC | 35m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-05-22 14:38 UTC | 2026-05-22 15:06 UTC | 28m |
| N29230 |  | City Of Colorado Springs Municipal Airport (KCOS) | Rocky Mountain Metro Airport (KBJC) | 2026-05-22 14:03 UTC | 2026-05-22 15:02 UTC | 59m |
| FJO66L | FJO | Bologna / Borgo Panigale Airport (LIPE) | Southampton Airport (EGHI) | 2026-05-22 13:09 UTC | 2026-05-22 15:00 UTC | 1h 50m |
| N9767F |  | Brookhaven Airport (KHWV) | Talmage Field (03NY) | 2026-05-22 14:34 UTC | 2026-05-22 14:59 UTC | 25m |
| VLG9YM | Vueling | Barcelona International Airport (LEBL) | Napoli / Capodichino International Airport (LIRN) | 2026-05-22 13:28 UTC | 2026-05-22 14:58 UTC | 1h 29m |
| N753AM |  | John Nichol's Field (0CL3) | CA75 (CA75) | 2026-05-22 14:38 UTC | 2026-05-22 14:54 UTC | 15m |
| FHRNS | FHR | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-05-22 14:07 UTC | 2026-05-22 14:53 UTC | 46m |
| N113UV |  | Provo Municipal Airport (KPVU) | Wendover Airport (KENV) | 2026-05-22 13:54 UTC | 2026-05-22 14:52 UTC | 57m |
| OYNTE | OYN | Odense Airport (EKOD) | Poznań-Ławica Airport (EPPO) | 2026-05-22 13:42 UTC | 2026-05-22 14:51 UTC | 1h 8m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-05-22 13:57 UTC | 2026-05-22 14:50 UTC | 52m |
| GFA013 | Gulf Air | Bahrain International Airport (OBBI) | Queen Alia International Airport (OJAI) | 2026-05-21 23:06 UTC | 2026-05-22 14:49 UTC | 15h 43m |
| GFA16I | Gulf Air | Frankfurt am Main International Airport (EDDF) | Queen Alia International Airport (OJAI) | 2026-05-22 11:17 UTC | 2026-05-22 14:49 UTC | 3h 31m |
| EJU82AQ | EJU | Nice-Cote d'Azur Airport (LFMN) | Napoli / Capodichino International Airport (LIRN) | 2026-05-22 13:33 UTC | 2026-05-22 14:48 UTC | 1h 15m |
| JZR8901 | JZR | Kuala Lumpur International Airport (WMKK) | Termeloh Airport (WMBE) | 2026-05-22 12:56 UTC | 2026-05-22 14:47 UTC | 1h 51m |
| N908FG |  | Trenton Mercer Airport (KTTN) | Sky Manor Airport (KN40) | 2026-05-22 13:24 UTC | 2026-05-22 14:39 UTC | 1h 14m |
| N12341 |  | Los Alamos Airport (KLAM) | Ohkay Owingeh Airport (KE14) | 2026-05-22 14:18 UTC | 2026-05-22 14:38 UTC | 19m |
| EJM529 | EJM | John Glenn Columbus International Airport (KCMH) | Grayling Army Air Field (KGOV) | 2026-05-22 13:49 UTC | 2026-05-22 14:33 UTC | 43m |
| WING35 | WIN | Mc Guire Field (Joint Base Mc Guire Dix Lakehurst) Airport (KWRI) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-05-22 12:54 UTC | 2026-05-22 14:31 UTC | 1h 36m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
