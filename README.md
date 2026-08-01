# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_18:22:50_UTC-green)

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

**Latest saved flight:** 2026-08-01 18:22:50 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-01 18:22:50 UTC

- **165,222** saved flights
- **54,252** unique routes
- **138** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **165,222** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,986,542.9 tonnes** estimated CO2 emissions
- **115,161,908 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 6596 |
| 2 | SkyWest Airlines | 6009 |
| 3 | EJA | 3277 |
| 4 | IndiGo | 2910 |
| 5 | American Airlines | 2602 |
| 6 | Southwest Airlines | 2593 |
| 7 | ENY | 2055 |
| 8 | Delta Air Lines | 1969 |
| 9 | LATAM Airlines | 1539 |
| 10 | Lufthansa | 1537 |
| 11 | AZU | 1450 |
| 12 | WIF | 1388 |
| 13 | Vueling | 1366 |
| 14 | LXJ | 1285 |
| 15 | AXM | 1141 |
| 16 | Swiss International | 1132 |
| 17 | easyJet | 1086 |
| 18 | Alaska Airlines | 1018 |
| 19 | EJU | 1013 |
| 20 | QLK | 1011 |
| 21 | All Nippon Airways | 1009 |
| 22 | VIV | 909 |
| 23 | CXK | 885 |
| 24 | Cathay Pacific | 878 |
| 25 | AEE | 868 |
| 26 | United Airlines | 867 |
| 27 | GLO | 866 |
| 28 | Air France | 853 |
| 29 | MXY | 851 |
| 30 | JetBlue | 839 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 142613 |
| 2 | 🇪🇸 ES | 10573 |
| 3 | 🇧🇷 BR | 9417 |
| 4 | 🇦🇺 AU | 9259 |
| 5 | 🇮🇳 IN | 9133 |
| 6 | 🇨🇦 CA | 8977 |
| 7 | 🇮🇹 IT | 8534 |
| 8 | 🇩🇪 DE | 8273 |
| 9 | 🇬🇧 GB | 7603 |
| 10 | 🇯🇵 JP | 6660 |
| 11 | 🇫🇷 FR | 6555 |
| 12 | 🇨🇴 CO | 5948 |
| 13 | 🇬🇷 GR | 4765 |
| 14 | 🇲🇽 MX | 4730 |
| 15 | 🇨🇭 CH | 4351 |
| 16 | 🇳🇴 NO | 4341 |
| 17 | 🇹🇷 TR | 3966 |
| 18 | 🇲🇾 MY | 2968 |
| 19 | 🇵🇱 PL | 2802 |
| 20 | 🇿🇦 ZA | 2695 |
| 21 | 🇳🇿 NZ | 2410 |
| 22 | 🇹🇭 TH | 2369 |
| 23 | 🇵🇭 PH | 2172 |
| 24 | 🇬🇹 GT | 2137 |
| 25 | 🇰🇷 KR | 2133 |
| 26 | 🇲🇦 MA | 1662 |
| 27 | 🇭🇷 HR | 1565 |
| 28 | 🇲🇪 ME | 1544 |
| 29 | 🇳🇱 NL | 1499 |
| 30 | 🇲🇴 MO | 1402 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3373 |
| 2 | Denver International Airport |  | US | 2735 |
| 3 | Tokyo International Airport |  | JP | 2095 |
| 4 | Guaymaral Airport |  | CO | 2079 |
| 5 | Indira Gandhi International Airport |  | IN | 2023 |
| 6 | Harry Reid International Airport |  | US | 1997 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1814 |
| 8 | Zurich Airport |  | CH | 1758 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1733 |
| 10 | La Aurora Airport |  | GT | 1654 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1531 |
| 12 | El Dorado International Airport |  | CO | 1518 |
| 13 | Frankfurt am Main International Airport |  | DE | 1495 |
| 14 | Chicago O'Hare International Airport |  | US | 1491 |
| 15 | Salt Lake City International Airport |  | US | 1482 |
| 16 | Macau International Airport |  | MO | 1402 |
| 17 | General Edward Lawrence Logan International Airport |  | US | 1383 |
| 18 | Congonhas Airport |  | BR | 1365 |
| 19 | Madrid Barajas International Airport |  | ES | 1301 |
| 20 | Capua Airport |  | IT | 1294 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1257 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1167 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1163 |
| 24 | Charlotte/Douglas International Airport |  | US | 1158 |
| 25 | Charles de Gaulle International Airport |  | FR | 1129 |
| 26 | Kuala Lumpur International Airport |  | MY | 1124 |
| 27 | Malpensa International Airport |  | IT | 1099 |
| 28 | Bengaluru International Airport |  | IN | 1081 |
| 29 | Ninoy Aquino International Airport |  | PH | 1021 |
| 30 | Norman Y Mineta San Jose International Airport |  | US | 1010 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 1010 |
| 32 | Barcelona International Airport |  | ES | 977 |
| 33 | Daniel K Inouye International Airport |  | US | 964 |
| 34 | Seattle-Tacoma International Airport |  | US | 954 |
| 35 | Calgary International Airport |  | CA | 941 |
| 36 | Viracopos International Airport |  | BR | 937 |
| 37 | Scottsdale Airport |  | US | 924 |
| 38 | Tenerife Norte Airport |  | ES | 921 |
| 39 | Oslo Gardermoen Airport |  | NO | 919 |
| 40 | Reno/Tahoe International Airport |  | US | 907 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 868 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 602 | 21m | 244 km | 2,534.9 t |
| 3 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 397 | 9m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 395 | 24m | 225 km | 1,532.4 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 377 | 1h 9m | 770 km | 5,008.2 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 308 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 301 | 14m | 114 km | 590.4 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 290 | 1h 7m | 706 km | 3,530.8 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 285 | 27m | 275 km | 1,350.5 t |
| 11 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 253 | 22m | 55 km | 240.5 t |
| 13 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 242 | 19m | 165 km | 688.4 t |
| 14 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 239 | 44m | 241 km | 992.8 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 228 | 1h 47m | 1,423 km | 5,595.5 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 217 | 20m | 250 km | 937.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 215 | 26m | 215 km | 796.3 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 210 | 20m | 99 km | 359.7 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 209 | 13m | - | - |
| 20 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 204 | 31m | 49 km | 172.4 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 197 | 1h 15m | 961 km | 3,265.4 t |
| 22 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 196 | 28m | 152 km | 512.2 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 194 | 19m | 144 km | 482.6 t |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 191 | 31m | 369 km | 1,215.8 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 188 | 50m | 556 km | 1,802.1 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 186 | 12m | - | - |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 185 | 1h 38m | 1,156 km | 3,690.7 t |
| 28 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 181 | 1h 1m | 695 km | 2,169.7 t |
| 29 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 181 | 44m | 452 km | 1,410.6 t |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 176 | 24m | 218 km | 663.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N1303T |  | Juneau International Airport (PAJN) | Juneau International Airport (PAJN) | 2026-08-01 17:26 UTC | 2026-08-01 18:22 UTC | 56m |
| SVA775 | Saudia | Cochin International Airport (VOCI) | OM10 (OM10) | 2026-08-01 15:02 UTC | 2026-08-01 18:15 UTC | 3h 12m |
| N18AC |  | Roberts Field (KRDM) | Prineville Airport (KS39) | 2026-08-01 17:56 UTC | 2026-08-01 18:12 UTC | 16m |
| FOXX66 | FOX | Pinal Airpark (KMZJ) | Pinal Airpark (KMZJ) | 2026-08-01 17:56 UTC | 2026-08-01 18:09 UTC | 13m |
| OEBXS | OEB | Graz Airport (LOWG) | Kapfenberg Airport (LOGK) | 2026-08-01 17:43 UTC | 2026-08-01 18:09 UTC | 25m |
| AIZ417 | AIZ | Ben Gurion International Airport (LLBG) | Tbilisi International Airport (UGTB) | 2026-08-01 15:50 UTC | 2026-08-01 17:59 UTC | 2h 8m |
| N15MP |  | Joe Foss Field (KFSD) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 2026-08-01 17:14 UTC | 2026-08-01 17:58 UTC | 44m |
| SFY119 | SFY | Broocke Air Patch Airport (FL95) | Broocke Air Patch Airport (FL95) | 2026-08-01 16:55 UTC | 2026-08-01 17:56 UTC | 1h 0m |
| GCPSS | GCP | Netheravon Airfield (EGDN) | Netheravon Airfield (EGDN) | 2026-08-01 17:08 UTC | 2026-08-01 17:53 UTC | 44m |
| N331FZ |  | KU77 (KU77) | K36U (K36U) | 2026-08-01 17:43 UTC | 2026-08-01 17:51 UTC | 7m |
| N333FR |  | Rogue Valley International/Medford Airport (KMFR) | Spaulding Airport (K1Q2) | 2026-08-01 16:32 UTC | 2026-08-01 17:50 UTC | 1h 18m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-01 17:35 UTC | 2026-08-01 17:50 UTC | 15m |
| EAI2A | EAI | Southampton Airport (EGHI) | Dublin Airport (EIDW) | 2026-08-01 16:26 UTC | 2026-08-01 17:50 UTC | 1h 23m |
| TKR02 | TKR | Hill Afb Airport (KHIF) | K43U (K43U) | 2026-08-01 17:32 UTC | 2026-08-01 17:49 UTC | 16m |
| N15760 |  | Cmelak Field (MA18) | Hartford-Brainard Airport (KHFD) | 2026-08-01 17:24 UTC | 2026-08-01 17:47 UTC | 22m |
| CXK585 | CXK | Brigham City Regional Airport (KBMC) | Wendover Airport (KENV) | 2026-08-01 16:39 UTC | 2026-08-01 17:44 UTC | 1h 5m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-08-01 17:34 UTC | 2026-08-01 17:41 UTC | 7m |
| CHXE5 | CHX | St. Peter-Ording Airport (EDXO) | Heide-Busum Airport (EDXB) | 2026-08-01 17:31 UTC | 2026-08-01 17:41 UTC | 9m |
| N5283M |  | Chino Airport (KCNO) | Chino Airport (KCNO) | 2026-08-01 17:36 UTC | 2026-08-01 17:41 UTC | 4m |
| N516ML |  | Wings Field (KLOM) | Wings Field (KLOM) | 2026-08-01 16:56 UTC | 2026-08-01 17:40 UTC | 43m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
