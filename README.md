# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_19:39:38_UTC-green)

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

**Latest saved flight:** 2026-07-03 19:39:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-03 19:39:38 UTC

- **128,010** saved flights
- **43,660** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **128,010** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,543,898.8 tonnes** estimated CO2 emissions
- **89,501,377 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5191 |
| 2 | SkyWest Airlines | 4736 |
| 3 | EJA | 2515 |
| 4 | IndiGo | 2413 |
| 5 | American Airlines | 1969 |
| 6 | Southwest Airlines | 1923 |
| 7 | ENY | 1607 |
| 8 | Delta Air Lines | 1527 |
| 9 | Lufthansa | 1354 |
| 10 | LATAM Airlines | 1165 |
| 11 | Vueling | 1131 |
| 12 | WIF | 1126 |
| 13 | AZU | 1083 |
| 14 | AXM | 1002 |
| 15 | LXJ | 996 |
| 16 | Swiss International | 887 |
| 17 | All Nippon Airways | 853 |
| 18 | Alaska Airlines | 828 |
| 19 | easyJet | 815 |
| 20 | QLK | 803 |
| 21 | EJU | 793 |
| 22 | Cathay Pacific | 708 |
| 23 | VIV | 702 |
| 24 | AEE | 700 |
| 25 | Air France | 698 |
| 26 | CXK | 690 |
| 27 | United Airlines | 679 |
| 28 | MXY | 666 |
| 29 | JetBlue | 655 |
| 30 | GLO | 646 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 109592 |
| 2 | 🇪🇸 ES | 8516 |
| 3 | 🇮🇳 IN | 7560 |
| 4 | 🇦🇺 AU | 7449 |
| 5 | 🇧🇷 BR | 7164 |
| 6 | 🇩🇪 DE | 6742 |
| 7 | 🇨🇦 CA | 6740 |
| 8 | 🇮🇹 IT | 6711 |
| 9 | 🇬🇧 GB | 5657 |
| 10 | 🇯🇵 JP | 5567 |
| 11 | 🇫🇷 FR | 5070 |
| 12 | 🇨🇴 CO | 4066 |
| 13 | 🇲🇽 MX | 3726 |
| 14 | 🇬🇷 GR | 3639 |
| 15 | 🇳🇴 NO | 3497 |
| 16 | 🇨🇭 CH | 3253 |
| 17 | 🇹🇷 TR | 2739 |
| 18 | 🇲🇾 MY | 2597 |
| 19 | 🇿🇦 ZA | 2126 |
| 20 | 🇵🇱 PL | 2091 |
| 21 | 🇳🇿 NZ | 2059 |
| 22 | 🇹🇭 TH | 1990 |
| 23 | 🇰🇷 KR | 1958 |
| 24 | 🇵🇭 PH | 1804 |
| 25 | 🇬🇹 GT | 1751 |
| 26 | 🇲🇦 MA | 1373 |
| 27 | 🇲🇪 ME | 1264 |
| 28 | 🇳🇱 NL | 1205 |
| 29 | 🇲🇴 MO | 1184 |
| 30 | 🇧🇸 BS | 1104 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2672 |
| 2 | Denver International Airport |  | US | 2163 |
| 3 | Tokyo International Airport |  | JP | 1835 |
| 4 | Indira Gandhi International Airport |  | IN | 1664 |
| 5 | Harry Reid International Airport |  | US | 1598 |
| 6 | Guaymaral Airport |  | CO | 1553 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1517 |
| 8 | Zurich Airport |  | CH | 1405 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1363 |
| 10 | La Aurora Airport |  | GT | 1355 |
| 11 | Frankfurt am Main International Airport |  | DE | 1312 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1249 |
| 13 | Chicago O'Hare International Airport |  | US | 1235 |
| 14 | Macau International Airport |  | MO | 1184 |
| 15 | El Dorado International Airport |  | CO | 1172 |
| 16 | Salt Lake City International Airport |  | US | 1136 |
| 17 | Capua Airport |  | IT | 1067 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 1057 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1056 |
| 20 | Madrid Barajas International Airport |  | ES | 1046 |
| 21 | Kuala Lumpur International Airport |  | MY | 1010 |
| 22 | Congonhas Airport |  | BR | 1006 |
| 23 | Charlotte/Douglas International Airport |  | US | 963 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 935 |
| 25 | Charles de Gaulle International Airport |  | FR | 931 |
| 26 | Bengaluru International Airport |  | IN | 916 |
| 27 | Malpensa International Airport |  | IT | 872 |
| 28 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 860 |
| 29 | Ninoy Aquino International Airport |  | PH | 836 |
| 30 | Daniel K Inouye International Airport |  | US | 811 |
| 31 | Barcelona International Airport |  | ES | 796 |
| 32 | Tenerife Norte Airport |  | ES | 780 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 779 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 752 |
| 35 | Calgary International Airport |  | CA | 749 |
| 36 | Scottsdale Airport |  | US | 741 |
| 37 | Seattle-Tacoma International Airport |  | US | 739 |
| 38 | Vitoria/Foronda Airport |  | ES | 738 |
| 39 | Viracopos International Airport |  | BR | 730 |
| 40 | Amsterdam Airport Schiphol |  | NL | 726 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 649 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 465 | 21m | 244 km | 1,958.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 328 | 24m | 225 km | 1,272.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 322 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 309 | 1h 10m | 770 km | 4,104.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 244 | 26m | 275 km | 1,156.2 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 236 | 31m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 188 | 22m | 55 km | 178.7 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 181 | 26m | 215 km | 670.3 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 178 | 44m | 241 km | 739.4 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 177 | 13m | - | - |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 177 | 20m | 99 km | 303.2 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 172 | 27m | 152 km | 449.5 t |
| 19 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 166 | 1h 45m | 1,423 km | 4,073.9 t |
| 20 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 162 | 31m | 369 km | 1,031.2 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 157 | 20m | 250 km | 678.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 157 | 18m | 144 km | 390.5 t |
| 23 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 156 | 44m | 452 km | 1,215.8 t |
| 24 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 154 | 30m | 49 km | 130.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 150 | 1h 1m | 695 km | 1,798.1 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 148 | 1h 17m | 961 km | 2,453.2 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 147 | 1h 38m | 1,156 km | 2,932.6 t |
| 29 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 146 | 54m | 136 km | 342.3 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 141 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASI89 | ASI | Chandler Municipal Airport (KCHD) | Gila Bend Municipal Airport (KE63) | 2026-07-03 17:56 UTC | 2026-07-03 19:39 UTC | 1h 43m |
| AA1TB |  | Grand Junction Regional Airport (KGJT) | Blanding Municipal Airport (KBDG) | 2026-07-03 17:57 UTC | 2026-07-03 19:38 UTC | 1h 41m |
| N1450U |  | City Of Colorado Springs Municipal Airport (KCOS) | La Junta Municipal Airport (KLHX) | 2026-07-03 18:44 UTC | 2026-07-03 19:34 UTC | 50m |
| AAL470 | American Airlines | Philadelphia International Airport (KPHL) | Philadelphia International Airport (KPHL) | 2026-07-03 19:21 UTC | 2026-07-03 19:32 UTC | 11m |
| N555Q |  | Palo Alto Airport (KPAO) | Livermore Municipal Airport (KLVK) | 2026-07-03 18:59 UTC | 2026-07-03 19:32 UTC | 33m |
| N477XP |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-07-03 16:54 UTC | 2026-07-03 19:23 UTC | 2h 29m |
| MSR521 | EgyptAir | Ostend-Bruges International Airport (EBOS) | HE12 (HE12) | 2026-07-03 15:43 UTC | 2026-07-03 19:22 UTC | 3h 39m |
| N734HX |  | Witherspoons Landing Strip (ME41) | Witherspoons Landing Strip (ME41) | 2026-07-03 19:03 UTC | 2026-07-03 19:21 UTC | 18m |
| N543PD |  | Hayward Executive Airport (KHWD) | Truckee-Tahoe Airport (KTRK) | 2026-07-03 18:45 UTC | 2026-07-03 19:19 UTC | 34m |
| N24VF |  | Double A Airport (XA75) | Granbury Regional Airport (KGDJ) | 2026-07-03 17:59 UTC | 2026-07-03 19:18 UTC | 1h 18m |
| N88765 |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-03 18:42 UTC | 2026-07-03 19:15 UTC | 32m |
| MGO103 | MGO | Barcelona International Airport (LEBL) | Ibiza Airport (LEIB) | 2026-07-03 18:37 UTC | 2026-07-03 19:12 UTC | 34m |
| N552TJ |  | 0PA7 (0PA7) | Northeast Philadelphia Airport (KPNE) | 2026-07-03 18:36 UTC | 2026-07-03 19:10 UTC | 34m |
| N4365R |  | Salt Lake City International Airport (KSLC) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-03 18:23 UTC | 2026-07-03 19:09 UTC | 46m |
| N436SP |  | Roberts Field (KRDM) | Prineville Airport (KS39) | 2026-07-03 18:36 UTC | 2026-07-03 19:07 UTC | 30m |
| VPCVI | VPC | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-07-03 18:44 UTC | 2026-07-03 19:05 UTC | 20m |
| N403TD |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-07-03 15:26 UTC | 2026-07-03 19:04 UTC | 3h 37m |
| N716AT |  | Noatak Airport (PAWN) | Kivalina Airport (PAVL) | 2026-07-03 18:52 UTC | 2026-07-03 19:02 UTC | 10m |
| N739UK |  | Boise Air Trml/Gowen Field (KBOI) | High Valley Airport (ID35) | 2026-07-03 18:33 UTC | 2026-07-03 19:00 UTC | 27m |
| N865A |  | Sunriver Airport (KS21) | Sunriver Airport (KS21) | 2026-07-03 18:52 UTC | 2026-07-03 18:59 UTC | 7m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
