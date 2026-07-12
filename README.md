# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_19:36:06_UTC-green)

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

**Latest saved flight:** 2026-07-12 19:36:06 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-12 19:36:06 UTC

- **139,206** saved flights
- **46,906** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **139,206** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,671,850.9 tonnes** estimated CO2 emissions
- **96,918,891 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5673 |
| 2 | SkyWest Airlines | 5103 |
| 3 | EJA | 2732 |
| 4 | IndiGo | 2559 |
| 5 | American Airlines | 2197 |
| 6 | Southwest Airlines | 2095 |
| 7 | ENY | 1741 |
| 8 | Delta Air Lines | 1653 |
| 9 | Lufthansa | 1422 |
| 10 | LATAM Airlines | 1279 |
| 11 | Vueling | 1202 |
| 12 | WIF | 1200 |
| 13 | AZU | 1195 |
| 14 | LXJ | 1070 |
| 15 | AXM | 1041 |
| 16 | Swiss International | 992 |
| 17 | easyJet | 906 |
| 18 | All Nippon Airways | 892 |
| 19 | Alaska Airlines | 875 |
| 20 | QLK | 865 |
| 21 | EJU | 860 |
| 22 | VIV | 766 |
| 23 | Air France | 748 |
| 24 | AEE | 747 |
| 25 | CXK | 746 |
| 26 | JetBlue | 732 |
| 27 | United Airlines | 730 |
| 28 | Cathay Pacific | 728 |
| 29 | MXY | 723 |
| 30 | GLO | 712 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 119574 |
| 2 | 🇪🇸 ES | 9150 |
| 3 | 🇮🇳 IN | 8018 |
| 4 | 🇦🇺 AU | 7926 |
| 5 | 🇧🇷 BR | 7851 |
| 6 | 🇨🇦 CA | 7307 |
| 7 | 🇮🇹 IT | 7282 |
| 8 | 🇩🇪 DE | 7276 |
| 9 | 🇬🇧 GB | 6327 |
| 10 | 🇯🇵 JP | 5845 |
| 11 | 🇫🇷 FR | 5557 |
| 12 | 🇨🇴 CO | 4401 |
| 13 | 🇲🇽 MX | 4039 |
| 14 | 🇬🇷 GR | 3966 |
| 15 | 🇳🇴 NO | 3753 |
| 16 | 🇨🇭 CH | 3618 |
| 17 | 🇹🇷 TR | 3260 |
| 18 | 🇲🇾 MY | 2702 |
| 19 | 🇵🇱 PL | 2333 |
| 20 | 🇿🇦 ZA | 2284 |
| 21 | 🇳🇿 NZ | 2134 |
| 22 | 🇹🇭 TH | 2105 |
| 23 | 🇰🇷 KR | 2005 |
| 24 | 🇵🇭 PH | 1891 |
| 25 | 🇬🇹 GT | 1847 |
| 26 | 🇲🇦 MA | 1464 |
| 27 | 🇲🇪 ME | 1383 |
| 28 | 🇳🇱 NL | 1307 |
| 29 | 🇭🇷 HR | 1261 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2883 |
| 2 | Denver International Airport |  | US | 2328 |
| 3 | Tokyo International Airport |  | JP | 1900 |
| 4 | Indira Gandhi International Airport |  | IN | 1772 |
| 5 | Harry Reid International Airport |  | US | 1736 |
| 6 | Guaymaral Airport |  | CO | 1696 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1606 |
| 8 | Zurich Airport |  | CH | 1551 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1463 |
| 10 | La Aurora Airport |  | GT | 1427 |
| 11 | Frankfurt am Main International Airport |  | DE | 1372 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1332 |
| 13 | Chicago O'Hare International Airport |  | US | 1310 |
| 14 | Salt Lake City International Airport |  | US | 1238 |
| 15 | El Dorado International Airport |  | CO | 1236 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1194 |
| 17 | Macau International Airport |  | MO | 1188 |
| 18 | Capua Airport |  | IT | 1146 |
| 19 | Madrid Barajas International Airport |  | ES | 1135 |
| 20 | Congonhas Airport |  | BR | 1120 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1120 |
| 22 | Kuala Lumpur International Airport |  | MY | 1048 |
| 23 | Charlotte/Douglas International Airport |  | US | 1018 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 999 |
| 25 | Charles de Gaulle International Airport |  | FR | 991 |
| 26 | Bengaluru International Airport |  | IN | 961 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 960 |
| 28 | Malpensa International Airport |  | IT | 905 |
| 29 | Ninoy Aquino International Airport |  | PH | 880 |
| 30 | Daniel K Inouye International Airport |  | US | 854 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 849 |
| 32 | Barcelona International Airport |  | ES | 848 |
| 33 | Tenerife Norte Airport |  | ES | 816 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 815 |
| 35 | Calgary International Airport |  | CA | 802 |
| 36 | Viracopos International Airport |  | BR | 794 |
| 37 | Seattle-Tacoma International Airport |  | US | 792 |
| 38 | Scottsdale Airport |  | US | 791 |
| 39 | Amsterdam Airport Schiphol |  | NL | 782 |
| 40 | Vitoria/Foronda Airport |  | ES | 776 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 715 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 504 | 21m | 244 km | 2,122.2 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 342 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 341 | 24m | 225 km | 1,322.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 190 | 26m | 215 km | 703.7 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 186 | 20m | 99 km | 318.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 184 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 168 | 18m | 144 km | 417.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 160 | 1h 1m | 695 km | 1,917.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 157 | 1h 38m | 1,156 km | 3,132.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 155 | 14m | 154 km | 410.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 152 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N352HP |  | Salt Lake City International Airport (KSLC) | Provo Municipal Airport (KPVU) | 2026-07-12 19:05 UTC | 2026-07-12 19:36 UTC | 31m |
| TKR16 | TKR | Hill Afb Airport (KHIF) | Michael Army Air Field (Dugway Proving Ground) Airport (KDPG) | 2026-07-12 19:18 UTC | 2026-07-12 19:34 UTC | 16m |
| JBU2260 | JetBlue | Madrid Barajas International Airport (LEMD) | General Edward Lawrence Logan International Airport (KBOS) | 2026-07-12 12:23 UTC | 2026-07-12 19:31 UTC | 7h 7m |
| N6227R |  | Richters Airport (87MO) | Richters Airport (87MO) | 2026-07-12 19:03 UTC | 2026-07-12 19:23 UTC | 20m |
| FFT2022 | FFT | Detroit Metro Wayne County Airport (KDTW) | Philadelphia International Airport (KPHL) | 2026-07-12 18:12 UTC | 2026-07-12 19:20 UTC | 1h 7m |
| N41HX |  | 01UT (01UT) | Blanding Municipal Airport (KBDG) | 2026-07-12 18:54 UTC | 2026-07-12 19:20 UTC | 25m |
| N5331F |  | Central Jersey Regional Airport (K47N) | Somerset Airport (KSMQ) | 2026-07-12 18:48 UTC | 2026-07-12 19:18 UTC | 29m |
| N8212Z |  | 2OH9 (2OH9) | 2OH9 (2OH9) | 2026-07-12 18:46 UTC | 2026-07-12 19:16 UTC | 29m |
| N766LF |  | Vero Beach Regional Airport (KVRB) | 8NC3 (8NC3) | 2026-07-12 17:54 UTC | 2026-07-12 19:13 UTC | 1h 18m |
| N690E |  | Biddeford Municipal Airport (KB19) | Wings Field (KLOM) | 2026-07-12 17:58 UTC | 2026-07-12 19:11 UTC | 1h 12m |
| VJH357 | VJH | Dinard-Pleurtuit-Saint-Malo Airport (LFRD) | Ibiza Airport (LEIB) | 2026-07-12 17:15 UTC | 2026-07-12 19:10 UTC | 1h 55m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-07-12 18:55 UTC | 2026-07-12 19:10 UTC | 14m |
| N35HF |  | Newark Liberty International Airport (KEWR) | Francis S Gabreski Airport (KFOK) | 2026-07-12 18:33 UTC | 2026-07-12 19:08 UTC | 35m |
| T815 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-12 18:34 UTC | 2026-07-12 19:07 UTC | 32m |
| T825 |  | Bolinder Field/Tooele Valley Airport (KTVY) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-07-12 18:34 UTC | 2026-07-12 19:07 UTC | 32m |
| N40JF |  | 0OI4 (0OI4) | 1OI1 (1OI1) | 2026-07-12 18:50 UTC | 2026-07-12 19:03 UTC | 13m |
| THY1DY | Turkish Airlines | Istanbul Airport (LTFM) | Smolensk North Airport (XUBS) | 2026-07-12 16:45 UTC | 2026-07-12 19:03 UTC | 2h 17m |
| N160EA |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-07-12 18:49 UTC | 2026-07-12 19:03 UTC | 13m |
| N55FA |  | Wings Field (KLOM) | Wings Field (KLOM) | 2026-07-12 18:35 UTC | 2026-07-12 19:02 UTC | 27m |
| N223AL |  | General Mariano Matamoros Airport (MMCB) | General Mariano Matamoros Airport (MMCB) | 2026-07-12 14:50 UTC | 2026-07-12 19:02 UTC | 4h 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
