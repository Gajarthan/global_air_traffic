# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_18:53:56_UTC-green)

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

**Latest saved flight:** 2026-08-10 18:53:56 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-10 18:53:56 UTC

- **184,875** saved flights
- **58,813** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **184,875** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,220,759.8 tonnes** estimated CO2 emissions
- **128,739,696 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7333 |
| 2 | SkyWest Airlines | 6718 |
| 3 | EJA | 3649 |
| 4 | IndiGo | 3237 |
| 5 | Southwest Airlines | 2899 |
| 6 | American Airlines | 2881 |
| 7 | ENY | 2306 |
| 8 | Delta Air Lines | 2177 |
| 9 | LATAM Airlines | 1731 |
| 10 | AZU | 1660 |
| 11 | Lufthansa | 1626 |
| 12 | WIF | 1530 |
| 13 | Vueling | 1526 |
| 14 | LXJ | 1455 |
| 15 | easyJet | 1269 |
| 16 | Swiss International | 1267 |
| 17 | AXM | 1235 |
| 18 | EJU | 1142 |
| 19 | QLK | 1135 |
| 20 | All Nippon Airways | 1125 |
| 21 | Alaska Airlines | 1106 |
| 22 | VIV | 1017 |
| 23 | GLO | 989 |
| 24 | Air France | 961 |
| 25 | AEE | 960 |
| 26 | CXK | 959 |
| 27 | Cathay Pacific | 947 |
| 28 | PGT | 943 |
| 29 | United Airlines | 942 |
| 30 | MXY | 919 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 157943 |
| 2 | 🇪🇸 ES | 11891 |
| 3 | 🇧🇷 BR | 10619 |
| 4 | 🇦🇺 AU | 10306 |
| 5 | 🇮🇳 IN | 10141 |
| 6 | 🇨🇦 CA | 10077 |
| 7 | 🇮🇹 IT | 9552 |
| 8 | 🇩🇪 DE | 9139 |
| 9 | 🇬🇧 GB | 8585 |
| 10 | 🇯🇵 JP | 7511 |
| 11 | 🇫🇷 FR | 7398 |
| 12 | 🇨🇴 CO | 6956 |
| 13 | 🇬🇷 GR | 5424 |
| 14 | 🇲🇽 MX | 5273 |
| 15 | 🇨🇭 CH | 4944 |
| 16 | 🇹🇷 TR | 4840 |
| 17 | 🇳🇴 NO | 4757 |
| 18 | 🇲🇾 MY | 3220 |
| 19 | 🇿🇦 ZA | 3108 |
| 20 | 🇵🇱 PL | 3087 |
| 21 | 🇹🇭 TH | 2862 |
| 22 | 🇳🇿 NZ | 2629 |
| 23 | 🇵🇭 PH | 2441 |
| 24 | 🇬🇹 GT | 2364 |
| 25 | 🇰🇷 KR | 2287 |
| 26 | 🇲🇦 MA | 1870 |
| 27 | 🇭🇷 HR | 1859 |
| 28 | 🇲🇪 ME | 1668 |
| 29 | 🇳🇱 NL | 1657 |
| 30 | 🇲🇴 MO | 1521 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3834 |
| 2 | Denver International Airport |  | US | 3049 |
| 3 | Tokyo International Airport |  | JP | 2329 |
| 4 | Indira Gandhi International Airport |  | IN | 2274 |
| 5 | Guaymaral Airport |  | CO | 2261 |
| 6 | Harry Reid International Airport |  | US | 2161 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1981 |
| 8 | Zurich Airport |  | CH | 1977 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1916 |
| 10 | La Aurora Airport |  | GT | 1813 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1683 |
| 12 | El Dorado International Airport |  | CO | 1658 |
| 13 | Salt Lake City International Airport |  | US | 1645 |
| 14 | Chicago O'Hare International Airport |  | US | 1644 |
| 15 | Frankfurt am Main International Airport |  | DE | 1594 |
| 16 | Congonhas Airport |  | BR | 1542 |
| 17 | Macau International Airport |  | MO | 1521 |
| 18 | Madrid Barajas International Airport |  | ES | 1454 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1451 |
| 20 | Capua Airport |  | IT | 1451 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1377 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1321 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1288 |
| 24 | Malpensa International Airport |  | IT | 1276 |
| 25 | Charles de Gaulle International Airport |  | FR | 1264 |
| 26 | Charlotte/Douglas International Airport |  | US | 1252 |
| 27 | Kuala Lumpur International Airport |  | MY | 1208 |
| 28 | Bengaluru International Airport |  | IN | 1201 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1154 |
| 30 | Ninoy Aquino International Airport |  | PH | 1151 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1132 |
| 32 | Barcelona International Airport |  | ES | 1095 |
| 33 | Viracopos International Airport |  | BR | 1065 |
| 34 | Seattle-Tacoma International Airport |  | US | 1061 |
| 35 | Reno/Tahoe International Airport |  | US | 1060 |
| 36 | Calgary International Airport |  | CA | 1052 |
| 37 | Daniel K Inouye International Airport |  | US | 1050 |
| 38 | Oslo Gardermoen Airport |  | NO | 1031 |
| 39 | Tenerife Norte Airport |  | ES | 1010 |
| 40 | Vitoria/Foronda Airport |  | ES | 1003 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 933 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 678 | 21m | 244 km | 2,854.9 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 444 | 1h 8m | 770 km | 5,898.2 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 430 | 24m | 225 km | 1,668.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 429 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 328 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 310 | 27m | 275 km | 1,469.0 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 300 | 1h 7m | 706 km | 3,652.5 t |
| 10 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 276 | 44m | 241 km | 1,146.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 270 | 22m | 55 km | 256.6 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 263 | 8m | - | - |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 262 | 1h 49m | 1,423 km | 6,429.9 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 249 | 20m | 250 km | 1,075.5 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 231 | 26m | 215 km | 855.5 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 231 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 228 | 19m | 99 km | 390.5 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 227 | 1h 15m | 961 km | 3,762.6 t |
| 22 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 224 | 12m | - | - |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 222 | 50m | 556 km | 2,128.1 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 222 | 19m | 144 km | 552.2 t |
| 25 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 219 | 1h 38m | 1,156 km | 4,369.0 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 218 | 24m | 218 km | 821.3 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 215 | 31m | 369 km | 1,368.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 202 | 1h 1m | 695 km | 2,421.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N40057 |  | Van Nuys Airport (KVNY) | Santa Barbara Municipal Airport (KSBA) | 2026-08-10 17:54 UTC | 2026-08-10 18:53 UTC | 59m |
| CNS101 | CNS | Portsmouth International At Pease Airport (KPSM) | Concord Municipal Airport (KCON) | 2026-08-10 18:37 UTC | 2026-08-10 18:50 UTC | 12m |
| N1885M |  | Wasilla Airport (PAWS) | Helio Airport (2AK7) | 2026-08-10 17:49 UTC | 2026-08-10 18:50 UTC | 1h 1m |
| TKR855 | TKR | K36U (K36U) | Bolinder Field/Tooele Valley Airport (KTVY) | 2026-08-10 18:22 UTC | 2026-08-10 18:42 UTC | 19m |
| WAKE67 | WAK | Albuquerque International Sunport Airport (KABQ) | Albuquerque International Sunport Airport (KABQ) | 2026-08-10 18:27 UTC | 2026-08-10 18:38 UTC | 10m |
| C6551 |  | Miami-Opa Locka Executive Airport (KOPF) | North Perry Airport (KHWO) | 2026-08-10 18:30 UTC | 2026-08-10 18:36 UTC | 6m |
| N7199H |  | Ketcham Lndg Area Airport (VT30) | Bonebender Airport (41NY) | 2026-08-10 18:04 UTC | 2026-08-10 18:34 UTC | 29m |
| MAVRK29 | MAV | Lincoln Airport (KLNK) | Delta County Airport (KESC) | 2026-08-10 16:14 UTC | 2026-08-10 18:32 UTC | 2h 17m |
| EMB35 | EMB | Fazenda Cambuhy Airport (SDMY) | Marchesan S.A. Airport (SDME) | 2026-08-10 18:25 UTC | 2026-08-10 18:30 UTC | 4m |
| N282ME |  | Quast Airport (MN62) | Airlake Airport (KLVN) | 2026-08-10 18:01 UTC | 2026-08-10 18:30 UTC | 29m |
| N85FF |  | AZ86 (AZ86) | Montezuma Airport (19AZ) | 2026-08-10 18:18 UTC | 2026-08-10 18:26 UTC | 8m |
| TKR210 | TKR | Casper/Natrona County International Airport (KCPR) | Rock & A Hard Place Ranch Airport (WY61) | 2026-08-10 18:17 UTC | 2026-08-10 18:25 UTC | 8m |
| NSE8845 | NSE | Jose Maria Cordova International Airport (SKRG) | Enrique Olaya Herrera Airport (SKMD) | 2026-08-10 18:11 UTC | 2026-08-10 18:23 UTC | 11m |
| N421DK |  | Oakland San Francisco Bay Airport (KOAK) | Truckee-Tahoe Airport (KTRK) | 2026-08-10 17:40 UTC | 2026-08-10 18:23 UTC | 42m |
| N4347R |  | Dupage Airport (KDPA) | Dupage Airport (KDPA) | 2026-08-10 17:38 UTC | 2026-08-10 18:21 UTC | 43m |
| HK4476 |  | El Dorado International Airport (SKBO) | La Nubia Airport (SKMZ) | 2026-08-10 17:46 UTC | 2026-08-10 18:21 UTC | 34m |
| N40SF |  | Tallahassee International Airport (KTLH) | Cairo-Grady County Airport (K70J) | 2026-08-10 17:24 UTC | 2026-08-10 18:21 UTC | 57m |
| N895CA |  | Aztec Municipal Airport (KN19) | Phoenix Sky Harbor International Airport (KPHX) | 2026-08-10 17:36 UTC | 2026-08-10 18:21 UTC | 45m |
| N429SL |  | Harrington Airport (20ID) | Boise Air Trml/Gowen Field (KBOI) | 2026-08-10 18:14 UTC | 2026-08-10 18:19 UTC | 5m |
| EJU48FM | EJU | L'Aquila / Preturo Airport (LIAP) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-10 17:45 UTC | 2026-08-10 18:19 UTC | 34m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
