# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_04:14:04_UTC-green)

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

**Latest saved flight:** 2026-06-25 04:14:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-25 04:14:04 UTC

- **119,682** saved flights
- **41,202** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **119,682** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,447,883.0 tonnes** estimated CO2 emissions
- **83,935,244 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4919 |
| 2 | SkyWest Airlines | 4418 |
| 3 | EJA | 2313 |
| 4 | IndiGo | 2303 |
| 5 | American Airlines | 1861 |
| 6 | Southwest Airlines | 1784 |
| 7 | ENY | 1493 |
| 8 | Delta Air Lines | 1417 |
| 9 | Lufthansa | 1312 |
| 10 | Vueling | 1077 |
| 11 | LATAM Airlines | 1060 |
| 12 | WIF | 1060 |
| 13 | AZU | 997 |
| 14 | AXM | 977 |
| 15 | LXJ | 909 |
| 16 | Swiss International | 839 |
| 17 | All Nippon Airways | 819 |
| 18 | Alaska Airlines | 792 |
| 19 | easyJet | 769 |
| 20 | QLK | 768 |
| 21 | EJU | 749 |
| 22 | Cathay Pacific | 674 |
| 23 | AEE | 666 |
| 24 | United Airlines | 656 |
| 25 | VIV | 656 |
| 26 | Air France | 652 |
| 27 | CXK | 639 |
| 28 | MXY | 630 |
| 29 | AXB | 595 |
| 30 | JetBlue | 591 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 101385 |
| 2 | 🇪🇸 ES | 8137 |
| 3 | 🇮🇳 IN | 7237 |
| 4 | 🇦🇺 AU | 7062 |
| 5 | 🇧🇷 BR | 6590 |
| 6 | 🇩🇪 DE | 6384 |
| 7 | 🇮🇹 IT | 6379 |
| 8 | 🇨🇦 CA | 6297 |
| 9 | 🇯🇵 JP | 5334 |
| 10 | 🇬🇧 GB | 5251 |
| 11 | 🇫🇷 FR | 4754 |
| 12 | 🇨🇴 CO | 4012 |
| 13 | 🇲🇽 MX | 3495 |
| 14 | 🇬🇷 GR | 3412 |
| 15 | 🇳🇴 NO | 3290 |
| 16 | 🇨🇭 CH | 3074 |
| 17 | 🇲🇾 MY | 2537 |
| 18 | 🇹🇷 TR | 2456 |
| 19 | 🇿🇦 ZA | 2013 |
| 20 | 🇵🇱 PL | 1965 |
| 21 | 🇳🇿 NZ | 1942 |
| 22 | 🇹🇭 TH | 1912 |
| 23 | 🇰🇷 KR | 1904 |
| 24 | 🇵🇭 PH | 1721 |
| 25 | 🇬🇹 GT | 1675 |
| 26 | 🇲🇦 MA | 1291 |
| 27 | 🇲🇪 ME | 1190 |
| 28 | 🇲🇴 MO | 1173 |
| 29 | 🇳🇱 NL | 1148 |
| 30 | 🇭🇷 HR | 1035 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2517 |
| 2 | Denver International Airport |  | US | 2009 |
| 3 | Tokyo International Airport |  | JP | 1767 |
| 4 | Indira Gandhi International Airport |  | IN | 1590 |
| 5 | Guaymaral Airport |  | CO | 1502 |
| 6 | Harry Reid International Airport |  | US | 1489 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1451 |
| 8 | Zurich Airport |  | CH | 1332 |
| 9 | La Aurora Airport |  | GT | 1293 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1272 |
| 11 | Frankfurt am Main International Airport |  | DE | 1267 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1184 |
| 13 | Macau International Airport |  | MO | 1173 |
| 14 | El Dorado International Airport |  | CO | 1171 |
| 15 | Chicago O'Hare International Airport |  | US | 1170 |
| 16 | Salt Lake City International Airport |  | US | 1030 |
| 17 | Capua Airport |  | IT | 1028 |
| 18 | Madrid Barajas International Airport |  | ES | 1008 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 999 |
| 20 | Kuala Lumpur International Airport |  | MY | 981 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 925 |
| 22 | Congonhas Airport |  | BR | 921 |
| 23 | Charlotte/Douglas International Airport |  | US | 908 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 890 |
| 25 | Charles de Gaulle International Airport |  | FR | 874 |
| 26 | Bengaluru International Airport |  | IN | 874 |
| 27 | Malpensa International Airport |  | IT | 836 |
| 28 | Ninoy Aquino International Airport |  | PH | 797 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 782 |
| 30 | Daniel K Inouye International Airport |  | US | 772 |
| 31 | Tenerife Norte Airport |  | ES | 762 |
| 32 | Barcelona International Airport |  | ES | 757 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 735 |
| 34 | Calgary International Airport |  | CA | 700 |
| 35 | Vitoria/Foronda Airport |  | ES | 699 |
| 36 | Amsterdam Airport Schiphol |  | NL | 694 |
| 37 | Don Mueang International Airport |  | TH | 693 |
| 38 | Seattle-Tacoma International Airport |  | US | 688 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 680 |
| 40 | Scottsdale Airport |  | US | 679 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 625 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 434 | 21m | 244 km | 1,827.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 315 | 24m | 225 km | 1,222.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 307 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 291 | 1h 25m | 910 km | 4,566.5 t |
| 6 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 288 | 1h 10m | 770 km | 3,825.9 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
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
| LS09 |  | Imperial Beach Nolf (Ream Field) Airport (KNRS) | North Island Nas (Halsey Field) Airport (KNZY) | 2026-06-25 03:38 UTC | 2026-06-25 04:14 UTC | 35m |
| N733LN |  | Fort Lauderdale Executive Airport (KFXE) | Witham Field (KSUA) | 2026-06-25 02:33 UTC | 2026-06-25 04:10 UTC | 1h 37m |
| JBU1854 | JetBlue | Ronald Reagan Washington Ntl Airport (KDCA) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-25 03:06 UTC | 2026-06-25 04:06 UTC | 59m |
| J826KT |  | Adi Sutjipto International Airport (WARJ) | Gading Wonosari Airport (WI1G) | 2026-06-25 03:44 UTC | 2026-06-25 04:03 UTC | 18m |
| WOLF01 | WOL | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-06-25 03:49 UTC | 2026-06-25 04:01 UTC | 11m |
| N401NG |  | Samsarg Field (KN58) | Fry Canyon Field (UT74) | 2026-06-25 02:16 UTC | 2026-06-25 04:00 UTC | 1h 44m |
| UCI | UCI | Perth Jandakot Airport (YPJT) | Merredin Airport (YMDN) | 2026-06-25 02:40 UTC | 2026-06-25 04:00 UTC | 1h 19m |
| VAR789 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-06-25 03:43 UTC | 2026-06-25 03:58 UTC | 14m |
| STALK51 | STA | Albuquerque International Sunport Airport (KABQ) | NM74 (NM74) | 2026-06-25 03:01 UTC | 2026-06-25 03:56 UTC | 54m |
| ANZ607 | ANZ | Wellington International Airport (NZWN) | Wanaka Airport (NZWF) | 2026-06-25 02:35 UTC | 2026-06-25 03:54 UTC | 1h 18m |
| N782MM |  | Harry Reid International Airport (KLAS) | Harry Reid International Airport (KLAS) | 2026-06-25 03:38 UTC | 2026-06-25 03:50 UTC | 11m |
| N504MP |  | Dallas Executive Airport (KRBD) | Austin Executive Airport (KEDC) | 2026-06-25 03:09 UTC | 2026-06-25 03:48 UTC | 39m |
| VAR485 | VAR | Phoenix Goodyear Airport (KGYR) | Glendale Regional Airport (KGEU) | 2026-06-25 03:34 UTC | 2026-06-25 03:45 UTC | 11m |
| VAR494 | VAR | Phoenix Goodyear Airport (KGYR) | Buckeye Municipal Airport (KBXK) | 2026-06-25 03:25 UTC | 2026-06-25 03:41 UTC | 16m |
| SCA42 | SCA | Scottsdale Airport (KSDL) | Marana Regional Airport (KAVQ) | 2026-06-25 02:33 UTC | 2026-06-25 03:36 UTC | 1h 3m |
| WOLF01 | WOL | Elmendorf Afb Airport (PAED) | Elmendorf Afb Airport (PAED) | 2026-06-25 01:57 UTC | 2026-06-25 03:35 UTC | 1h 37m |
| NOGS34 | NOG | 1OK5 (1OK5) | TX01 (TX01) | 2026-06-25 01:50 UTC | 2026-06-25 03:31 UTC | 1h 41m |
| ANZ311L | ANZ | Wellington International Airport (NZWN) | Woodbourne Airport (NZWB) | 2026-06-25 03:09 UTC | 2026-06-25 03:25 UTC | 16m |
| QLK22D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-06-25 02:46 UTC | 2026-06-25 03:25 UTC | 38m |
| RYR11EX | Ryanair | Eleftherios Venizelos International Airport (LGAV) | Kasteli Airport (LGTL) | 2026-06-25 03:05 UTC | 2026-06-25 03:24 UTC | 19m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
