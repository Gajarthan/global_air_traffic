# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_15:15:39_UTC-green)

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

**Latest saved flight:** 2026-07-03 15:15:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 15:15:39 UTC

- **127,303** saved flights
- **43,436** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **127,303** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,536,093.5 tonnes** estimated CO2 emissions
- **89,048,896 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5160 |
| 2 | SkyWest Airlines | 4695 |
| 3 | EJA | 2501 |
| 4 | IndiGo | 2407 |
| 5 | American Airlines | 1952 |
| 6 | Southwest Airlines | 1908 |
| 7 | ENY | 1594 |
| 8 | Delta Air Lines | 1514 |
| 9 | Lufthansa | 1353 |
| 10 | LATAM Airlines | 1158 |
| 11 | Vueling | 1126 |
| 12 | WIF | 1121 |
| 13 | AZU | 1075 |
| 14 | AXM | 1002 |
| 15 | LXJ | 991 |
| 16 | Swiss International | 883 |
| 17 | All Nippon Airways | 853 |
| 18 | Alaska Airlines | 825 |
| 19 | easyJet | 813 |
| 20 | QLK | 803 |
| 21 | EJU | 788 |
| 22 | Cathay Pacific | 706 |
| 23 | VIV | 699 |
| 24 | AEE | 696 |
| 25 | Air France | 694 |
| 26 | CXK | 684 |
| 27 | United Airlines | 675 |
| 28 | MXY | 662 |
| 29 | JetBlue | 653 |
| 30 | GLO | 642 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 108851 |
| 2 | 🇪🇸 ES | 8475 |
| 3 | 🇮🇳 IN | 7548 |
| 4 | 🇦🇺 AU | 7447 |
| 5 | 🇧🇷 BR | 7117 |
| 6 | 🇩🇪 DE | 6710 |
| 7 | 🇨🇦 CA | 6697 |
| 8 | 🇮🇹 IT | 6677 |
| 9 | 🇬🇧 GB | 5622 |
| 10 | 🇯🇵 JP | 5565 |
| 11 | 🇫🇷 FR | 5036 |
| 12 | 🇨🇴 CO | 4054 |
| 13 | 🇲🇽 MX | 3698 |
| 14 | 🇬🇷 GR | 3614 |
| 15 | 🇳🇴 NO | 3477 |
| 16 | 🇨🇭 CH | 3239 |
| 17 | 🇹🇷 TR | 2705 |
| 18 | 🇲🇾 MY | 2597 |
| 19 | 🇿🇦 ZA | 2108 |
| 20 | 🇵🇱 PL | 2080 |
| 21 | 🇳🇿 NZ | 2057 |
| 22 | 🇹🇭 TH | 1989 |
| 23 | 🇰🇷 KR | 1958 |
| 24 | 🇵🇭 PH | 1804 |
| 25 | 🇬🇹 GT | 1747 |
| 26 | 🇲🇦 MA | 1364 |
| 27 | 🇲🇪 ME | 1258 |
| 28 | 🇳🇱 NL | 1199 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1100 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2655 |
| 2 | Denver International Airport |  | US | 2142 |
| 3 | Tokyo International Airport |  | JP | 1835 |
| 4 | Indira Gandhi International Airport |  | IN | 1660 |
| 5 | Harry Reid International Airport |  | US | 1590 |
| 6 | Guaymaral Airport |  | CO | 1541 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1510 |
| 8 | Zurich Airport |  | CH | 1398 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1352 |
| 10 | La Aurora Airport |  | GT | 1351 |
| 11 | Frankfurt am Main International Airport |  | DE | 1308 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1244 |
| 13 | Chicago O'Hare International Airport |  | US | 1228 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1122 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1054 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1049 |
| 20 | Madrid Barajas International Airport |  | ES | 1044 |
| 21 | Kuala Lumpur International Airport |  | MY | 1010 |
| 22 | Congonhas Airport |  | BR | 998 |
| 23 | Charlotte/Douglas International Airport |  | US | 952 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 935 |
| 25 | Charles de Gaulle International Airport |  | FR | 925 |
| 26 | Bengaluru International Airport |  | IN | 914 |
| 27 | Malpensa International Airport |  | IT | 870 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 854 |
| 29 | Ninoy Aquino International Airport |  | PH | 836 |
| 30 | Daniel K Inouye International Airport |  | US | 807 |
| 31 | Barcelona International Airport |  | ES | 792 |
| 32 | Tenerife Norte Airport |  | ES | 776 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 772 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 745 |
| 35 | Calgary International Airport |  | CA | 742 |
| 36 | Scottsdale Airport |  | US | 738 |
| 37 | Seattle-Tacoma International Airport |  | US | 734 |
| 38 | Vitoria/Foronda Airport |  | ES | 730 |
| 39 | Viracopos International Airport |  | BR | 726 |
| 40 | Amsterdam Airport Schiphol |  | NL | 723 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 643 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 462 | 21m | 244 km | 1,945.4 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 320 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 309 | 1h 10m | 770 km | 4,104.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 243 | 26m | 275 km | 1,151.5 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 187 | 22m | 55 km | 177.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 180 | 26m | 215 km | 666.6 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 16 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 177 | 44m | 241 km | 735.2 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 164 | 1h 45m | 1,423 km | 4,024.8 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 22 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 154 | 20m | 250 km | 665.2 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 152 | 30m | 49 km | 128.5 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 148 | 1h 1m | 695 km | 1,774.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 147 | 1h 17m | 961 km | 2,436.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 144 | 54m | 136 km | 337.6 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OUA3 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Hickory Hills Airport (10OK) | 2026-07-03 14:48 UTC | 2026-07-03 15:15 UTC | 27m |
| FFT1542 | FFT | Orlando International Airport (KMCO) | Philadelphia International Airport (KPHL) | 2026-07-03 13:16 UTC | 2026-07-03 15:09 UTC | 1h 52m |
| N26BQ |  | Dupage Airport (KDPA) | Ruder Airport (59IL) | 2026-07-03 14:01 UTC | 2026-07-03 15:08 UTC | 1h 6m |
| N416SC |  | Skypark Airport (KBTF) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-03 14:25 UTC | 2026-07-03 15:08 UTC | 43m |
| N8394C |  | Three Rivers Municipal/Dr Haines Airport (KHAI) | Three Rivers Municipal/Dr Haines Airport (KHAI) | 2026-07-03 14:21 UTC | 2026-07-03 14:57 UTC | 35m |
| N7683H |  | Bend Municipal Airport (KBDN) | Bend Municipal Airport (KBDN) | 2026-07-03 14:45 UTC | 2026-07-03 14:56 UTC | 11m |
| N750SS |  | Pepperell Airport (26MA) | Pepperell Airport (26MA) | 2026-07-03 14:33 UTC | 2026-07-03 14:56 UTC | 23m |
| N372MM |  | Skypark Airport (KBTF) | True Grit South Airport (CO95) | 2026-07-03 14:05 UTC | 2026-07-03 14:55 UTC | 50m |
| HORUS30 | HOR | Nimes-Arles-Camargue Airport (LFTW) | Avignon-Caumont Airport (LFMV) | 2026-07-03 13:40 UTC | 2026-07-03 14:54 UTC | 1h 14m |
| ERU55 | ERU | Yav'Pe Ma'Ta Airport (16AZ) | Yav'Pe Ma'Ta Airport (16AZ) | 2026-07-03 14:29 UTC | 2026-07-03 14:54 UTC | 25m |
| SD1 |  | 52TA (52TA) | Tri-County Aerodrome (48TX) | 2026-07-03 14:14 UTC | 2026-07-03 14:53 UTC | 39m |
| CGMPA | CGM | Prince Albert (Glass Field) Airport (CYPA) | Saskatoon John G. Diefenbaker International Airport (CYXE) | 2026-07-03 14:28 UTC | 2026-07-03 14:52 UTC | 24m |
| ASI968 | ASI | Phoenix Deer Valley Airport (KDVT) | Phoenix Deer Valley Airport (KDVT) | 2026-07-03 14:21 UTC | 2026-07-03 14:47 UTC | 26m |
| XBPBH | XBP | Hermanos Serdan International Airport (MMPB) | Tehuacan Airport (MMHC) | 2026-07-03 14:16 UTC | 2026-07-03 14:47 UTC | 30m |
| NJE745D | NJE | Verona / Villafranca Airport (LIPX) | Lyon-Bron Airport (LFLY) | 2026-07-03 13:59 UTC | 2026-07-03 14:46 UTC | 47m |
| N150MT |  | Mc Clellan-Palomar Airport (KCRQ) | Sedona Airport (KSEZ) | 2026-07-03 14:04 UTC | 2026-07-03 14:46 UTC | 41m |
| N137MH |  | Woodbine Municipal Airport (KOBI) | Philadelphia International Airport (KPHL) | 2026-07-03 14:13 UTC | 2026-07-03 14:45 UTC | 32m |
| N4802N |  | Bend Municipal Airport (KBDN) | Madras Municipal Airport (KS33) | 2026-07-03 14:01 UTC | 2026-07-03 14:45 UTC | 43m |
| N16NW |  | Albuquerque International Sunport Airport (KABQ) | Flying H Ranch Airport (68NM) | 2026-07-03 13:56 UTC | 2026-07-03 14:45 UTC | 48m |
| N62801 |  | Mount Sterling/Montgomery County Airport (KIOB) | Russell County Airport (KK24) | 2026-07-03 11:35 UTC | 2026-07-03 14:43 UTC | 3h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
