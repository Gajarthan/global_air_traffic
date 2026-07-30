# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_16:36:39_UTC-green)

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

**Latest saved flight:** 2026-07-30 16:36:39 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-30 16:36:39 UTC

- **160,656** saved flights
- **53,084** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **160,656** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,927,767.1 tonnes** estimated CO2 emissions
- **111,754,615 km** total distance flown
- **856 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6437 |
| 2 | SkyWest Airlines | 5853 |
| 3 | EJA | 3183 |
| 4 | IndiGo | 2830 |
| 5 | American Airlines | 2537 |
| 6 | Southwest Airlines | 2516 |
| 7 | ENY | 1997 |
| 8 | Delta Air Lines | 1908 |
| 9 | Lufthansa | 1517 |
| 10 | LATAM Airlines | 1508 |
| 11 | AZU | 1413 |
| 12 | WIF | 1361 |
| 13 | Vueling | 1337 |
| 14 | LXJ | 1238 |
| 15 | AXM | 1120 |
| 16 | Swiss International | 1108 |
| 17 | easyJet | 1051 |
| 18 | Alaska Airlines | 1002 |
| 19 | QLK | 991 |
| 20 | All Nippon Airways | 990 |
| 21 | EJU | 983 |
| 22 | VIV | 883 |
| 23 | CXK | 857 |
| 24 | United Airlines | 849 |
| 25 | Cathay Pacific | 847 |
| 26 | GLO | 846 |
| 27 | AEE | 845 |
| 28 | Air France | 837 |
| 29 | MXY | 833 |
| 30 | JetBlue | 821 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 138555 |
| 2 | 🇪🇸 ES | 10309 |
| 3 | 🇧🇷 BR | 9182 |
| 4 | 🇦🇺 AU | 9080 |
| 5 | 🇮🇳 IN | 8904 |
| 6 | 🇨🇦 CA | 8724 |
| 7 | 🇮🇹 IT | 8290 |
| 8 | 🇩🇪 DE | 8121 |
| 9 | 🇬🇧 GB | 7381 |
| 10 | 🇯🇵 JP | 6531 |
| 11 | 🇫🇷 FR | 6365 |
| 12 | 🇨🇴 CO | 5687 |
| 13 | 🇬🇷 GR | 4612 |
| 14 | 🇲🇽 MX | 4604 |
| 15 | 🇳🇴 NO | 4251 |
| 16 | 🇨🇭 CH | 4224 |
| 17 | 🇹🇷 TR | 3840 |
| 18 | 🇲🇾 MY | 2908 |
| 19 | 🇵🇱 PL | 2729 |
| 20 | 🇿🇦 ZA | 2599 |
| 21 | 🇳🇿 NZ | 2366 |
| 22 | 🇹🇭 TH | 2292 |
| 23 | 🇵🇭 PH | 2117 |
| 24 | 🇰🇷 KR | 2108 |
| 25 | 🇬🇹 GT | 2053 |
| 26 | 🇲🇦 MA | 1625 |
| 27 | 🇲🇪 ME | 1526 |
| 28 | 🇭🇷 HR | 1501 |
| 29 | 🇳🇱 NL | 1476 |
| 30 | 🇲🇴 MO | 1339 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3278 |
| 2 | Denver International Airport |  | US | 2673 |
| 3 | Tokyo International Airport |  | JP | 2063 |
| 4 | Guaymaral Airport |  | CO | 2024 |
| 5 | Indira Gandhi International Airport |  | IN | 1980 |
| 6 | Harry Reid International Airport |  | US | 1951 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1780 |
| 8 | Zurich Airport |  | CH | 1717 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1687 |
| 10 | La Aurora Airport |  | GT | 1594 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1495 |
| 12 | El Dorado International Airport |  | CO | 1471 |
| 13 | Frankfurt am Main International Airport |  | DE | 1468 |
| 14 | Chicago O'Hare International Airport |  | US | 1453 |
| 15 | Salt Lake City International Airport |  | US | 1444 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1341 |
| 17 | Macau International Airport |  | MO | 1339 |
| 18 | Congonhas Airport |  | BR | 1334 |
| 19 | Madrid Barajas International Airport |  | ES | 1275 |
| 20 | Capua Airport |  | IT | 1263 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1230 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 1147 |
| 23 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1140 |
| 24 | Charlotte/Douglas International Airport |  | US | 1125 |
| 25 | Kuala Lumpur International Airport |  | MY | 1111 |
| 26 | Charles de Gaulle International Airport |  | FR | 1103 |
| 27 | Malpensa International Airport |  | IT | 1063 |
| 28 | Bengaluru International Airport |  | IN | 1058 |
| 29 | Ninoy Aquino International Airport |  | PH | 993 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 979 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 977 |
| 32 | Barcelona International Airport |  | ES | 957 |
| 33 | Daniel K Inouye International Airport |  | US | 945 |
| 34 | Seattle-Tacoma International Airport |  | US | 935 |
| 35 | Calgary International Airport |  | CA | 922 |
| 36 | Viracopos International Airport |  | BR | 917 |
| 37 | Scottsdale Airport |  | US | 904 |
| 38 | Tenerife Norte Airport |  | ES | 901 |
| 39 | Oslo Gardermoen Airport |  | NO | 893 |
| 40 | Amsterdam Airport Schiphol |  | NL | 885 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 850 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 584 | 21m | 244 km | 2,459.1 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 383 | 24m | 225 km | 1,485.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 382 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 369 | 1h 9m | 770 km | 4,901.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 296 | 32m | - | - |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 283 | 27m | 275 km | 1,341.0 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 237 | 19m | 165 km | 674.2 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 236 | 22m | 55 km | 224.3 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 229 | 44m | 241 km | 951.2 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 221 | 1h 47m | 1,423 km | 5,423.7 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 212 | 26m | 215 km | 785.2 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 206 | 13m | - | - |
| 18 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 203 | 20m | 250 km | 876.8 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 202 | 20m | 99 km | 346.0 t |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 192 | 30m | 49 km | 162.3 t |
| 21 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 192 | 28m | 152 km | 501.8 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 191 | 1h 15m | 961 km | 3,165.9 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 190 | 18m | 144 km | 472.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 188 | 31m | 369 km | 1,196.7 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 184 | 12m | - | - |
| 26 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 182 | 50m | 556 km | 1,744.6 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 180 | 1h 39m | 1,156 km | 3,590.9 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 178 | 1h 1m | 695 km | 2,133.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 177 | 44m | 452 km | 1,379.5 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 171 | 23m | 218 km | 644.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N75972 |  | Airlake Airport (KLVN) | Airlake Airport (KLVN) | 2026-07-30 15:59 UTC | 2026-07-30 16:36 UTC | 37m |
| N9443L |  | Mansfield Lahm Regional Airport (KMFD) | Findlay Airport (KFDY) | 2026-07-30 15:56 UTC | 2026-07-30 16:27 UTC | 30m |
| N754FG |  | Trenton Mercer Airport (KTTN) | Lehigh Valley International Airport (KABE) | 2026-07-30 15:52 UTC | 2026-07-30 16:26 UTC | 34m |
| N643LV |  | Mesquite Airport (K67L) | North Las Vegas Airport (KVGT) | 2026-07-30 15:47 UTC | 2026-07-30 16:21 UTC | 33m |
| MEA203 | Middle East Airlines | Rayak Air Base (OLRA) | Craiova Airport (LRCV) | 2026-07-30 14:29 UTC | 2026-07-30 16:19 UTC | 1h 49m |
| CXK491 | CXK | K55J (K55J) | K55J (K55J) | 2026-07-30 16:12 UTC | 2026-07-30 16:18 UTC | 6m |
| T7ACA |  | Belgrade Nikola Tesla Airport (LYBE) | Slavonski Jelas Airport (LDOR) | 2026-07-30 15:49 UTC | 2026-07-30 16:16 UTC | 26m |
| TGHGF | TGH | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 2026-07-30 15:46 UTC | 2026-07-30 16:16 UTC | 29m |
| N560FW |  | Fort Worth Meacham International Airport (KFTW) | Las Arenas Earth And Sky Observatory Airport (2CO2) | 2026-07-30 14:42 UTC | 2026-07-30 16:12 UTC | 1h 30m |
| DKBXP | DKB | Langkampfen Airport (LOIK) | Samedan Airport (LSZS) | 2026-07-30 08:46 UTC | 2026-07-30 16:11 UTC | 7h 25m |
| N13887 |  | Pleasant Grove Airpark (8TN2) | Huntsville Executive Tom Sharp Jr Field (KMDQ) | 2026-07-30 15:51 UTC | 2026-07-30 16:11 UTC | 19m |
| ZKIDH | ZKI | Balclutha Aerodrome (NZBA) | Taieri Airport (NZTI) | 2026-07-30 15:52 UTC | 2026-07-30 16:10 UTC | 17m |
| HBXKX | HBX | Locarno Airport (LSZL) | Ambri Airport (LSPM) | 2026-07-30 15:40 UTC | 2026-07-30 16:09 UTC | 28m |
| VAR469 | VAR | Buckeye Municipal Airport (KBXK) | Buckeye Municipal Airport (KBXK) | 2026-07-30 15:37 UTC | 2026-07-30 16:09 UTC | 31m |
| N423AC |  | East Jordan City Airport (KY94) | East Jordan City Airport (KY94) | 2026-07-30 15:23 UTC | 2026-07-30 16:08 UTC | 44m |
| PAV651H | PAV | Madrid Barajas International Airport (LEMD) | Logrono-Agoncillo Airport (LELO) | 2026-07-30 15:42 UTC | 2026-07-30 16:06 UTC | 24m |
| ECNKC | ECN | Castellón De La Plana Airport (LECN) | Castellón De La Plana Airport (LECN) | 2026-07-30 16:02 UTC | 2026-07-30 16:05 UTC | 3m |
| N54AP |  | San Antonio International Airport (KSAT) | Daviess County Airport (KDCY) | 2026-07-30 14:02 UTC | 2026-07-30 16:05 UTC | 2h 3m |
| TGARR | TGA | La Aurora Airport (MGGT) | Zacapa Airport (MGZA) | 2026-07-30 15:20 UTC | 2026-07-30 16:05 UTC | 44m |
| INOST | INO | Torino / Aeritalia Airport (LIMA) | Torino / Aeritalia Airport (LIMA) | 2026-07-30 15:48 UTC | 2026-07-30 16:03 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
