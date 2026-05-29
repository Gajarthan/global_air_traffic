# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_08:14:07_UTC-green)

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

**Latest saved flight:** 2026-05-29 08:14:07 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-29 08:14:07 UTC

- **96,366** saved flights
- **33,882** unique routes
- **132** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **96,366** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,180,939.4 tonnes** estimated CO2 emissions
- **68,460,254 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4052 |
| 2 | SkyWest Airlines | 3582 |
| 3 | IndiGo | 1992 |
| 4 | EJA | 1822 |
| 5 | American Airlines | 1457 |
| 6 | Southwest Airlines | 1402 |
| 7 | ENY | 1185 |
| 8 | Lufthansa | 1152 |
| 9 | Delta Air Lines | 1053 |
| 10 | Vueling | 911 |
| 11 | LATAM Airlines | 864 |
| 12 | AXM | 853 |
| 13 | WIF | 850 |
| 14 | AZU | 772 |
| 15 | LXJ | 734 |
| 16 | Swiss International | 718 |
| 17 | All Nippon Airways | 709 |
| 18 | Alaska Airlines | 672 |
| 19 | QLK | 669 |
| 20 | easyJet | 632 |
| 21 | EJU | 614 |
| 22 | Cathay Pacific | 582 |
| 23 | AEE | 580 |
| 24 | Air France | 567 |
| 25 | VIV | 566 |
| 26 | CXK | 514 |
| 27 | MXY | 510 |
| 28 | Japan Airlines | 497 |
| 29 | AXB | 488 |
| 30 | AIQ | 464 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 79637 |
| 2 | 🇪🇸 ES | 6732 |
| 3 | 🇮🇳 IN | 6294 |
| 4 | 🇦🇺 AU | 5922 |
| 5 | 🇧🇷 BR | 5286 |
| 6 | 🇩🇪 DE | 5284 |
| 7 | 🇮🇹 IT | 5212 |
| 8 | 🇨🇦 CA | 4900 |
| 9 | 🇯🇵 JP | 4599 |
| 10 | 🇬🇧 GB | 4126 |
| 11 | 🇫🇷 FR | 3911 |
| 12 | 🇨🇴 CO | 3343 |
| 13 | 🇲🇽 MX | 2955 |
| 14 | 🇬🇷 GR | 2778 |
| 15 | 🇳🇴 NO | 2700 |
| 16 | 🇨🇭 CH | 2534 |
| 17 | 🇲🇾 MY | 2165 |
| 18 | 🇹🇷 TR | 1786 |
| 19 | 🇿🇦 ZA | 1727 |
| 20 | 🇳🇿 NZ | 1651 |
| 21 | 🇹🇭 TH | 1636 |
| 22 | 🇰🇷 KR | 1589 |
| 23 | 🇵🇱 PL | 1571 |
| 24 | 🇵🇭 PH | 1455 |
| 25 | 🇬🇹 GT | 1439 |
| 26 | 🇲🇦 MA | 1093 |
| 27 | 🇲🇴 MO | 1039 |
| 28 | 🇳🇱 NL | 971 |
| 29 | 🇲🇪 ME | 948 |
| 30 | 🇭🇷 HR | 874 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2085 |
| 2 | Denver International Airport |  | US | 1630 |
| 3 | Tokyo International Airport |  | JP | 1524 |
| 4 | Indira Gandhi International Airport |  | IN | 1363 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1272 |
| 6 | Harry Reid International Airport |  | US | 1240 |
| 7 | Guaymaral Airport |  | CO | 1184 |
| 8 | Frankfurt am Main International Airport |  | DE | 1161 |
| 9 | Zurich Airport |  | CH | 1124 |
| 10 | La Aurora Airport |  | GT | 1103 |
| 11 | El Dorado International Airport |  | CO | 1041 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1039 |
| 13 | Macau International Airport |  | MO | 1039 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 966 |
| 15 | Chicago O'Hare International Airport |  | US | 925 |
| 16 | Kuala Lumpur International Airport |  | MY | 855 |
| 17 | Madrid Barajas International Airport |  | ES | 854 |
| 18 | Salt Lake City International Airport |  | US | 811 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 809 |
| 20 | Capua Airport |  | IT | 801 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 769 |
| 22 | Bengaluru International Airport |  | IN | 755 |
| 23 | Malpensa International Airport |  | IT | 753 |
| 24 | Charles de Gaulle International Airport |  | FR | 749 |
| 25 | Congonhas Airport |  | BR | 733 |
| 26 | Charlotte/Douglas International Airport |  | US | 730 |
| 27 | Daniel K Inouye International Airport |  | US | 686 |
| 28 | Tenerife Norte Airport |  | ES | 682 |
| 29 | Ninoy Aquino International Airport |  | PH | 664 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 644 |
| 31 | Barcelona International Airport |  | ES | 644 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 622 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 616 |
| 34 | Netaji Subhash Chandra Bose International Airport |  | IN | 601 |
| 35 | Amsterdam Airport Schiphol |  | NL | 599 |
| 36 | Don Mueang International Airport |  | TH | 598 |
| 37 | Vitoria/Foronda Airport |  | ES | 594 |
| 38 | John Paul II International Airport Kraków-Balice Airport |  | PL | 571 |
| 39 | Calgary International Airport |  | CA | 568 |
| 40 | O. R. Tambo International Airport |  | ZA | 550 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 487 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 356 | 21m | 244 km | 1,499.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 278 | 1h 7m | 706 km | 3,384.7 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 263 | 24m | 225 km | 1,020.3 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 256 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 245 | 14m | 114 km | 480.5 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 243 | 1h 26m | 910 km | 3,813.2 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 242 | 28m | 304 km | 1,268.6 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 223 | 1h 10m | 770 km | 2,962.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 208 | 19m | 165 km | 591.7 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 202 | 31m | - | - |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 192 | 26m | 275 km | 909.8 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 154 | 21m | 99 km | 263.8 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 145 | 14m | 154 km | 384.2 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 144 | 27m | 215 km | 533.3 t |
| 16 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 142 | 44m | 452 km | 1,106.7 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 140 | 31m | 369 km | 891.1 t |
| 18 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 138 | 22m | 55 km | 131.2 t |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 138 | 27m | 152 km | 360.6 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 131 | 20m | 250 km | 565.8 t |
| 21 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 129 | 20m | 147 km | 326.4 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 125 | 13m | - | - |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 123 | 1h 1m | 695 km | 1,474.4 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 123 | 18m | 144 km | 306.0 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 122 | 1h 39m | 1,156 km | 2,433.9 t |
| 26 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 52m | 1,304 km | 2,609.7 t |
| 27 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 28 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 114 | 1h 42m | 1,423 km | 2,797.7 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 114 | 1h 18m | 961 km | 1,889.6 t |
| 30 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RYR3JZ | Ryanair | Václav Havel Airport (LKPR) | Podgorica Airport (LYPG) | 2026-05-29 06:55 UTC | 2026-05-29 08:14 UTC | 1h 18m |
| RYR100T | Ryanair | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-05-29 07:12 UTC | 2026-05-29 08:06 UTC | 54m |
| HSOMR2 | HSO | Husum-Schwesing Airport (EDXJ) | Helgoland-Dune Airport (EDXH) | 2026-05-29 07:37 UTC | 2026-05-29 08:04 UTC | 27m |
| DETNL | DET | Barth Airport (EDBH) | Heringsdorf Airport (EDAH) | 2026-05-29 07:11 UTC | 2026-05-29 08:00 UTC | 48m |
| HBZZZ | HBZ | Winterthur Airport (LSPH) | Winterthur Airport (LSPH) | 2026-05-29 07:22 UTC | 2026-05-29 07:44 UTC | 21m |
| 6VHAD |  | Leopold Sedar Senghor International Airport (GOOY) | Banjul International Airport (GBYD) | 2026-05-29 07:12 UTC | 2026-05-29 07:41 UTC | 29m |
| THY6NP | Turkish Airlines | Istanbul Airport (LTFM) | Queen Alia International Airport (OJAI) | 2026-05-29 04:05 UTC | 2026-05-29 07:38 UTC | 3h 32m |
| SAS661 | Scandinavian Airlines | Copenhagen Kastrup Airport (EKCH) | EDPI (EDPI) | 2026-05-29 06:18 UTC | 2026-05-29 07:32 UTC | 1h 14m |
| KLM25X | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | Neustadt/Aisch Airport (EDQN) | 2026-05-29 06:39 UTC | 2026-05-29 07:32 UTC | 53m |
| WIF1DK | WIF | Sogndal Airport (ENSG) | Sogndal Airport (ENSG) | 2026-05-29 07:20 UTC | 2026-05-29 07:31 UTC | 10m |
|  |  | Tribhuvan International Airport (VNKT) | Suketar Airport (VNTJ) | 2026-05-29 07:05 UTC | 2026-05-29 07:28 UTC | 23m |
| WZZ946 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | LRPV (LRPV) | 2026-05-29 06:28 UTC | 2026-05-29 07:23 UTC | 55m |
| ULC25 | ULC | Budapest Ferenc Liszt International Airport (LHBP) | Torino / Caselle International Airport (LIMF) | 2026-05-29 05:59 UTC | 2026-05-29 07:21 UTC | 1h 22m |
| AXM5305 | AXM | Kota Kinabalu International Airport (WBKK) | Changi Air Base (WSAC) | 2026-05-29 05:21 UTC | 2026-05-29 07:13 UTC | 1h 51m |
| RYR80LC | Ryanair | Bologna / Borgo Panigale Airport (LIPE) | Václav Havel Airport (LKPR) | 2026-05-29 06:06 UTC | 2026-05-29 07:12 UTC | 1h 5m |
| AHX105 | AHX | Amakusa Airport (RJDA) | Fukuoka Airport (RJFF) | 2026-05-29 06:51 UTC | 2026-05-29 07:10 UTC | 19m |
| IPL51EG | IPL | Requena Airport (LERE) | Teruel Airport (LETL) | 2026-05-29 06:48 UTC | 2026-05-29 07:10 UTC | 21m |
| BUC598T | BUC | Burgas Airport (LBBG) | Burgas Airport (LBBG) | 2026-05-29 05:51 UTC | 2026-05-29 07:07 UTC | 1h 15m |
| AXM6419 | AXM | Penang International Airport (WMKP) | Batu Pahat Airport (WMAB) | 2026-05-29 06:26 UTC | 2026-05-29 07:06 UTC | 40m |
| OKUWE | OKU | Václav Havel Airport (LKPR) | Hradec Kralove Airport (LKHK) | 2026-05-29 06:31 UTC | 2026-05-29 07:06 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
