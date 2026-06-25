# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_23:58:01_UTC-green)

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

**Latest saved flight:** 2026-06-24 23:58:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-24 23:58:01 UTC

- **119,587** saved flights
- **41,185** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **119,587** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,447,080.6 tonnes** estimated CO2 emissions
- **83,888,730 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4918 |
| 2 | SkyWest Airlines | 4418 |
| 3 | EJA | 2313 |
| 4 | IndiGo | 2303 |
| 5 | American Airlines | 1860 |
| 6 | Southwest Airlines | 1783 |
| 7 | ENY | 1493 |
| 8 | Delta Air Lines | 1415 |
| 9 | Lufthansa | 1312 |
| 10 | Vueling | 1077 |
| 11 | LATAM Airlines | 1060 |
| 12 | WIF | 1060 |
| 13 | AZU | 997 |
| 14 | AXM | 974 |
| 15 | LXJ | 909 |
| 16 | Swiss International | 839 |
| 17 | All Nippon Airways | 818 |
| 18 | Alaska Airlines | 791 |
| 19 | easyJet | 769 |
| 20 | QLK | 764 |
| 21 | EJU | 749 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 666 |
| 24 | United Airlines | 656 |
| 25 | VIV | 656 |
| 26 | Air France | 652 |
| 27 | CXK | 639 |
| 28 | MXY | 630 |
| 29 | AXB | 593 |
| 30 | JetBlue | 590 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 101298 |
| 2 | 🇪🇸 ES | 8136 |
| 3 | 🇮🇳 IN | 7230 |
| 4 | 🇦🇺 AU | 7036 |
| 5 | 🇧🇷 BR | 6590 |
| 6 | 🇩🇪 DE | 6384 |
| 7 | 🇮🇹 IT | 6378 |
| 8 | 🇨🇦 CA | 6293 |
| 9 | 🇯🇵 JP | 5326 |
| 10 | 🇬🇧 GB | 5250 |
| 11 | 🇫🇷 FR | 4754 |
| 12 | 🇨🇴 CO | 4012 |
| 13 | 🇲🇽 MX | 3495 |
| 14 | 🇬🇷 GR | 3410 |
| 15 | 🇳🇴 NO | 3290 |
| 16 | 🇨🇭 CH | 3074 |
| 17 | 🇲🇾 MY | 2533 |
| 18 | 🇹🇷 TR | 2453 |
| 19 | 🇿🇦 ZA | 2013 |
| 20 | 🇵🇱 PL | 1965 |
| 21 | 🇳🇿 NZ | 1936 |
| 22 | 🇹🇭 TH | 1909 |
| 23 | 🇰🇷 KR | 1902 |
| 24 | 🇵🇭 PH | 1717 |
| 25 | 🇬🇹 GT | 1675 |
| 26 | 🇲🇦 MA | 1291 |
| 27 | 🇲🇪 ME | 1190 |
| 28 | 🇲🇴 MO | 1172 |
| 29 | 🇳🇱 NL | 1148 |
| 30 | 🇭🇷 HR | 1035 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2516 |
| 2 | Denver International Airport |  | US | 2008 |
| 3 | Tokyo International Airport |  | JP | 1764 |
| 4 | Indira Gandhi International Airport |  | IN | 1589 |
| 5 | Guaymaral Airport |  | CO | 1502 |
| 6 | Harry Reid International Airport |  | US | 1485 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1450 |
| 8 | Zurich Airport |  | CH | 1332 |
| 9 | La Aurora Airport |  | GT | 1293 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1272 |
| 11 | Frankfurt am Main International Airport |  | DE | 1267 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1184 |
| 13 | Macau International Airport |  | MO | 1172 |
| 14 | El Dorado International Airport |  | CO | 1171 |
| 15 | Chicago O'Hare International Airport |  | US | 1170 |
| 16 | Salt Lake City International Airport |  | US | 1029 |
| 17 | Capua Airport |  | IT | 1028 |
| 18 | Madrid Barajas International Airport |  | ES | 1007 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 999 |
| 20 | Kuala Lumpur International Airport |  | MY | 979 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 923 |
| 22 | Congonhas Airport |  | BR | 921 |
| 23 | Charlotte/Douglas International Airport |  | US | 908 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 886 |
| 25 | Charles de Gaulle International Airport |  | FR | 874 |
| 26 | Bengaluru International Airport |  | IN | 873 |
| 27 | Malpensa International Airport |  | IT | 836 |
| 28 | Ninoy Aquino International Airport |  | PH | 795 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 782 |
| 30 | Daniel K Inouye International Airport |  | US | 771 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 757 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 735 |
| 34 | Calgary International Airport |  | CA | 700 |
| 35 | Vitoria/Foronda Airport |  | ES | 699 |
| 36 | Amsterdam Airport Schiphol |  | NL | 694 |
| 37 | Don Mueang International Airport |  | TH | 691 |
| 38 | Seattle-Tacoma International Airport |  | US | 687 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 680 |
| 40 | Scottsdale Airport |  | US | 678 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 625 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 433 | 21m | 244 km | 1,823.2 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 314 | 24m | 225 km | 1,218.2 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 307 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 290 | 1h 25m | 910 km | 4,550.8 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 287 | 1h 10m | 770 km | 3,812.6 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 261 | 28m | 304 km | 1,368.2 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 236 | 26m | 275 km | 1,118.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 221 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 177 | 22m | 55 km | 168.2 t |
| 14 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 173 | 20m | 99 km | 296.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 171 | 26m | 215 km | 633.3 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 164 | 44m | 241 km | 681.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 160 | 27m | 152 km | 418.1 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 155 | 31m | 369 km | 986.6 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 154 | 44m | 452 km | 1,200.2 t |
| 21 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 22 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 150 | 1h 44m | 1,423 km | 3,681.2 t |
| 23 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 150 | 20m | 250 km | 647.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 149 | 18m | 144 km | 370.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 141 | 1h 38m | 1,156 km | 2,812.9 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 140 | 1h 1m | 695 km | 1,678.2 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 136 | 13m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 135 | 1h 17m | 961 km | 2,237.7 t |
| 29 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 133 | 54m | 136 km | 311.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ZOB | ZOB | Toowoomba Airport (YTWB) | Toowoomba Airport (YTWB) | 2026-06-24 23:16 UTC | 2026-06-24 23:58 UTC | 41m |
| N782MM |  | New Century Aircenter Airport (KIXD) | Harry Reid International Airport (KLAS) | 2026-06-24 21:21 UTC | 2026-06-24 23:57 UTC | 2h 36m |
| N9837L |  | Bland Airport (52KS) | Lawrence Regional Airport (KLWC) | 2026-06-24 23:20 UTC | 2026-06-24 23:55 UTC | 35m |
| N335BG |  | Wood County Airport (K1G0) | Wood County Airport (K1G0) | 2026-06-24 23:35 UTC | 2026-06-24 23:53 UTC | 17m |
| N520AF |  | Morristown Municipal Airport (KMMU) | Sky Manor Airport (KN40) | 2026-06-24 22:37 UTC | 2026-06-24 23:51 UTC | 1h 13m |
| N628SR |  | Palo Alto Airport (KPAO) | Truckee-Tahoe Airport (KTRK) | 2026-06-24 23:13 UTC | 2026-06-24 23:48 UTC | 34m |
| KSF39 | KSF | Kent State University Airport (K1G3) | Portage County Airport (KPOV) | 2026-06-24 23:31 UTC | 2026-06-24 23:47 UTC | 15m |
| N2553Y |  | OI34 (OI34) | OI34 (OI34) | 2026-06-24 23:26 UTC | 2026-06-24 23:46 UTC | 19m |
| N911NT |  | Ted Stevens Anchorage International Airport (PANC) | Elmendorf Afb Airport (PAED) | 2026-06-24 22:23 UTC | 2026-06-24 23:42 UTC | 1h 18m |
| N513LF |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-06-24 23:26 UTC | 2026-06-24 23:41 UTC | 14m |
| N6148W |  | North Central State Airport (KSFZ) | Southbridge Municipal Airport (K3B0) | 2026-06-24 23:18 UTC | 2026-06-24 23:40 UTC | 21m |
| N1316Z |  | Muskegon County Airport (KMKG) | II02 (II02) | 2026-06-24 22:41 UTC | 2026-06-24 23:37 UTC | 55m |
| N72NG |  | Montgomery-Gibbs Executive Airport (KMYF) | Palmdale Usaf Plant 42 Airport (KPMD) | 2026-06-24 23:06 UTC | 2026-06-24 23:35 UTC | 29m |
| N716AP |  | Houma-Terrebonne Airport (KHUM) | Hurlburt Field (KHRT) | 2026-06-24 22:41 UTC | 2026-06-24 23:32 UTC | 50m |
| ASP503 | ASP | Calgary International Airport (CYYC) | Shuswap (Skwlax Field) Airport (CSQ2) | 2026-06-24 22:46 UTC | 2026-06-24 23:26 UTC | 39m |
| SCU57 | SCU | Flying G Ranch Airport (3OK8) | Flying G Ranch Airport (3OK8) | 2026-06-24 23:23 UTC | 2026-06-24 23:24 UTC | 0m |
| N6768X |  | WN10 (WN10) | WN10 (WN10) | 2026-06-24 23:12 UTC | 2026-06-24 23:22 UTC | 10m |
| N523DV |  | Hawks Run Airport (00WN) | 30WA (30WA) | 2026-06-24 23:12 UTC | 2026-06-24 23:22 UTC | 10m |
| N516TH |  | Norman Y Mineta San Jose International Airport (KSJC) | Agape Farm Airport (OR42) | 2026-06-24 22:21 UTC | 2026-06-24 23:19 UTC | 58m |
| N300SF |  | Nantucket Memorial Airport (KACK) | 7LA3 (7LA3) | 2026-06-24 20:10 UTC | 2026-06-24 23:18 UTC | 3h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
