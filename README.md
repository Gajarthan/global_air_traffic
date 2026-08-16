# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_21:11:10_UTC-green)

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

**Latest saved flight:** 2026-08-16 21:11:10 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 21:11:10 UTC

- **206,254** saved flights
- **65,782** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **206,254** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,480,902.6 tonnes** estimated CO2 emissions
- **143,820,438 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8137 |
| 2 | SkyWest Airlines | 7417 |
| 3 | EJA | 4008 |
| 4 | IndiGo | 3522 |
| 5 | American Airlines | 3439 |
| 6 | Southwest Airlines | 3318 |
| 7 | Delta Air Lines | 2652 |
| 8 | ENY | 2574 |
| 9 | LATAM Airlines | 1936 |
| 10 | AZU | 1867 |
| 11 | Lufthansa | 1749 |
| 12 | Vueling | 1708 |
| 13 | WIF | 1657 |
| 14 | LXJ | 1629 |
| 15 | easyJet | 1428 |
| 16 | Swiss International | 1376 |
| 17 | AXM | 1339 |
| 18 | United Airlines | 1302 |
| 19 | Alaska Airlines | 1278 |
| 20 | QLK | 1261 |
| 21 | EJU | 1260 |
| 22 | All Nippon Airways | 1245 |
| 23 | VIV | 1132 |
| 24 | GLO | 1114 |
| 25 | Air France | 1103 |
| 26 | PGT | 1101 |
| 27 | JetBlue | 1057 |
| 28 | AEE | 1052 |
| 29 | WMT | 1039 |
| 30 | CXK | 1016 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 175303 |
| 2 | 🇪🇸 ES | 13181 |
| 3 | 🇧🇷 BR | 11818 |
| 4 | 🇦🇺 AU | 11483 |
| 5 | 🇨🇦 CA | 11389 |
| 6 | 🇮🇳 IN | 10991 |
| 7 | 🇮🇹 IT | 10752 |
| 8 | 🇩🇪 DE | 10208 |
| 9 | 🇬🇧 GB | 9622 |
| 10 | 🇯🇵 JP | 8453 |
| 11 | 🇨🇴 CO | 8203 |
| 12 | 🇫🇷 FR | 8166 |
| 13 | 🇬🇷 GR | 6068 |
| 14 | 🇹🇷 TR | 5851 |
| 15 | 🇲🇽 MX | 5798 |
| 16 | 🇨🇭 CH | 5512 |
| 17 | 🇳🇴 NO | 5134 |
| 18 | 🇲🇾 MY | 3529 |
| 19 | 🇿🇦 ZA | 3454 |
| 20 | 🇵🇱 PL | 3403 |
| 21 | 🇹🇭 TH | 3247 |
| 22 | 🇳🇿 NZ | 2843 |
| 23 | 🇵🇭 PH | 2729 |
| 24 | 🇬🇹 GT | 2628 |
| 25 | 🇰🇷 KR | 2505 |
| 26 | 🇭🇷 HR | 2208 |
| 27 | 🇲🇦 MA | 2080 |
| 28 | 🇳🇱 NL | 1839 |
| 29 | 🇲🇪 ME | 1738 |
| 30 | 🇮🇩 ID | 1686 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4340 |
| 2 | Denver International Airport |  | US | 3374 |
| 3 | Tokyo International Airport |  | JP | 2550 |
| 4 | Guaymaral Airport |  | CO | 2494 |
| 5 | Indira Gandhi International Airport |  | IN | 2494 |
| 6 | Harry Reid International Airport |  | US | 2328 |
| 7 | Zurich Airport |  | CH | 2153 |
| 8 | Eleftherios Venizelos International Airport |  | GR | 2151 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2143 |
| 10 | La Aurora Airport |  | GT | 2003 |
| 11 | Chicago O'Hare International Airport |  | US | 1912 |
| 12 | El Dorado International Airport |  | CO | 1885 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1842 |
| 14 | Salt Lake City International Airport |  | US | 1826 |
| 15 | Congonhas Airport |  | BR | 1723 |
| 16 | Frankfurt am Main International Airport |  | DE | 1706 |
| 17 | Madrid Barajas International Airport |  | ES | 1618 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1573 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1569 |
| 20 | Capua Airport |  | IT | 1567 |
| 21 | Macau International Airport |  | MO | 1542 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1492 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1436 |
| 24 | Malpensa International Airport |  | IT | 1420 |
| 25 | Charles de Gaulle International Airport |  | FR | 1413 |
| 26 | Charlotte/Douglas International Airport |  | US | 1408 |
| 27 | Kuala Lumpur International Airport |  | MY | 1309 |
| 28 | Ninoy Aquino International Airport |  | PH | 1293 |
| 29 | Bengaluru International Airport |  | IN | 1276 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1275 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1245 |
| 32 | Barcelona International Airport |  | ES | 1228 |
| 33 | Seattle-Tacoma International Airport |  | US | 1221 |
| 34 | Viracopos International Airport |  | BR | 1196 |
| 35 | Calgary International Airport |  | CA | 1167 |
| 36 | Reno/Tahoe International Airport |  | US | 1141 |
| 37 | Oslo Gardermoen Airport |  | NO | 1139 |
| 38 | Vitoria/Foronda Airport |  | ES | 1136 |
| 39 | Amsterdam Airport Schiphol |  | NL | 1107 |
| 40 | Tenerife Norte Airport |  | ES | 1104 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1026 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 500 | 1h 7m | 770 km | 6,642.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 478 | 24m | 225 km | 1,854.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 470 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 398 | 8m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 345 | 27m | 275 km | 1,634.8 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 309 | 1h 7m | 706 km | 3,762.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 303 | 44m | 241 km | 1,258.6 t |
| 12 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 297 | 1h 49m | 1,423 km | 7,288.8 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 268 | 21m | 250 km | 1,157.6 t |
| 16 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 257 | 24m | 218 km | 968.2 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 252 | 19m | 99 km | 431.7 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 250 | 27m | 215 km | 925.9 t |
| 20 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 247 | 1h 14m | 961 km | 4,094.2 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 245 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 244 | 1h 37m | 1,156 km | 4,867.7 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 237 | 19m | 144 km | 589.5 t |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 233 | 31m | 369 km | 1,483.1 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 224 | 28m | 152 km | 585.4 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 222 | 1h 49m | 1,304 km | 4,994.4 t |
| 30 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| MNL14 | MNL | Truckee-Tahoe Airport (KTRK) | Buchanan Field (KCCR) | 2026-08-16 20:41 UTC | 2026-08-16 21:11 UTC | 30m |
| N234WL |  | Talmage Field (03NY) | Laguardia Airport (KLGA) | 2026-08-16 20:41 UTC | 2026-08-16 21:10 UTC | 29m |
| QTR18M | Qatar Airways | Malaga Airport (LEMG) | Al Udeid Air Base (OTBH) | 2026-08-16 14:39 UTC | 2026-08-16 21:00 UTC | 6h 20m |
| QTR69T | Qatar Airways | Dublin Airport (EIDW) | Al Udeid Air Base (OTBH) | 2026-08-16 14:23 UTC | 2026-08-16 20:58 UTC | 6h 35m |
| AAL37 | American Airlines | Madrid Barajas International Airport (LEMD) | Dallas-Fort Worth International Airport (KDFW) | 2026-08-16 11:08 UTC | 2026-08-16 20:58 UTC | 9h 49m |
| ES801 |  | Sacramento Mather Airport (KMHR) | Sacramento Mather Airport (KMHR) | 2026-08-16 20:36 UTC | 2026-08-16 20:57 UTC | 20m |
| WIF1H | WIF | Bodø Airport (ENBO) | Mo i Rana Airport Rossvoll (ENRA) | 2026-08-16 20:45 UTC | 2026-08-16 20:56 UTC | 11m |
| N314EV |  | Minden-Tahoe Airport (KMEV) | Desert Creek Airport (NV97) | 2026-08-16 19:34 UTC | 2026-08-16 20:54 UTC | 1h 20m |
| UAE192 | Emirates | Lisbon Portela Airport (LPPT) | Dubai International Airport (OMDB) | 2026-08-16 13:48 UTC | 2026-08-16 20:51 UTC | 7h 2m |
| N901ST |  | 75IS (75IS) | Staton Airport (4LL1) | 2026-08-16 20:35 UTC | 2026-08-16 20:48 UTC | 13m |
| AFR52VY | Air France | Charles de Gaulle International Airport (LFPG) | Vilar Da Luz Airport (LPVL) | 2026-08-16 18:53 UTC | 2026-08-16 20:44 UTC | 1h 50m |
| TAP76EN | TAP Air Portugal | Oslo Gardermoen Airport (ENGM) | Sintra Airport (LPST) | 2026-08-16 17:03 UTC | 2026-08-16 20:44 UTC | 3h 41m |
| N330V |  | Kintail Farm Airport (GA00) | Cy Nunnally Memorial Airport (KD73) | 2026-08-16 20:32 UTC | 2026-08-16 20:43 UTC | 11m |
| N473CA |  | Meadows Field (KBFL) | Meadows Field (KBFL) | 2026-08-16 20:06 UTC | 2026-08-16 20:42 UTC | 35m |
| N713BY |  | UT09 (UT09) | K43U (K43U) | 2026-08-16 20:00 UTC | 2026-08-16 20:41 UTC | 40m |
| UAE41M | Emirates | Lyon Saint-Exupery Airport (LFLL) | Buraimi Airport (OOBR) | 2026-08-16 14:12 UTC | 2026-08-16 20:39 UTC | 6h 26m |
| 00000000 |  | Kingston Airport (CYGK) | Taber Airport (CED5) | 2026-08-16 16:07 UTC | 2026-08-16 20:37 UTC | 4h 29m |
| EJA759 | EJA | Indianapolis Executive Airport (KTYQ) | K36U (K36U) | 2026-08-16 17:41 UTC | 2026-08-16 20:33 UTC | 2h 51m |
| TGELY | TGE | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-08-16 20:07 UTC | 2026-08-16 20:33 UTC | 25m |
| N396FS |  | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 2026-08-16 20:09 UTC | 2026-08-16 20:33 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
