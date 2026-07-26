# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_23:47:49_UTC-green)

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

**Latest saved flight:** 2026-07-25 23:47:49 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-25 23:47:49 UTC

- **151,480** saved flights
- **50,337** unique routes
- **135** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **151,480** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,811,983.5 tonnes** estimated CO2 emissions
- **105,042,521 km** total distance flown
- **853 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6112 |
| 2 | SkyWest Airlines | 5554 |
| 3 | EJA | 3000 |
| 4 | IndiGo | 2695 |
| 5 | American Airlines | 2407 |
| 6 | Southwest Airlines | 2308 |
| 7 | ENY | 1895 |
| 8 | Delta Air Lines | 1780 |
| 9 | Lufthansa | 1480 |
| 10 | LATAM Airlines | 1404 |
| 11 | AZU | 1317 |
| 12 | WIF | 1276 |
| 13 | Vueling | 1271 |
| 14 | LXJ | 1168 |
| 15 | AXM | 1082 |
| 16 | Swiss International | 1061 |
| 17 | easyJet | 987 |
| 18 | All Nippon Airways | 955 |
| 19 | Alaska Airlines | 947 |
| 20 | QLK | 934 |
| 21 | EJU | 928 |
| 22 | VIV | 835 |
| 23 | CXK | 811 |
| 24 | AEE | 795 |
| 25 | MXY | 795 |
| 26 | JetBlue | 790 |
| 27 | Air France | 788 |
| 28 | GLO | 788 |
| 29 | United Airlines | 783 |
| 30 | Cathay Pacific | 781 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 130794 |
| 2 | 🇪🇸 ES | 9789 |
| 3 | 🇧🇷 BR | 8595 |
| 4 | 🇦🇺 AU | 8518 |
| 5 | 🇮🇳 IN | 8484 |
| 6 | 🇨🇦 CA | 8087 |
| 7 | 🇮🇹 IT | 7837 |
| 8 | 🇩🇪 DE | 7756 |
| 9 | 🇬🇧 GB | 6942 |
| 10 | 🇯🇵 JP | 6262 |
| 11 | 🇫🇷 FR | 5990 |
| 12 | 🇨🇴 CO | 5160 |
| 13 | 🇲🇽 MX | 4373 |
| 14 | 🇬🇷 GR | 4299 |
| 15 | 🇳🇴 NO | 4002 |
| 16 | 🇨🇭 CH | 3973 |
| 17 | 🇹🇷 TR | 3589 |
| 18 | 🇲🇾 MY | 2819 |
| 19 | 🇵🇱 PL | 2569 |
| 20 | 🇿🇦 ZA | 2460 |
| 21 | 🇳🇿 NZ | 2280 |
| 22 | 🇹🇭 TH | 2194 |
| 23 | 🇰🇷 KR | 2068 |
| 24 | 🇵🇭 PH | 2015 |
| 25 | 🇬🇹 GT | 1976 |
| 26 | 🇲🇦 MA | 1543 |
| 27 | 🇲🇪 ME | 1481 |
| 28 | 🇳🇱 NL | 1395 |
| 29 | 🇭🇷 HR | 1386 |
| 30 | 🇲🇴 MO | 1249 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3126 |
| 2 | Denver International Airport |  | US | 2547 |
| 3 | Tokyo International Airport |  | JP | 1997 |
| 4 | Guaymaral Airport |  | CO | 1906 |
| 5 | Indira Gandhi International Airport |  | IN | 1883 |
| 6 | Harry Reid International Airport |  | US | 1871 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1695 |
| 8 | Zurich Airport |  | CH | 1645 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1587 |
| 10 | La Aurora Airport |  | GT | 1531 |
| 11 | Frankfurt am Main International Airport |  | DE | 1430 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1418 |
| 13 | Chicago O'Hare International Airport |  | US | 1398 |
| 14 | Salt Lake City International Airport |  | US | 1364 |
| 15 | El Dorado International Airport |  | CO | 1364 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1294 |
| 17 | Macau International Airport |  | MO | 1249 |
| 18 | Congonhas Airport |  | BR | 1229 |
| 19 | Madrid Barajas International Airport |  | ES | 1208 |
| 20 | Capua Airport |  | IT | 1205 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1174 |
| 22 | Kuala Lumpur International Airport |  | MY | 1085 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1081 |
| 24 | Charlotte/Douglas International Airport |  | US | 1079 |
| 25 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1069 |
| 26 | Charles de Gaulle International Airport |  | FR | 1039 |
| 27 | Bengaluru International Airport |  | IN | 1012 |
| 28 | Malpensa International Airport |  | IT | 993 |
| 29 | Ninoy Aquino International Airport |  | PH | 944 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 917 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 909 |
| 32 | Barcelona International Airport |  | ES | 906 |
| 33 | Daniel K Inouye International Airport |  | US | 904 |
| 34 | Seattle-Tacoma International Airport |  | US | 874 |
| 35 | Tenerife Norte Airport |  | ES | 872 |
| 36 | Calgary International Airport |  | CA | 862 |
| 37 | Viracopos International Airport |  | BR | 857 |
| 38 | Scottsdale Airport |  | US | 854 |
| 39 | Amsterdam Airport Schiphol |  | NL | 838 |
| 40 | Oslo Gardermoen Airport |  | NO | 830 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 804 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 548 | 21m | 244 km | 2,307.5 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 369 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 366 | 24m | 225 km | 1,419.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 353 | 1h 9m | 770 km | 4,689.3 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 289 | 1h 7m | 706 km | 3,518.6 t |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 277 | 32m | - | - |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 271 | 27m | 275 km | 1,284.2 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 226 | 22m | 55 km | 214.8 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 205 | 44m | 241 km | 851.5 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 204 | 1h 47m | 1,423 km | 5,006.5 t |
| 16 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 198 | 20m | 99 km | 339.2 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 197 | 26m | 215 km | 729.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 196 | 13m | - | - |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 191 | 20m | 250 km | 825.0 t |
| 20 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 184 | 27m | 152 km | 480.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 183 | 30m | 49 km | 154.7 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 180 | 1h 15m | 961 km | 2,983.6 t |
| 23 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 178 | 31m | 369 km | 1,133.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 178 | 18m | 144 km | 442.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 178 | 13m | - | - |
| 26 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 174 | 44m | 452 km | 1,356.1 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 170 | 1h 39m | 1,156 km | 3,391.4 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 170 | 1h 1m | 695 km | 2,037.8 t |
| 29 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 166 | 51m | 556 km | 1,591.2 t |
| 30 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 164 | 55m | 136 km | 384.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| TKR03 | TKR | City Of Colorado Springs Municipal Airport (KCOS) | K7V6 (K7V6) | 2026-07-25 23:05 UTC | 2026-07-25 23:47 UTC | 42m |
| TKR40 | TKR | Roberts Field (KRDM) | Ochs Private Airport (72OR) | 2026-07-25 23:21 UTC | 2026-07-25 23:30 UTC | 8m |
| N670WH |  | Rogue Valley International/Medford Airport (KMFR) | Big Muddy Ranch Airport (2OR1) | 2026-07-25 22:41 UTC | 2026-07-25 23:26 UTC | 45m |
| NRD | NRD | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-07-25 22:57 UTC | 2026-07-25 23:24 UTC | 27m |
| N75824 |  | Hurlburt Field (KHRT) | KNKL (KNKL) | 2026-07-25 23:06 UTC | 2026-07-25 23:23 UTC | 16m |
| QLK20D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-07-25 22:41 UTC | 2026-07-25 23:22 UTC | 41m |
| NOE | NOE | Brisbane Archerfield Airport (YBAF) | Brisbane Archerfield Airport (YBAF) | 2026-07-25 23:12 UTC | 2026-07-25 23:22 UTC | 10m |
| DRK153 | DRK | Suvarnabhumi Airport (VTBS) | Naypyidaw Airport (VYEL) | 2026-07-25 22:09 UTC | 2026-07-25 23:19 UTC | 1h 9m |
| TKR167 | TKR | Boise Air Trml/Gowen Field (KBOI) | Reek Ranch Airport (ID63) | 2026-07-25 23:09 UTC | 2026-07-25 23:18 UTC | 9m |
| N6236J |  | Greeley-Weld County Airport (KGXY) | Pine Bluffs Municipal Airport (K82V) | 2026-07-25 22:49 UTC | 2026-07-25 23:18 UTC | 28m |
| N149AE |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-07-25 22:44 UTC | 2026-07-25 23:12 UTC | 28m |
| N739EZ |  | Mc Clellan Airfield (KMCC) | Mc Clellan Airfield (KMCC) | 2026-07-25 22:24 UTC | 2026-07-25 23:10 UTC | 46m |
| TKR140 | TKR | Boise Air Trml/Gowen Field (KBOI) | Josephine Ranch Airport (2ID3) | 2026-07-25 22:55 UTC | 2026-07-25 23:09 UTC | 14m |
| DAL1342 | Delta Air Lines | Salt Lake City International Airport (KSLC) | Sacramento International Airport (KSMF) | 2026-07-25 21:50 UTC | 2026-07-25 23:08 UTC | 1h 18m |
| N5117E |  | Colorado City Municipal Airport (KAZC) | St George Regional Airport (KSGU) | 2026-07-25 22:47 UTC | 2026-07-25 23:08 UTC | 20m |
| TKR160 | TKR | Boise Air Trml/Gowen Field (KBOI) | 0ID5 (0ID5) | 2026-07-25 22:58 UTC | 2026-07-25 23:07 UTC | 9m |
| ASA7004 | Alaska Airlines | Seattle-Tacoma International Airport (KSEA) | Annette Island Airport (PANT) | 2026-07-25 21:45 UTC | 2026-07-25 23:06 UTC | 1h 20m |
| N267MH |  | Eugene F Kranz Toledo Express Airport (KTOL) | 82OH (82OH) | 2026-07-25 22:58 UTC | 2026-07-25 23:04 UTC | 6m |
| N12RH |  | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-07-25 22:28 UTC | 2026-07-25 23:04 UTC | 36m |
| UAL331 | United Airlines | Charles de Gaulle International Airport (LFPG) | Washington Dulles International Airport (KIAD) | 2026-07-25 15:22 UTC | 2026-07-25 23:04 UTC | 7h 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
