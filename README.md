# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_23:34:18_UTC-green)

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

**Latest saved flight:** 2026-08-22 23:34:18 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 23:34:18 UTC

- **227,293** saved flights
- **70,518** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **227,293** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,740,311.5 tonnes** estimated CO2 emissions
- **158,858,640 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9121 |
| 2 | SkyWest Airlines | 8096 |
| 3 | EJA | 4389 |
| 4 | IndiGo | 3831 |
| 5 | American Airlines | 3739 |
| 6 | Southwest Airlines | 3546 |
| 7 | Delta Air Lines | 2915 |
| 8 | ENY | 2788 |
| 9 | LATAM Airlines | 2183 |
| 10 | AZU | 2109 |
| 11 | Vueling | 1925 |
| 12 | Lufthansa | 1860 |
| 13 | WIF | 1797 |
| 14 | LXJ | 1790 |
| 15 | easyJet | 1579 |
| 16 | Swiss International | 1514 |
| 17 | AXM | 1493 |
| 18 | United Airlines | 1441 |
| 19 | EJU | 1435 |
| 20 | QLK | 1421 |
| 21 | Alaska Airlines | 1378 |
| 22 | All Nippon Airways | 1356 |
| 23 | GLO | 1264 |
| 24 | VIV | 1250 |
| 25 | PGT | 1247 |
| 26 | Air France | 1235 |
| 27 | WMT | 1229 |
| 28 | Wizz Air | 1178 |
| 29 | JetBlue | 1137 |
| 30 | AEE | 1130 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 190400 |
| 2 | 🇪🇸 ES | 14567 |
| 3 | 🇧🇷 BR | 13284 |
| 4 | 🇦🇺 AU | 12785 |
| 5 | 🇨🇦 CA | 12592 |
| 6 | 🇮🇹 IT | 12213 |
| 7 | 🇮🇳 IN | 11937 |
| 8 | 🇩🇪 DE | 11177 |
| 9 | 🇬🇧 GB | 10688 |
| 10 | 🇨🇴 CO | 9374 |
| 11 | 🇯🇵 JP | 9196 |
| 12 | 🇫🇷 FR | 9094 |
| 13 | 🇹🇷 TR | 6669 |
| 14 | 🇬🇷 GR | 6643 |
| 15 | 🇲🇽 MX | 6346 |
| 16 | 🇨🇭 CH | 5996 |
| 17 | 🇳🇴 NO | 5601 |
| 18 | 🇲🇾 MY | 3981 |
| 19 | 🇿🇦 ZA | 3923 |
| 20 | 🇹🇭 TH | 3889 |
| 21 | 🇵🇱 PL | 3776 |
| 22 | 🇳🇿 NZ | 3151 |
| 23 | 🇵🇭 PH | 3093 |
| 24 | 🇬🇹 GT | 2873 |
| 25 | 🇰🇷 KR | 2678 |
| 26 | 🇭🇷 HR | 2568 |
| 27 | 🇲🇦 MA | 2296 |
| 28 | 🇲🇪 ME | 2053 |
| 29 | 🇳🇱 NL | 2027 |
| 30 | 🇮🇩 ID | 1952 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4767 |
| 2 | Denver International Airport |  | US | 3710 |
| 3 | Indira Gandhi International Airport |  | IN | 2752 |
| 4 | Tokyo International Airport |  | JP | 2749 |
| 5 | Guaymaral Airport |  | CO | 2647 |
| 6 | Harry Reid International Airport |  | US | 2472 |
| 7 | Zurich Airport |  | CH | 2361 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2331 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2292 |
| 10 | La Aurora Airport |  | GT | 2189 |
| 11 | El Dorado International Airport |  | CO | 2083 |
| 12 | Chicago O'Hare International Airport |  | US | 2070 |
| 13 | Salt Lake City International Airport |  | US | 2000 |
| 14 | Congonhas Airport |  | BR | 1939 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1936 |
| 16 | Frankfurt am Main International Airport |  | DE | 1823 |
| 17 | Madrid Barajas International Airport |  | ES | 1771 |
| 18 | Capua Airport |  | IT | 1761 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1702 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1697 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1643 |
| 22 | Malpensa International Airport |  | IT | 1614 |
| 23 | Macau International Airport |  | MO | 1594 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1590 |
| 25 | Charles de Gaulle International Airport |  | FR | 1573 |
| 26 | Charlotte/Douglas International Airport |  | US | 1491 |
| 27 | Ninoy Aquino International Airport |  | PH | 1480 |
| 28 | Kuala Lumpur International Airport |  | MY | 1446 |
| 29 | Barcelona International Airport |  | ES | 1413 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1382 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1350 |
| 32 | Viracopos International Airport |  | BR | 1347 |
| 33 | Bengaluru International Airport |  | IN | 1345 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1343 |
| 35 | Seattle-Tacoma International Airport |  | US | 1343 |
| 36 | Calgary International Airport |  | CA | 1296 |
| 37 | Don Mueang International Airport |  | TH | 1276 |
| 38 | Oslo Gardermoen Airport |  | NO | 1264 |
| 39 | Vitoria/Foronda Airport |  | ES | 1247 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1228 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1075 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 823 | 21m | 244 km | 3,465.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 564 | 1h 6m | 770 km | 7,492.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 547 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 514 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 356 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 343 | 1h 50m | 1,423 km | 8,417.8 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 330 | 44m | 241 km | 1,370.8 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 313 | 1h 7m | 706 km | 3,810.8 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 306 | 21m | 250 km | 1,321.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 305 | 22m | 55 km | 289.9 t |
| 15 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 16 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 293 | 44m | 555 km | 2,805.6 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 291 | 1h 38m | 1,156 km | 5,805.3 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 288 | 24m | 218 km | 1,085.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 284 | 19m | 99 km | 486.5 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 276 | 27m | 215 km | 1,022.2 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 267 | 1h 14m | 961 km | 4,425.7 t |
| 22 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 263 | 13m | - | - |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 262 | 12m | - | - |
| 25 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 259 | 19m | 144 km | 644.2 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 245 | 1h 50m | 1,304 km | 5,511.9 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 239 | 28m | 152 km | 624.6 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N29MA |  | Reno/Tahoe International Airport (KRNO) | Minden-Tahoe Airport (KMEV) | 2026-08-22 22:50 UTC | 2026-08-22 23:34 UTC | 43m |
| N916NT |  | Montgomery-Gibbs Executive Airport (KMYF) | Hemet-Ryan Airport (KHMT) | 2026-08-22 22:54 UTC | 2026-08-22 23:34 UTC | 39m |
| N295HS |  | Merritt Island Airport (KCOI) | Valkaria Airport (KX59) | 2026-08-22 23:12 UTC | 2026-08-22 23:29 UTC | 16m |
| N310BF |  | WN36 (WN36) | Talus Ranch Airport (WA97) | 2026-08-22 22:41 UTC | 2026-08-22 23:21 UTC | 39m |
| PAG907T | PAG | Winnipeg James Armstrong Richardson International Airport (CYWG) | Winnipeg James Armstrong Richardson International Airport (CYWG) | 2026-08-22 21:09 UTC | 2026-08-22 23:15 UTC | 2h 5m |
| TRP7 | TRP | Robinson Airport (MD14) | Ronald Reagan Washington Ntl Airport (KDCA) | 2026-08-22 23:00 UTC | 2026-08-22 23:11 UTC | 11m |
| N407MZ |  | Albuquerque International Sunport Airport (KABQ) | Los Alamos Airport (KLAM) | 2026-08-22 22:42 UTC | 2026-08-22 23:06 UTC | 23m |
| VT663 |  | Faa'a International Airport (NTAA) | Tikehau Airport (NTGC) | 2026-08-22 20:54 UTC | 2026-08-22 23:00 UTC | 2h 5m |
| AAL3049 | American Airlines | Philadelphia International Airport (KPHL) | St Louis Lambert International Airport (KSTL) | 2026-08-22 20:50 UTC | 2026-08-22 22:55 UTC | 2h 4m |
| TRF509 | TRF | Addison Airport (KADS) | Caddo Mills Municipal Airport (K7F3) | 2026-08-22 21:56 UTC | 2026-08-22 22:55 UTC | 59m |
| N704BH |  | Jordan Field (NR02) | Gastonia Municipal Airport (KAKH) | 2026-08-22 21:39 UTC | 2026-08-22 22:54 UTC | 1h 15m |
| JST221 | JST | Sydney Kingsford Smith International Airport (YSSY) | Queenstown International Airport (NZQN) | 2026-08-22 20:32 UTC | 2026-08-22 22:52 UTC | 2h 20m |
| EJA429 | EJA | San Francisco International Airport (KSFO) | Ellsworth Municipal Airport (K9K7) | 2026-08-22 20:01 UTC | 2026-08-22 22:48 UTC | 2h 47m |
| N378BD |  | Boeing Field/King County International Airport (KBFI) | Thompson Airport (WA61) | 2026-08-22 22:33 UTC | 2026-08-22 22:46 UTC | 12m |
| N692CK |  | Muskegon County Airport (KMKG) | Muskegon County Airport (KMKG) | 2026-08-22 22:32 UTC | 2026-08-22 22:46 UTC | 13m |
| AAR8733 | AAR | Gimpo International Airport (RKSS) | Yeosu Airport (RKJY) | 2026-08-22 22:13 UTC | 2026-08-22 22:43 UTC | 30m |
| N390KT |  | Sunnyhill Airport (1OR0) | Boeing Field/King County International Airport (KBFI) | 2026-08-22 21:53 UTC | 2026-08-22 22:43 UTC | 49m |
| OXF9203 | OXF | Falcon Field (KFFZ) | Marana Regional Airport (KAVQ) | 2026-08-22 20:52 UTC | 2026-08-22 22:42 UTC | 1h 49m |
| N93KK |  | Lakewood Airport (KN12) | Monmouth Executive Airport (KBLM) | 2026-08-22 21:13 UTC | 2026-08-22 22:34 UTC | 1h 20m |
| EVA072 | EVA Air | Munich International Airport (EDDM) | Taiwan Taoyuan International Airport (RCTP) | 2026-08-22 10:38 UTC | 2026-08-22 22:32 UTC | 11h 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
