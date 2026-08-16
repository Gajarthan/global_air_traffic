# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_07:11:41_UTC-green)

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

**Latest saved flight:** 2026-08-16 07:11:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-16 07:11:41 UTC

- **203,734** saved flights
- **65,229** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **203,734** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,448,209.3 tonnes** estimated CO2 emissions
- **141,925,175 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 8002 |
| 2 | SkyWest Airlines | 7351 |
| 3 | EJA | 3956 |
| 4 | IndiGo | 3472 |
| 5 | American Airlines | 3400 |
| 6 | Southwest Airlines | 3304 |
| 7 | Delta Air Lines | 2611 |
| 8 | ENY | 2548 |
| 9 | LATAM Airlines | 1907 |
| 10 | AZU | 1836 |
| 11 | Lufthansa | 1727 |
| 12 | Vueling | 1685 |
| 13 | WIF | 1640 |
| 14 | LXJ | 1606 |
| 15 | easyJet | 1397 |
| 16 | Swiss International | 1352 |
| 17 | AXM | 1321 |
| 18 | United Airlines | 1292 |
| 19 | Alaska Airlines | 1275 |
| 20 | QLK | 1255 |
| 21 | EJU | 1242 |
| 22 | All Nippon Airways | 1237 |
| 23 | VIV | 1119 |
| 24 | GLO | 1094 |
| 25 | PGT | 1080 |
| 26 | Air France | 1078 |
| 27 | JetBlue | 1051 |
| 28 | AEE | 1037 |
| 29 | WMT | 1012 |
| 30 | CXK | 1011 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 173773 |
| 2 | 🇪🇸 ES | 13003 |
| 3 | 🇧🇷 BR | 11644 |
| 4 | 🇦🇺 AU | 11432 |
| 5 | 🇨🇦 CA | 11274 |
| 6 | 🇮🇳 IN | 10845 |
| 7 | 🇮🇹 IT | 10537 |
| 8 | 🇩🇪 DE | 10029 |
| 9 | 🇬🇧 GB | 9466 |
| 10 | 🇯🇵 JP | 8361 |
| 11 | 🇨🇴 CO | 8044 |
| 12 | 🇫🇷 FR | 8043 |
| 13 | 🇬🇷 GR | 5972 |
| 14 | 🇲🇽 MX | 5741 |
| 15 | 🇹🇷 TR | 5684 |
| 16 | 🇨🇭 CH | 5426 |
| 17 | 🇳🇴 NO | 5077 |
| 18 | 🇲🇾 MY | 3473 |
| 19 | 🇿🇦 ZA | 3382 |
| 20 | 🇵🇱 PL | 3337 |
| 21 | 🇹🇭 TH | 3200 |
| 22 | 🇳🇿 NZ | 2839 |
| 23 | 🇵🇭 PH | 2697 |
| 24 | 🇬🇹 GT | 2556 |
| 25 | 🇰🇷 KR | 2487 |
| 26 | 🇭🇷 HR | 2141 |
| 27 | 🇲🇦 MA | 2040 |
| 28 | 🇳🇱 NL | 1805 |
| 29 | 🇲🇪 ME | 1689 |
| 30 | 🇮🇩 ID | 1667 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4287 |
| 2 | Denver International Airport |  | US | 3339 |
| 3 | Tokyo International Airport |  | JP | 2526 |
| 4 | Guaymaral Airport |  | CO | 2476 |
| 5 | Indira Gandhi International Airport |  | IN | 2463 |
| 6 | Harry Reid International Airport |  | US | 2321 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2128 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2118 |
| 9 | Zurich Airport |  | CH | 2110 |
| 10 | La Aurora Airport |  | GT | 1958 |
| 11 | Chicago O'Hare International Airport |  | US | 1903 |
| 12 | El Dorado International Airport |  | CO | 1860 |
| 13 | Phoenix Sky Harbor International Airport |  | US | 1826 |
| 14 | Salt Lake City International Airport |  | US | 1808 |
| 15 | Congonhas Airport |  | BR | 1694 |
| 16 | Frankfurt am Main International Airport |  | DE | 1688 |
| 17 | Madrid Barajas International Airport |  | ES | 1587 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1564 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1555 |
| 20 | Macau International Airport |  | MO | 1541 |
| 21 | Capua Airport |  | IT | 1539 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1471 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1433 |
| 24 | Malpensa International Airport |  | IT | 1400 |
| 25 | Charlotte/Douglas International Airport |  | US | 1391 |
| 26 | Charles de Gaulle International Airport |  | FR | 1387 |
| 27 | Kuala Lumpur International Airport |  | MY | 1290 |
| 28 | Ninoy Aquino International Airport |  | PH | 1276 |
| 29 | Bengaluru International Airport |  | IN | 1264 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1257 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1231 |
| 32 | Barcelona International Airport |  | ES | 1215 |
| 33 | Seattle-Tacoma International Airport |  | US | 1212 |
| 34 | Viracopos International Airport |  | BR | 1177 |
| 35 | Calgary International Airport |  | CA | 1157 |
| 36 | Reno/Tahoe International Airport |  | US | 1133 |
| 37 | Oslo Gardermoen Airport |  | NO | 1120 |
| 38 | Vitoria/Foronda Airport |  | ES | 1119 |
| 39 | Daniel K Inouye International Airport |  | US | 1103 |
| 40 | Tenerife Norte Airport |  | ES | 1096 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1019 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 729 | 21m | 244 km | 3,069.6 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 493 | 1h 7m | 770 km | 6,549.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 473 | 24m | 225 km | 1,835.0 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 466 | 10m | - | - |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 383 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 342 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 340 | 27m | 275 km | 1,611.1 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 307 | 1h 7m | 706 km | 3,737.7 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 299 | 44m | 241 km | 1,242.0 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 293 | 1h 49m | 1,423 km | 7,190.7 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 287 | 22m | 55 km | 272.8 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 262 | 21m | 250 km | 1,131.7 t |
| 17 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 251 | 24m | 218 km | 945.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 248 | 26m | 215 km | 918.5 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 248 | 19m | 165 km | 705.4 t |
| 20 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 245 | 1h 14m | 961 km | 4,061.0 t |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 245 | 19m | 99 km | 419.7 t |
| 22 | Bodø Airport (ENBO) | ENEN (ENEN) | 244 | 13m | - | - |
| 23 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 239 | 1h 37m | 1,156 km | 4,768.0 t |
| 24 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 234 | 19m | 144 km | 582.1 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 229 | 31m | 369 km | 1,457.6 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 220 | 1h 49m | 1,304 km | 4,949.4 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 216 | 1h 3m | 695 km | 2,589.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| EXS6UB | EXS | Birmingham International Airport (EGBB) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-16 05:03 UTC | 2026-08-16 07:11 UTC | 2h 7m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-16 06:33 UTC | 2026-08-16 07:05 UTC | 31m |
| IOV | IOV | YSMB (YSMB) | Sydney Kingsford Smith International Airport (YSSY) | 2026-08-16 06:45 UTC | 2026-08-16 07:02 UTC | 17m |
| HSEFS | HSE | Bang Pra Airport (VTBT) | Bang Pra Airport (VTBT) | 2026-08-16 06:44 UTC | 2026-08-16 06:53 UTC | 9m |
| BEL5BN | Brussels Airlines | Brussels Airport (EBBR) | Malpensa International Airport (LIMC) | 2026-08-16 04:43 UTC | 2026-08-16 06:44 UTC | 2h 0m |
| DLH207 | Lufthansa | Berlin Brandenburg Airport (EDDB) | Frankfurt am Main International Airport (EDDF) | 2026-08-16 05:41 UTC | 2026-08-16 06:37 UTC | 56m |
| MRS0915 | MRS | Ifrane Airport (GMFI) | Olbia / Costa Smeralda Airport (LIEO) | 2026-08-16 04:46 UTC | 2026-08-16 06:33 UTC | 1h 47m |
| CRUSH51 | CRU | Grant County International Airport (KMWH) | Hanson Airport (0MT6) | 2026-08-16 05:53 UTC | 2026-08-16 06:32 UTC | 38m |
| RYR32TE | Ryanair | Pescara International Airport (LIBP) | Bergamo / Orio Al Serio Airport (LIME) | 2026-08-16 05:41 UTC | 2026-08-16 06:30 UTC | 48m |
| WWF287 | WWF | Roberts Field/Redmond Municipal Airport (KRDM) | Collins Landing Strip (04OR) | 2026-08-16 05:37 UTC | 2026-08-16 06:29 UTC | 52m |
| BBC388 | BBC | VGZR (VGZR) | Naypyidaw Airport (VYEL) | 2026-08-16 05:27 UTC | 2026-08-16 06:25 UTC | 58m |
| RYR178Q | Ryanair | Henri Coanda International Airport (LROP) | Paris Beauvais Tille Airport (LFOB) | 2026-08-16 03:46 UTC | 2026-08-16 06:22 UTC | 2h 36m |
| QLK24D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-08-16 05:36 UTC | 2026-08-16 06:18 UTC | 42m |
| NVP | NVP | Kyneton Airport (YKTN) | Melbourne Essendon Airport (YMEN) | 2026-08-16 05:51 UTC | 2026-08-16 06:18 UTC | 27m |
| RYR72JG | Ryanair | Aarhus Airport (EKAH) | Pruszcz Gdański Airport (EPPR) | 2026-08-16 05:30 UTC | 2026-08-16 06:16 UTC | 46m |
| VJT409 | VJT | Linate Airport (LIML) | Samedan Airport (LSZS) | 2026-08-16 05:53 UTC | 2026-08-16 06:16 UTC | 22m |
| TGW420 | TGW | Changi Air Base (WSAC) | Malacca Airport (WMKM) | 2026-08-16 05:46 UTC | 2026-08-16 06:15 UTC | 28m |
| ANE87CJ | ANE | Madrid Barajas International Airport (LEMD) | La Morgal Airport (LEMR) | 2026-08-16 05:35 UTC | 2026-08-16 06:09 UTC | 34m |
| CHX25 | CHX | Hunsborn Airport (EDKH) | Hunsborn Airport (EDKH) | 2026-08-16 06:04 UTC | 2026-08-16 06:09 UTC | 5m |
| EZS91YN | EZS | Geneva Cointrin International Airport (LSGG) | Ghisonaccia Alzitone Airport (LFKG) | 2026-08-16 05:09 UTC | 2026-08-16 06:07 UTC | 58m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
