# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_11:03:51_UTC-green)

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

**Latest saved flight:** 2026-05-19 11:03:51 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-19 11:03:51 UTC

- **87,838** saved flights
- **31,401** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **87,838** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,088,115.7 tonnes** estimated CO2 emissions
- **63,079,169 km** total distance flown
- **871 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3765 |
| 2 | SkyWest Airlines | 3259 |
| 3 | IndiGo | 1871 |
| 4 | EJA | 1665 |
| 5 | American Airlines | 1350 |
| 6 | Southwest Airlines | 1280 |
| 7 | Lufthansa | 1103 |
| 8 | ENY | 1091 |
| 9 | Delta Air Lines | 965 |
| 10 | Vueling | 839 |
| 11 | LATAM Airlines | 792 |
| 12 | AXM | 784 |
| 13 | WIF | 753 |
| 14 | AZU | 696 |
| 15 | Swiss International | 679 |
| 16 | All Nippon Airways | 669 |
| 17 | LXJ | 644 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 624 |
| 20 | easyJet | 579 |
| 21 | EJU | 566 |
| 22 | Cathay Pacific | 561 |
| 23 | AEE | 547 |
| 24 | VIV | 528 |
| 25 | Air France | 514 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 462 |
| 28 | AXB | 458 |
| 29 | MXY | 450 |
| 30 | AIQ | 429 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 72079 |
| 2 | 🇪🇸 ES | 6233 |
| 3 | 🇮🇳 IN | 5862 |
| 4 | 🇦🇺 AU | 5502 |
| 5 | 🇩🇪 DE | 4878 |
| 6 | 🇮🇹 IT | 4877 |
| 7 | 🇧🇷 BR | 4830 |
| 8 | 🇨🇦 CA | 4390 |
| 9 | 🇯🇵 JP | 4344 |
| 10 | 🇬🇧 GB | 3747 |
| 11 | 🇫🇷 FR | 3506 |
| 12 | 🇨🇴 CO | 2979 |
| 13 | 🇲🇽 MX | 2737 |
| 14 | 🇬🇷 GR | 2550 |
| 15 | 🇳🇴 NO | 2431 |
| 16 | 🇨🇭 CH | 2324 |
| 17 | 🇲🇾 MY | 1969 |
| 18 | 🇿🇦 ZA | 1625 |
| 19 | 🇹🇷 TR | 1596 |
| 20 | 🇳🇿 NZ | 1523 |
| 21 | 🇹🇭 TH | 1510 |
| 22 | 🇵🇱 PL | 1462 |
| 23 | 🇰🇷 KR | 1365 |
| 24 | 🇵🇭 PH | 1356 |
| 25 | 🇬🇹 GT | 1323 |
| 26 | 🇲🇴 MO | 1019 |
| 27 | 🇲🇦 MA | 1016 |
| 28 | 🇲🇪 ME | 909 |
| 29 | 🇳🇱 NL | 895 |
| 30 | 🇭🇷 HR | 792 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1934 |
| 2 | Denver International Airport |  | US | 1472 |
| 3 | Tokyo International Airport |  | JP | 1449 |
| 4 | Indira Gandhi International Airport |  | IN | 1263 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1209 |
| 6 | Harry Reid International Airport |  | US | 1121 |
| 7 | Frankfurt am Main International Airport |  | DE | 1114 |
| 8 | Zurich Airport |  | CH | 1048 |
| 9 | Macau International Airport |  | MO | 1019 |
| 10 | Guaymaral Airport |  | CO | 1010 |
| 11 | La Aurora Airport |  | GT | 1004 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 975 |
| 13 | El Dorado International Airport |  | CO | 952 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 890 |
| 15 | Chicago O'Hare International Airport |  | US | 848 |
| 16 | Madrid Barajas International Airport |  | ES | 797 |
| 17 | Kuala Lumpur International Airport |  | MY | 781 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 756 |
| 19 | Capua Airport |  | IT | 744 |
| 20 | Salt Lake City International Airport |  | US | 733 |
| 21 | Malpensa International Airport |  | IT | 719 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 23 | Bengaluru International Airport |  | IN | 707 |
| 24 | Charles de Gaulle International Airport |  | FR | 684 |
| 25 | Charlotte/Douglas International Airport |  | US | 680 |
| 26 | Congonhas Airport |  | BR | 673 |
| 27 | Tenerife Norte Airport |  | ES | 646 |
| 28 | Daniel K Inouye International Airport |  | US | 644 |
| 29 | Ninoy Aquino International Airport |  | PH | 621 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 596 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 32 | Barcelona International Airport |  | ES | 592 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 583 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 565 |
| 35 | Vitoria/Foronda Airport |  | ES | 560 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 554 |
| 37 | Don Mueang International Airport |  | TH | 548 |
| 38 | Amsterdam Airport Schiphol |  | NL | 547 |
| 39 | Calgary International Airport |  | CA | 519 |
| 40 | O. R. Tambo International Airport |  | ZA | 512 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 414 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 327 | 21m | 244 km | 1,376.9 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 225 | 14m | 114 km | 441.3 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 223 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 202 | 1h 10m | 770 km | 2,683.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 193 | 19m | 165 km | 549.0 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 183 | 26m | 275 km | 867.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 127 | 27m | 215 km | 470.4 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 125 | 14m | 154 km | 331.2 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 122 | 20m | 250 km | 527.0 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 113 | 18m | 144 km | 281.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 111 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 106 | 1h 41m | 1,156 km | 2,114.7 t |
| 30 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| APZ112 | APZ | San Francisco International Airport (KSFO) | Incheon International Airport (RKSI) | 2026-05-18 22:54 UTC | 2026-05-19 11:03 UTC | 12h 9m |
| YOX | YOX | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-05-19 10:25 UTC | 2026-05-19 11:01 UTC | 35m |
| PH1469 |  | Teuge Airport (EHTE) | Teuge Airport (EHTE) | 2026-05-19 10:37 UTC | 2026-05-19 10:56 UTC | 18m |
| N350LF |  | Santa Fe Regional Airport (KSAF) | NM74 (NM74) | 2026-05-19 10:14 UTC | 2026-05-19 10:55 UTC | 40m |
| EZY9009 | easyJet | London Gatwick Airport (EGKK) | Dresden Airport (EDDC) | 2026-05-19 08:22 UTC | 2026-05-19 10:35 UTC | 2h 12m |
| ESR614 | ESR | Kansai International Airport (RJBB) | Incheon International Airport (RKSI) | 2026-05-19 09:09 UTC | 2026-05-19 10:26 UTC | 1h 17m |
| HBFWA | HBF | Lausanne-la Blecherette Airport (LSGL) | Tivat Airport (LYTV) | 2026-05-19 08:04 UTC | 2026-05-19 10:25 UTC | 2h 21m |
| N252EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-19 08:24 UTC | 2026-05-19 10:24 UTC | 2h 0m |
| SEH4JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 2026-05-19 09:54 UTC | 2026-05-19 10:19 UTC | 24m |
| WIF1326 | WIF | Bodø Airport (ENBO) | Sørkjosen Airport (ENSR) | 2026-05-19 08:30 UTC | 2026-05-19 10:17 UTC | 1h 46m |
| FDX1502 | FDX | MS00 (MS00) | 3IN4 (3IN4) | 2026-05-19 09:22 UTC | 2026-05-19 10:15 UTC | 52m |
| IBB95FY | IBB | Tenerife Norte Airport (GCXO) | Logrono-Agoncillo Airport (LELO) | 2026-05-19 07:46 UTC | 2026-05-19 10:15 UTC | 2h 29m |
| XATVO | XAT | Eurico de Aguiar Salles Airport (SBVT) | Lajinha Airport (SNLH) | 2026-05-19 10:02 UTC | 2026-05-19 10:13 UTC | 10m |
| EJA597 | EJA | Lebanon Municipal Airport (KLEB) | General Edward Lawrence Logan International Airport (KBOS) | 2026-05-19 09:33 UTC | 2026-05-19 10:09 UTC | 36m |
| RYR65BP | Ryanair | Dublin Airport (EIDW) | Birmingham International Airport (EGBB) | 2026-05-19 09:34 UTC | 2026-05-19 10:09 UTC | 34m |
| AM322 |  | Melbourne Essendon Airport (YMEN) | Kyabram Airport (YKYB) | 2026-05-19 09:44 UTC | 2026-05-19 10:05 UTC | 20m |
| NOK104 | NOK | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-05-19 09:14 UTC | 2026-05-19 10:04 UTC | 49m |
| RYR17MN | Ryanair | Malaga Airport (LEMG) | John Paul II International Airport Kraków-Balice Airport (EPKK) | 2026-05-19 06:46 UTC | 2026-05-19 10:04 UTC | 3h 17m |
| CTN39PR | CTN | Munich International Airport (EDDM) | Zemunik Airport (LDZD) | 2026-05-19 09:19 UTC | 2026-05-19 10:02 UTC | 42m |
| ANE2328 | ANE | Palma De Mallorca Airport (LEPA) | Calaf-Sallavinera Airport (LECF) | 2026-05-19 09:20 UTC | 2026-05-19 10:00 UTC | 39m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
