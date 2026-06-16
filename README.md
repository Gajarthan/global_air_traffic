# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_18:50:43_UTC-green)

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

**Latest saved flight:** 2026-06-16 18:50:43 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-16 18:50:43 UTC

- **112,370** saved flights
- **39,124** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **112,370** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,372,227.7 tonnes** estimated CO2 emissions
- **79,549,434 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4632 |
| 2 | SkyWest Airlines | 4195 |
| 3 | IndiGo | 2187 |
| 4 | EJA | 2180 |
| 5 | American Airlines | 1774 |
| 6 | Southwest Airlines | 1676 |
| 7 | ENY | 1403 |
| 8 | Delta Air Lines | 1332 |
| 9 | Lufthansa | 1263 |
| 10 | Vueling | 1029 |
| 11 | WIF | 992 |
| 12 | LATAM Airlines | 989 |
| 13 | AXM | 939 |
| 14 | AZU | 934 |
| 15 | LXJ | 857 |
| 16 | Swiss International | 804 |
| 17 | All Nippon Airways | 780 |
| 18 | Alaska Airlines | 760 |
| 19 | QLK | 734 |
| 20 | easyJet | 726 |
| 21 | EJU | 712 |
| 22 | Cathay Pacific | 664 |
| 23 | AEE | 632 |
| 24 | Air France | 626 |
| 25 | United Airlines | 626 |
| 26 | VIV | 626 |
| 27 | MXY | 598 |
| 28 | CXK | 591 |
| 29 | AXB | 552 |
| 30 | GLO | 552 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 94684 |
| 2 | 🇪🇸 ES | 7704 |
| 3 | 🇮🇳 IN | 6901 |
| 4 | 🇦🇺 AU | 6654 |
| 5 | 🇧🇷 BR | 6213 |
| 6 | 🇮🇹 IT | 6037 |
| 7 | 🇩🇪 DE | 6007 |
| 8 | 🇨🇦 CA | 5901 |
| 9 | 🇯🇵 JP | 5063 |
| 10 | 🇬🇧 GB | 4851 |
| 11 | 🇫🇷 FR | 4479 |
| 12 | 🇨🇴 CO | 3807 |
| 13 | 🇲🇽 MX | 3322 |
| 14 | 🇬🇷 GR | 3192 |
| 15 | 🇳🇴 NO | 3105 |
| 16 | 🇨🇭 CH | 2879 |
| 17 | 🇲🇾 MY | 2429 |
| 18 | 🇹🇷 TR | 2245 |
| 19 | 🇿🇦 ZA | 1911 |
| 20 | 🇰🇷 KR | 1853 |
| 21 | 🇹🇭 TH | 1840 |
| 22 | 🇳🇿 NZ | 1840 |
| 23 | 🇵🇱 PL | 1836 |
| 24 | 🇵🇭 PH | 1633 |
| 25 | 🇬🇹 GT | 1610 |
| 26 | 🇲🇦 MA | 1235 |
| 27 | 🇲🇴 MO | 1159 |
| 28 | 🇲🇪 ME | 1101 |
| 29 | 🇳🇱 NL | 1092 |
| 30 | 🇭🇷 HR | 977 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2396 |
| 2 | Denver International Airport |  | US | 1904 |
| 3 | Tokyo International Airport |  | JP | 1679 |
| 4 | Indira Gandhi International Airport |  | IN | 1502 |
| 5 | Guaymaral Airport |  | CO | 1411 |
| 6 | Harry Reid International Airport |  | US | 1409 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1387 |
| 8 | Zurich Airport |  | CH | 1264 |
| 9 | La Aurora Airport |  | GT | 1240 |
| 10 | Frankfurt am Main International Airport |  | DE | 1232 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1207 |
| 12 | Macau International Airport |  | MO | 1159 |
| 13 | El Dorado International Airport |  | CO | 1144 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1126 |
| 15 | Chicago O'Hare International Airport |  | US | 1121 |
| 16 | Capua Airport |  | IT | 976 |
| 17 | Madrid Barajas International Airport |  | ES | 975 |
| 18 | Salt Lake City International Airport |  | US | 951 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 943 |
| 20 | Kuala Lumpur International Airport |  | MY | 942 |
| 21 | Charlotte/Douglas International Airport |  | US | 866 |
| 22 | Congonhas Airport |  | BR | 865 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 840 |
| 24 | Charles de Gaulle International Airport |  | FR | 838 |
| 25 | Bengaluru International Airport |  | IN | 835 |
| 26 | Malpensa International Airport |  | IT | 814 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 771 |
| 28 | Ninoy Aquino International Airport |  | PH | 754 |
| 29 | Daniel K Inouye International Airport |  | US | 742 |
| 30 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 736 |
| 31 | Tenerife Norte Airport |  | ES | 736 |
| 32 | Barcelona International Airport |  | ES | 732 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 713 |
| 34 | Amsterdam Airport Schiphol |  | NL | 672 |
| 35 | Don Mueang International Airport |  | TH | 670 |
| 36 | Vitoria/Foronda Airport |  | ES | 666 |
| 37 | Calgary International Airport |  | CA | 662 |
| 38 | Seattle-Tacoma International Airport |  | US | 646 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 645 |
| 40 | Viracopos International Airport |  | BR | 639 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 585 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 409 | 21m | 244 km | 1,722.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 298 | 24m | 225 km | 1,156.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 293 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 275 | 14m | 114 km | 539.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 272 | 1h 25m | 910 km | 4,268.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 264 | 1h 10m | 770 km | 3,507.0 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 225 | 26m | 275 km | 1,066.2 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 167 | 20m | 99 km | 286.1 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 163 | 27m | 215 km | 603.7 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 163 | 22m | 55 km | 154.9 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 162 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 154 | 27m | 152 km | 402.5 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 152 | 31m | 369 km | 967.5 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 149 | 44m | 452 km | 1,161.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 144 | 20m | 250 km | 622.0 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 143 | 44m | 241 km | 594.0 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 135 | 1h 1m | 695 km | 1,618.2 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 133 | 1h 39m | 1,156 km | 2,653.3 t |
| 27 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 127 | 12m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 126 | 1h 17m | 961 km | 2,088.5 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 125 | 24m | 223 km | 480.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N107MR |  | Meriden Markham Municipal Airport (KMMK) | Meriden Markham Municipal Airport (KMMK) | 2026-06-16 17:56 UTC | 2026-06-16 18:50 UTC | 53m |
| N13231 |  | Hilltop Airport (40OK) | Neversweat Airport (1OK0) | 2026-06-16 18:23 UTC | 2026-06-16 18:48 UTC | 25m |
| N2760U |  | Laurinburg/Maxton Airport (KMEB) | Richmond County Airport (KRCZ) | 2026-06-16 18:20 UTC | 2026-06-16 18:43 UTC | 22m |
| N3676R |  | City Of Slaton/Larry T Neal Memorial Airport (KF49) | City Of Slaton/Larry T Neal Memorial Airport (KF49) | 2026-06-16 18:23 UTC | 2026-06-16 18:42 UTC | 18m |
| N438H |  | General Edward Lawrence Logan International Airport (KBOS) | Lebanon Municipal Airport (KLEB) | 2026-06-16 17:53 UTC | 2026-06-16 18:40 UTC | 46m |
| HBAL791 | HBA | Dangel Airport (2SD7) | 12II (12II) | 2026-06-15 06:31 UTC | 2026-06-16 18:39 UTC | 36h 8m |
| PSOIG | PSO | Jundiai Airport (SBJD) | Fazenda Sao Miguel Airport (SNTA) | 2026-06-16 17:53 UTC | 2026-06-16 18:35 UTC | 41m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Mcgahan Industrial Airpark (AK73) | 2026-06-16 17:38 UTC | 2026-06-16 18:32 UTC | 54m |
| GLT157 | GLT | Spirit Of St Louis Airport (KSUS) | Laredo International Airport (KLRD) | 2026-06-16 16:10 UTC | 2026-06-16 18:32 UTC | 2h 21m |
| FLC72 | FLC | Reno/Tahoe International Airport (KRNO) | Reno/Tahoe International Airport (KRNO) | 2026-06-16 18:31 UTC | 2026-06-16 18:32 UTC | 0m |
| N5NJ |  | NJ58 (NJ58) | NJ58 (NJ58) | 2026-06-16 18:23 UTC | 2026-06-16 18:28 UTC | 5m |
| BRG621 | BRG | Shungnak Airport (PAGH) | Ambler Airport (PAFM) | 2026-06-16 17:41 UTC | 2026-06-16 18:28 UTC | 47m |
| LYM3712 | LYM | Denver International Airport (KDEN) | Telluride Regional Airport (KTEX) | 2026-06-16 17:51 UTC | 2026-06-16 18:28 UTC | 36m |
| EJA931 | EJA | Palm Beach International Airport (KPBI) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-16 15:50 UTC | 2026-06-16 18:26 UTC | 2h 36m |
| BELIGOUF | Brussels Airlines | Lanveoc-Poulmic Air Base (LFRL) | Lanveoc-Poulmic Air Base (LFRL) | 2026-06-16 17:25 UTC | 2026-06-16 18:26 UTC | 1h 0m |
| N230DF |  | Louisville Muhammad Ali International Airport (KSDF) | St Pete-Clearwater International Airport (KPIE) | 2026-06-16 16:41 UTC | 2026-06-16 18:26 UTC | 1h 44m |
| N100J |  | Modesto City-County-Harry Sham Field (KMOD) | Allen H Tigert Airport (KU78) | 2026-06-16 16:56 UTC | 2026-06-16 18:24 UTC | 1h 28m |
| N65251 |  | Rocky Mountain Metro Airport (KBJC) | Erie Municipal Airport (KEIK) | 2026-06-16 17:59 UTC | 2026-06-16 18:24 UTC | 24m |
| N846AA |  | Palm Beach County Park Airport (KLNA) | Palm Beach County Park Airport (KLNA) | 2026-06-16 18:03 UTC | 2026-06-16 18:23 UTC | 19m |
| N5196P |  | Lancaster Airport (KLNS) | Lancaster Airport (KLNS) | 2026-06-16 17:45 UTC | 2026-06-16 18:21 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
