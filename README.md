# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_06:28:49_UTC-green)

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

**Latest saved flight:** 2026-07-01 06:28:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-01 06:28:49 UTC

- **125,018** saved flights
- **42,759** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **125,018** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,509,251.5 tonnes** estimated CO2 emissions
- **87,492,840 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5087 |
| 2 | SkyWest Airlines | 4635 |
| 3 | EJA | 2448 |
| 4 | IndiGo | 2375 |
| 5 | American Airlines | 1934 |
| 6 | Southwest Airlines | 1877 |
| 7 | ENY | 1569 |
| 8 | Delta Air Lines | 1489 |
| 9 | Lufthansa | 1338 |
| 10 | LATAM Airlines | 1126 |
| 11 | Vueling | 1109 |
| 12 | WIF | 1105 |
| 13 | AZU | 1057 |
| 14 | AXM | 993 |
| 15 | LXJ | 969 |
| 16 | Swiss International | 875 |
| 17 | All Nippon Airways | 841 |
| 18 | Alaska Airlines | 820 |
| 19 | easyJet | 795 |
| 20 | QLK | 784 |
| 21 | EJU | 778 |
| 22 | Cathay Pacific | 694 |
| 23 | AEE | 691 |
| 24 | VIV | 683 |
| 25 | Air France | 678 |
| 26 | United Airlines | 669 |
| 27 | CXK | 665 |
| 28 | MXY | 652 |
| 29 | JetBlue | 641 |
| 30 | GLO | 630 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 106757 |
| 2 | 🇪🇸 ES | 8361 |
| 3 | 🇮🇳 IN | 7444 |
| 4 | 🇦🇺 AU | 7312 |
| 5 | 🇧🇷 BR | 6963 |
| 6 | 🇩🇪 DE | 6610 |
| 7 | 🇮🇹 IT | 6597 |
| 8 | 🇨🇦 CA | 6570 |
| 9 | 🇬🇧 GB | 5506 |
| 10 | 🇯🇵 JP | 5485 |
| 11 | 🇫🇷 FR | 4934 |
| 12 | 🇨🇴 CO | 4032 |
| 13 | 🇲🇽 MX | 3633 |
| 14 | 🇬🇷 GR | 3568 |
| 15 | 🇳🇴 NO | 3430 |
| 16 | 🇨🇭 CH | 3192 |
| 17 | 🇹🇷 TR | 2624 |
| 18 | 🇲🇾 MY | 2570 |
| 19 | 🇿🇦 ZA | 2052 |
| 20 | 🇵🇱 PL | 2049 |
| 21 | 🇳🇿 NZ | 2025 |
| 22 | 🇹🇭 TH | 1959 |
| 23 | 🇰🇷 KR | 1941 |
| 24 | 🇵🇭 PH | 1776 |
| 25 | 🇬🇹 GT | 1731 |
| 26 | 🇲🇦 MA | 1343 |
| 27 | 🇲🇪 ME | 1243 |
| 28 | 🇲🇴 MO | 1180 |
| 29 | 🇳🇱 NL | 1178 |
| 30 | 🇧🇸 BS | 1081 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2621 |
| 2 | Denver International Airport |  | US | 2112 |
| 3 | Tokyo International Airport |  | JP | 1813 |
| 4 | Indira Gandhi International Airport |  | IN | 1638 |
| 5 | Harry Reid International Airport |  | US | 1564 |
| 6 | Guaymaral Airport |  | CO | 1520 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1501 |
| 8 | Zurich Airport |  | CH | 1382 |
| 9 | La Aurora Airport |  | GT | 1337 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1334 |
| 11 | Frankfurt am Main International Airport |  | DE | 1291 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1229 |
| 13 | Chicago O'Hare International Airport |  | US | 1210 |
| 14 | Macau International Airport |  | MO | 1180 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1101 |
| 17 | Capua Airport |  | IT | 1063 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1040 |
| 19 | Madrid Barajas International Airport |  | ES | 1035 |
| 20 | General Edward Lawrence Logan International Airport |  | US | 1014 |
| 21 | Kuala Lumpur International Airport |  | MY | 1000 |
| 22 | Congonhas Airport |  | BR | 975 |
| 23 | Charlotte/Douglas International Airport |  | US | 944 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 920 |
| 25 | Charles de Gaulle International Airport |  | FR | 907 |
| 26 | Bengaluru International Airport |  | IN | 899 |
| 27 | Malpensa International Airport |  | IT | 863 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 831 |
| 29 | Ninoy Aquino International Airport |  | PH | 823 |
| 30 | Daniel K Inouye International Airport |  | US | 801 |
| 31 | Barcelona International Airport |  | ES | 781 |
| 32 | Tenerife Norte Airport |  | ES | 768 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 764 |
| 34 | Calgary International Airport |  | CA | 736 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 731 |
| 36 | Seattle-Tacoma International Airport |  | US | 723 |
| 37 | Vitoria/Foronda Airport |  | ES | 720 |
| 38 | Scottsdale Airport |  | US | 720 |
| 39 | Amsterdam Airport Schiphol |  | NL | 715 |
| 40 | Viracopos International Airport |  | BR | 711 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 633 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 457 | 21m | 244 km | 1,924.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 324 | 24m | 225 km | 1,257.0 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 315 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 300 | 1h 10m | 770 km | 3,985.3 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 298 | 1h 25m | 910 km | 4,676.3 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 242 | 26m | 275 km | 1,146.7 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 233 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 186 | 22m | 55 km | 176.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 179 | 26m | 215 km | 662.9 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 175 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 173 | 44m | 241 km | 718.6 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 171 | 27m | 152 km | 446.9 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 160 | 1h 45m | 1,423 km | 3,926.7 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 159 | 31m | 369 km | 1,012.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 153 | 20m | 250 km | 660.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 146 | 1h 38m | 1,156 km | 2,912.6 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 146 | 1h 1m | 695 km | 1,750.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 143 | 1h 17m | 961 km | 2,370.3 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |
| 29 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 140 | 30m | 49 km | 118.3 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 136 | 1h 1m | 611 km | 1,434.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| SPHSA | SPH | Mielec Airport (EPML) | Mielec Airport (EPML) | 2026-07-01 05:53 UTC | 2026-07-01 06:28 UTC | 35m |
| NAK741 | NAK | Saint-Yan Airport (LFLN) | Clermont-Ferrand Auvergne Airport (LFLC) | 2026-07-01 05:55 UTC | 2026-07-01 06:23 UTC | 27m |
| PKSCJ | PKS | Pondok Cabe Air Base (WIHP) | Pondok Cabe Air Base (WIHP) | 2026-07-01 04:59 UTC | 2026-07-01 06:22 UTC | 1h 23m |
| ETD747 | Etihad Airways | Abu Dhabi International Airport (OMAA) | Heidelburg Airport (FAHG) | 2026-06-30 22:25 UTC | 2026-07-01 06:05 UTC | 7h 39m |
| JET | JET | Camden Airport (YSCN) | Yarrawonga Airport (YYWG) | 2026-07-01 05:01 UTC | 2026-07-01 06:05 UTC | 1h 3m |
| N741CD |  | Logan-Cache Airport (KLGU) | Wendover Airport (KENV) | 2026-07-01 04:18 UTC | 2026-07-01 05:54 UTC | 1h 35m |
| YTL | YTL | Toowoomba Wellcamp Airport (YBWW) | Brisbane Archerfield Airport (YBAF) | 2026-07-01 04:55 UTC | 2026-07-01 05:54 UTC | 58m |
| QLK324D | QLK | Brisbane International Airport (YBBN) | Pacific Haven Airport (YPAC) | 2026-07-01 05:18 UTC | 2026-07-01 05:44 UTC | 25m |
| XCN81 | XCN | Ogden-Hinckley Airport (KOGD) | Aztec Municipal Airport (KN19) | 2026-07-01 02:41 UTC | 2026-07-01 05:35 UTC | 2h 53m |
| RYR3GD | Ryanair | Bergamo / Orio Al Serio Airport (LIME) | Capua Airport (LIAU) | 2026-07-01 04:44 UTC | 2026-07-01 05:34 UTC | 50m |
| RYR471K | Ryanair | Nis Airport (LYNI) | Ioannina Airport (LGIO) | 2026-07-01 05:02 UTC | 2026-07-01 05:33 UTC | 31m |
| ASL44F | ASL | Nis Airport (LYNI) | Cemovsko Polje Airport (LYPO) | 2026-07-01 05:15 UTC | 2026-07-01 05:33 UTC | 18m |
| QLK1255 | QLK | Brisbane International Airport (YBBN) | Melbourne International Airport (YMML) | 2026-07-01 03:14 UTC | 2026-07-01 05:32 UTC | 2h 17m |
| SIS918 | SIS | Los Angeles International Airport (KLAX) | Harry Reid International Airport (KLAS) | 2026-07-01 04:42 UTC | 2026-07-01 05:28 UTC | 46m |
| UBG145 | UBG | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-07-01 05:05 UTC | 2026-07-01 05:28 UTC | 23m |
| VLG5QN | Vueling | Palma De Mallorca Airport (LEPA) | Garray Airport (LEGY) | 2026-07-01 04:39 UTC | 2026-07-01 05:27 UTC | 48m |
|  |  | Al Bateen Executive Airport (OMAD) | Zirku Airport (OMAZ) | 2026-07-01 05:11 UTC | 2026-07-01 05:25 UTC | 13m |
| SFJ13 | SFJ | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 2026-07-01 04:11 UTC | 2026-07-01 05:23 UTC | 1h 12m |
| EJU756C | EJU | Malpensa International Airport (LIMC) | Tortoli' / Arbatax Airport (LIET) | 2026-07-01 04:27 UTC | 2026-07-01 05:22 UTC | 55m |
| OAL090 | OAL | Eleftherios Venizelos International Airport (LGAV) | Skiathos Island National Airport (LGSK) | 2026-07-01 05:00 UTC | 2026-07-01 05:21 UTC | 20m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
