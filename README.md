# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_19:58:03_UTC-green)

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

**Latest saved flight:** 2026-05-30 19:58:03 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-30 19:58:03 UTC

- **97,924** saved flights
- **34,400** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **97,924** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,198,596.5 tonnes** estimated CO2 emissions
- **69,483,854 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4108 |
| 2 | SkyWest Airlines | 3657 |
| 3 | IndiGo | 2010 |
| 4 | EJA | 1855 |
| 5 | American Airlines | 1488 |
| 6 | Southwest Airlines | 1418 |
| 7 | ENY | 1202 |
| 8 | Lufthansa | 1172 |
| 9 | Delta Air Lines | 1072 |
| 10 | Vueling | 926 |
| 11 | LATAM Airlines | 875 |
| 12 | WIF | 866 |
| 13 | AXM | 854 |
| 14 | AZU | 795 |
| 15 | LXJ | 744 |
| 16 | Swiss International | 726 |
| 17 | All Nippon Airways | 710 |
| 18 | Alaska Airlines | 677 |
| 19 | QLK | 669 |
| 20 | easyJet | 643 |
| 21 | EJU | 622 |
| 22 | Cathay Pacific | 589 |
| 23 | AEE | 586 |
| 24 | VIV | 575 |
| 25 | Air France | 574 |
| 26 | CXK | 526 |
| 27 | MXY | 521 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 492 |
| 30 | AIQ | 466 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 81165 |
| 2 | 🇪🇸 ES | 6858 |
| 3 | 🇮🇳 IN | 6348 |
| 4 | 🇦🇺 AU | 5928 |
| 5 | 🇧🇷 BR | 5398 |
| 6 | 🇩🇪 DE | 5389 |
| 7 | 🇮🇹 IT | 5291 |
| 8 | 🇨🇦 CA | 4977 |
| 9 | 🇯🇵 JP | 4604 |
| 10 | 🇬🇧 GB | 4203 |
| 11 | 🇫🇷 FR | 3960 |
| 12 | 🇨🇴 CO | 3431 |
| 13 | 🇲🇽 MX | 2999 |
| 14 | 🇬🇷 GR | 2832 |
| 15 | 🇳🇴 NO | 2746 |
| 16 | 🇨🇭 CH | 2568 |
| 17 | 🇲🇾 MY | 2172 |
| 18 | 🇹🇷 TR | 1846 |
| 19 | 🇿🇦 ZA | 1737 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1640 |
| 22 | 🇵🇱 PL | 1591 |
| 23 | 🇰🇷 KR | 1589 |
| 24 | 🇬🇹 GT | 1469 |
| 25 | 🇵🇭 PH | 1458 |
| 26 | 🇲🇦 MA | 1108 |
| 27 | 🇲🇴 MO | 1045 |
| 28 | 🇳🇱 NL | 992 |
| 29 | 🇲🇪 ME | 956 |
| 30 | 🇭🇷 HR | 881 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2122 |
| 2 | Denver International Airport |  | US | 1661 |
| 3 | Tokyo International Airport |  | JP | 1525 |
| 4 | Indira Gandhi International Airport |  | IN | 1378 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1287 |
| 6 | Harry Reid International Airport |  | US | 1254 |
| 7 | Guaymaral Airport |  | CO | 1235 |
| 8 | Frankfurt am Main International Airport |  | DE | 1176 |
| 9 | Zurich Airport |  | CH | 1141 |
| 10 | La Aurora Airport |  | GT | 1129 |
| 11 | El Dorado International Airport |  | CO | 1056 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1053 |
| 13 | Macau International Airport |  | MO | 1045 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 986 |
| 15 | Chicago O'Hare International Airport |  | US | 940 |
| 16 | Madrid Barajas International Airport |  | ES | 866 |
| 17 | Kuala Lumpur International Airport |  | MY | 858 |
| 18 | Salt Lake City International Airport |  | US | 826 |
| 19 | Capua Airport |  | IT | 819 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 818 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Malpensa International Airport |  | IT | 764 |
| 23 | Bengaluru International Airport |  | IN | 761 |
| 24 | Charles de Gaulle International Airport |  | FR | 759 |
| 25 | Charlotte/Douglas International Airport |  | US | 749 |
| 26 | Congonhas Airport |  | BR | 747 |
| 27 | Daniel K Inouye International Airport |  | US | 690 |
| 28 | Tenerife Norte Airport |  | ES | 687 |
| 29 | Ninoy Aquino International Airport |  | PH | 665 |
| 30 | Barcelona International Airport |  | ES | 657 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 651 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 629 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 626 |
| 34 | Amsterdam Airport Schiphol |  | NL | 610 |
| 35 | Vitoria/Foronda Airport |  | ES | 605 |
| 36 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 37 | Don Mueang International Airport |  | TH | 601 |
| 38 | Calgary International Airport |  | CA | 580 |
| 39 | John Paul II International Airport Kraków-Balice Airport |  | PL | 572 |
| 40 | O. R. Tambo International Airport |  | ZA | 554 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 511 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 360 | 21m | 244 km | 1,515.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 265 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 250 | 14m | 114 km | 490.3 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 209 | 19m | 165 km | 594.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 195 | 26m | 275 km | 924.0 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 155 | 20m | 99 km | 265.5 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 146 | 27m | 215 km | 540.7 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 141 | 22m | 55 km | 134.0 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 140 | 27m | 152 km | 365.9 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 134 | 20m | 250 km | 578.8 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 129 | 13m | - | - |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 127 | 18m | 144 km | 315.9 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 124 | 1h 39m | 1,156 km | 2,473.8 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 124 | 1h 1m | 695 km | 1,486.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 117 | 1h 43m | 1,423 km | 2,871.4 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 115 | 1h 18m | 961 km | 1,906.2 t |
| 29 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CPA3244 | Cathay Pacific | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-30 15:26 UTC | 2026-05-30 19:58 UTC | 4h 31m |
| VAR855 | VAR | Avi Suquilla Airport (KP20) | Lake Havasu City Airport (KHII) | 2026-05-30 19:39 UTC | 2026-05-30 19:57 UTC | 17m |
| HKC9458 | HKC | Indira Gandhi International Airport (VIDP) | Zhuhai Airport (ZGSD) | 2026-05-30 15:13 UTC | 2026-05-30 19:53 UTC | 4h 39m |
| CPA095 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Zhuhai Airport (ZGSD) | 2026-05-30 04:52 UTC | 2026-05-30 19:51 UTC | 14h 58m |
| DLH754 | Lufthansa | Frankfurt am Main International Airport (EDDF) | Bengaluru International Airport (VOBL) | 2026-05-30 11:35 UTC | 2026-05-30 19:47 UTC | 8h 11m |
| N6641C |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-05-30 19:35 UTC | 2026-05-30 19:45 UTC | 10m |
| N94MN |  | Whiteman Airport (KWHP) | Big Bear City Airport (KL35) | 2026-05-30 19:04 UTC | 2026-05-30 19:43 UTC | 39m |
| N732X |  | KFTG (KFTG) | Lebeau Ranch Airport (0CO5) | 2026-05-30 19:15 UTC | 2026-05-30 19:36 UTC | 21m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-30 16:40 UTC | 2026-05-30 19:32 UTC | 2h 52m |
| SAS2776 | Scandinavian Airlines | Larnaca International Airport (LCLK) | Queen Alia International Airport (OJAI) | 2026-05-30 19:09 UTC | 2026-05-30 19:31 UTC | 22m |
| N996RS |  | Hemet-Ryan Airport (KHMT) | Hemet-Ryan Airport (KHMT) | 2026-05-30 17:59 UTC | 2026-05-30 19:31 UTC | 1h 31m |
| N717CL |  | Provo Municipal Airport (KPVU) | K36U (K36U) | 2026-05-30 19:19 UTC | 2026-05-30 19:29 UTC | 10m |
| N990SC |  | Grand Prairie Municipal Airport (KGPM) | Mid-Way Regional Airport (KJWY) | 2026-05-30 19:15 UTC | 2026-05-30 19:29 UTC | 13m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-30 18:58 UTC | 2026-05-30 19:29 UTC | 31m |
| CONGO63 | CON | Southeast Colorado Regional Airport (KLAA) | Southeast Colorado Regional Airport (KLAA) | 2026-05-30 19:16 UTC | 2026-05-30 19:28 UTC | 11m |
| GOJUMP3 | GOJ | Bob Maxwell Memorial Airfield (KOKB) | Bob Maxwell Memorial Airfield (KOKB) | 2026-05-30 19:11 UTC | 2026-05-30 19:27 UTC | 16m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-05-30 19:14 UTC | 2026-05-30 19:26 UTC | 12m |
| N49TT |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-05-30 19:07 UTC | 2026-05-30 19:25 UTC | 18m |
| BOE507 | BOE | Seattle Paine Field International Airport (KPAE) | 74WA (74WA) | 2026-05-30 16:54 UTC | 2026-05-30 19:24 UTC | 2h 30m |
| MEDEVC01 | MED | Helgoland-Dune Airport (EDXH) | Heide-Busum Airport (EDXB) | 2026-05-30 18:57 UTC | 2026-05-30 19:24 UTC | 26m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
