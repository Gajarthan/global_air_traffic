# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_04:11:57_UTC-green)

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

**Latest saved flight:** 2026-07-25 04:11:57 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 04:11:57 UTC

- **149,391** saved flights
- **49,800** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **149,391** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,787,219.6 tonnes** estimated CO2 emissions
- **103,606,932 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6015 |
| 2 | SkyWest Airlines | 5479 |
| 3 | EJA | 2966 |
| 4 | IndiGo | 2668 |
| 5 | American Airlines | 2380 |
| 6 | Southwest Airlines | 2272 |
| 7 | ENY | 1863 |
| 8 | Delta Air Lines | 1763 |
| 9 | Lufthansa | 1455 |
| 10 | LATAM Airlines | 1377 |
| 11 | AZU | 1291 |
| 12 | WIF | 1268 |
| 13 | Vueling | 1258 |
| 14 | LXJ | 1153 |
| 15 | AXM | 1076 |
| 16 | Swiss International | 1052 |
| 17 | easyJet | 965 |
| 18 | All Nippon Airways | 945 |
| 19 | Alaska Airlines | 935 |
| 20 | QLK | 930 |
| 21 | EJU | 910 |
| 22 | VIV | 824 |
| 23 | CXK | 799 |
| 24 | AEE | 781 |
| 25 | JetBlue | 781 |
| 26 | Cathay Pacific | 780 |
| 27 | Air France | 779 |
| 28 | MXY | 779 |
| 29 | GLO | 772 |
| 30 | United Airlines | 771 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 129129 |
| 2 | 🇪🇸 ES | 9618 |
| 3 | 🇦🇺 AU | 8487 |
| 4 | 🇧🇷 BR | 8427 |
| 5 | 🇮🇳 IN | 8392 |
| 6 | 🇨🇦 CA | 8020 |
| 7 | 🇮🇹 IT | 7704 |
| 8 | 🇩🇪 DE | 7616 |
| 9 | 🇬🇧 GB | 6817 |
| 10 | 🇯🇵 JP | 6192 |
| 11 | 🇫🇷 FR | 5904 |
| 12 | 🇨🇴 CO | 5038 |
| 13 | 🇲🇽 MX | 4331 |
| 14 | 🇬🇷 GR | 4214 |
| 15 | 🇳🇴 NO | 3974 |
| 16 | 🇨🇭 CH | 3899 |
| 17 | 🇹🇷 TR | 3514 |
| 18 | 🇲🇾 MY | 2798 |
| 19 | 🇵🇱 PL | 2512 |
| 20 | 🇿🇦 ZA | 2406 |
| 21 | 🇳🇿 NZ | 2259 |
| 22 | 🇹🇭 TH | 2173 |
| 23 | 🇰🇷 KR | 2059 |
| 24 | 🇵🇭 PH | 1987 |
| 25 | 🇬🇹 GT | 1949 |
| 26 | 🇲🇦 MA | 1522 |
| 27 | 🇲🇪 ME | 1471 |
| 28 | 🇳🇱 NL | 1380 |
| 29 | 🇭🇷 HR | 1353 |
| 30 | 🇲🇴 MO | 1246 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3080 |
| 2 | Denver International Airport |  | US | 2514 |
| 3 | Tokyo International Airport |  | JP | 1980 |
| 4 | Guaymaral Airport |  | CO | 1866 |
| 5 | Indira Gandhi International Airport |  | IN | 1863 |
| 6 | Harry Reid International Airport |  | US | 1857 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1669 |
| 8 | Zurich Airport |  | CH | 1631 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1573 |
| 10 | La Aurora Airport |  | GT | 1509 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1405 |
| 12 | Frankfurt am Main International Airport |  | DE | 1405 |
| 13 | Chicago O'Hare International Airport |  | US | 1383 |
| 14 | Salt Lake City International Airport |  | US | 1348 |
| 15 | El Dorado International Airport |  | CO | 1343 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1285 |
| 17 | Macau International Airport |  | MO | 1246 |
| 18 | Congonhas Airport |  | BR | 1205 |
| 19 | Capua Airport |  | IT | 1193 |
| 20 | Madrid Barajas International Airport |  | ES | 1184 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1162 |
| 22 | Kuala Lumpur International Airport |  | MY | 1079 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1072 |
| 24 | Charlotte/Douglas International Airport |  | US | 1066 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1049 |
| 26 | Charles de Gaulle International Airport |  | FR | 1029 |
| 27 | Bengaluru International Airport |  | IN | 1005 |
| 28 | Malpensa International Airport |  | IT | 964 |
| 29 | Ninoy Aquino International Airport |  | PH | 931 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 909 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 898 |
| 32 | Barcelona International Airport |  | ES | 898 |
| 33 | Daniel K Inouye International Airport |  | US | 897 |
| 34 | Seattle-Tacoma International Airport |  | US | 860 |
| 35 | Calgary International Airport |  | CA | 854 |
| 36 | Tenerife Norte Airport |  | ES | 852 |
| 37 | Scottsdale Airport |  | US | 849 |
| 38 | Viracopos International Airport |  | BR | 843 |
| 39 | Amsterdam Airport Schiphol |  | NL | 830 |
| 40 | Oslo Gardermoen Airport |  | NO | 824 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 787 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 543 | 21m | 244 km | 2,286.4 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 362 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 361 | 24m | 225 km | 1,400.5 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 347 | 1h 9m | 770 km | 4,609.6 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 270 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 266 | 27m | 275 km | 1,260.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 223 | 22m | 55 km | 212.0 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 203 | 44m | 241 km | 843.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 199 | 1h 46m | 1,423 km | 4,883.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 197 | 20m | 99 km | 337.4 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 183 | 20m | 250 km | 790.5 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 183 | 27m | 152 km | 478.2 t |
| 21 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 177 | 31m | 369 km | 1,126.6 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 176 | 1h 16m | 961 km | 2,917.3 t |
| 23 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 176 | 30m | 49 km | 148.8 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 175 | 18m | 144 km | 435.3 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 175 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 171 | 44m | 452 km | 1,332.7 t |
| 27 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 169 | 1h 1m | 695 km | 2,025.8 t |
| 28 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 168 | 1h 39m | 1,156 km | 3,351.5 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 162 | 14m | 154 km | 429.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 162 | 55m | 136 km | 379.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N515MV |  | Kenai Municipal Airport (PAEN) | Ted Stevens Anchorage International Airport (PANC) | 2026-07-25 03:49 UTC | 2026-07-25 04:11 UTC | 22m |
| N83AE |  | Strother Field (KWLD) | Cessna Acft Field (KCEA) | 2026-07-25 03:34 UTC | 2026-07-25 04:04 UTC | 29m |
| AIRLIFT | AIR | Bremerton Ntl Airport (KPWT) | Boeing Field/King County International Airport (KBFI) | 2026-07-25 03:34 UTC | 2026-07-25 03:45 UTC | 10m |
| YGZ | YGZ | Perth Jandakot Airport (YPJT) | Perth Jandakot Airport (YPJT) | 2026-07-25 02:51 UTC | 2026-07-25 03:44 UTC | 52m |
| N814SS |  | Kenai Municipal Airport (PAEN) | Beluga Airport (PABG) | 2026-07-25 03:26 UTC | 2026-07-25 03:44 UTC | 18m |
| UNIDENT | UNI | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-07-24 18:09 UTC | 2026-07-25 03:29 UTC | 9h 20m |
| DAL1713 | Delta Air Lines | Hartsfield/Jackson Atlanta International Airport (KATL) | Dell City Municipal Airport (K2E5) | 2026-07-25 01:07 UTC | 2026-07-25 03:23 UTC | 2h 16m |
| AZU4099 | AZU | Viracopos International Airport (SBKP) | Catanduva Airport (SDCD) | 2026-07-25 02:34 UTC | 2026-07-25 03:20 UTC | 45m |
| KBZ781 | KBZ | Mandalay International Airport (VYMD) | Pinlebu Airport (VYPL) | 2026-07-25 02:30 UTC | 2026-07-25 03:11 UTC | 41m |
| FD469 |  | Brisbane International Airport (YBBN) | Dalby Airport (YDAY) | 2026-07-25 02:44 UTC | 2026-07-25 03:11 UTC | 26m |
| N75844 |  | Bellingham International Airport (KBLI) | Skagit Regional Airport (KBVS) | 2026-07-25 02:34 UTC | 2026-07-25 03:08 UTC | 34m |
| OUA39 | OUA | University Of Oklahoma Westheimer Airport (KOUN) | Haskell Airport (K2K9) | 2026-07-25 02:28 UTC | 2026-07-25 03:07 UTC | 38m |
| N11PP |  | Ronald Reagan Washington Ntl Airport (KDCA) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-07-25 02:38 UTC | 2026-07-25 03:04 UTC | 26m |
| SIA148 | Singapore Airlines | Singapore Changi International Airport (WSSS) | Anduki Airport (WBAK) | 2026-07-25 01:30 UTC | 2026-07-25 03:03 UTC | 1h 33m |
| SKW4264 | SkyWest Airlines | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Preszler Airstrip (1NA8) | 2026-07-25 01:20 UTC | 2026-07-25 03:03 UTC | 1h 42m |
| AXM391 | AXM | Kuala Lumpur International Airport (WMKK) | Silangit Airport (WIMN) | 2026-07-25 02:39 UTC | 2026-07-25 03:02 UTC | 22m |
| VOI3316 | VOI | General Abelardo L. Rodriguez International Airport (MMTJ) | General Jose Maria Yanez International Airport (MMGM) | 2026-07-25 01:57 UTC | 2026-07-25 03:02 UTC | 1h 4m |
| NOK572 | NOK | Don Mueang International Airport (VTBD) | Chumphon Airport (VTSE) | 2026-07-25 02:30 UTC | 2026-07-25 03:01 UTC | 31m |
| CEB897 | CEB | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-07-25 02:35 UTC | 2026-07-25 03:00 UTC | 24m |
| AZU4670 | AZU | Viracopos International Airport (SBKP) | Fazenda Treis Coringas Airport (SNUF) | 2026-07-25 02:02 UTC | 2026-07-25 03:00 UTC | 57m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
