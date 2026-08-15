# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_05:24:58_UTC-green)

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

**Latest saved flight:** 2026-08-15 05:24:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-15 05:24:58 UTC

- **197,615** saved flights
- **61,932** unique routes
- **143** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **197,615** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,359,570.7 tonnes** estimated CO2 emissions
- **136,786,708 km** total distance flown
- **852 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7838 |
| 2 | SkyWest Airlines | 7115 |
| 3 | EJA | 3896 |
| 4 | IndiGo | 3405 |
| 5 | Southwest Airlines | 3069 |
| 6 | American Airlines | 3054 |
| 7 | ENY | 2445 |
| 8 | Delta Air Lines | 2344 |
| 9 | LATAM Airlines | 1856 |
| 10 | AZU | 1791 |
| 11 | Lufthansa | 1696 |
| 12 | Vueling | 1645 |
| 13 | WIF | 1628 |
| 14 | LXJ | 1570 |
| 15 | easyJet | 1354 |
| 16 | Swiss International | 1331 |
| 17 | AXM | 1290 |
| 18 | EJU | 1222 |
| 19 | QLK | 1221 |
| 20 | All Nippon Airways | 1194 |
| 21 | Alaska Airlines | 1172 |
| 22 | VIV | 1091 |
| 23 | GLO | 1070 |
| 24 | Air France | 1034 |
| 25 | PGT | 1031 |
| 26 | AEE | 1015 |
| 27 | United Airlines | 1009 |
| 28 | CXK | 1005 |
| 29 | WMT | 988 |
| 30 | Wizz Air | 974 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 168138 |
| 2 | 🇪🇸 ES | 12719 |
| 3 | 🇧🇷 BR | 11381 |
| 4 | 🇦🇺 AU | 11118 |
| 5 | 🇨🇦 CA | 10839 |
| 6 | 🇮🇳 IN | 10638 |
| 7 | 🇮🇹 IT | 10274 |
| 8 | 🇩🇪 DE | 9780 |
| 9 | 🇬🇧 GB | 9252 |
| 10 | 🇯🇵 JP | 8049 |
| 11 | 🇫🇷 FR | 7847 |
| 12 | 🇨🇴 CO | 7801 |
| 13 | 🇬🇷 GR | 5800 |
| 14 | 🇲🇽 MX | 5604 |
| 15 | 🇹🇷 TR | 5391 |
| 16 | 🇨🇭 CH | 5317 |
| 17 | 🇳🇴 NO | 5044 |
| 18 | 🇲🇾 MY | 3372 |
| 19 | 🇿🇦 ZA | 3322 |
| 20 | 🇵🇱 PL | 3258 |
| 21 | 🇹🇭 TH | 3063 |
| 22 | 🇳🇿 NZ | 2769 |
| 23 | 🇵🇭 PH | 2615 |
| 24 | 🇬🇹 GT | 2530 |
| 25 | 🇰🇷 KR | 2396 |
| 26 | 🇭🇷 HR | 2063 |
| 27 | 🇲🇦 MA | 1994 |
| 28 | 🇳🇱 NL | 1770 |
| 29 | 🇲🇪 ME | 1687 |
| 30 | 🇮🇩 ID | 1621 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4117 |
| 2 | Denver International Airport |  | US | 3220 |
| 3 | Tokyo International Airport |  | JP | 2469 |
| 4 | Guaymaral Airport |  | CO | 2443 |
| 5 | Indira Gandhi International Airport |  | IN | 2408 |
| 6 | Harry Reid International Airport |  | US | 2268 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 2085 |
| 8 | Zurich Airport |  | CH | 2081 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2049 |
| 10 | La Aurora Airport |  | GT | 1938 |
| 11 | El Dorado International Airport |  | CO | 1815 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1764 |
| 13 | Salt Lake City International Airport |  | US | 1758 |
| 14 | Chicago O'Hare International Airport |  | US | 1736 |
| 15 | Congonhas Airport |  | BR | 1665 |
| 16 | Frankfurt am Main International Airport |  | DE | 1663 |
| 17 | Madrid Barajas International Airport |  | ES | 1548 |
| 18 | Macau International Airport |  | MO | 1532 |
| 19 | General Edward Lawrence Logan International Airport |  | US | 1508 |
| 20 | Capua Airport |  | IT | 1507 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1458 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1424 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1376 |
| 24 | Malpensa International Airport |  | IT | 1369 |
| 25 | Charles de Gaulle International Airport |  | FR | 1350 |
| 26 | Charlotte/Douglas International Airport |  | US | 1308 |
| 27 | Kuala Lumpur International Airport |  | MY | 1259 |
| 28 | Bengaluru International Airport |  | IN | 1248 |
| 29 | Ninoy Aquino International Airport |  | PH | 1237 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1236 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1211 |
| 32 | Barcelona International Airport |  | ES | 1182 |
| 33 | Viracopos International Airport |  | BR | 1151 |
| 34 | Seattle-Tacoma International Airport |  | US | 1139 |
| 35 | Calgary International Airport |  | CA | 1127 |
| 36 | Reno/Tahoe International Airport |  | US | 1116 |
| 37 | Oslo Gardermoen Airport |  | NO | 1112 |
| 38 | Daniel K Inouye International Airport |  | US | 1101 |
| 39 | Vitoria/Foronda Airport |  | ES | 1082 |
| 40 | Tenerife Norte Airport |  | ES | 1077 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1006 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 728 | 21m | 244 km | 3,065.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 479 | 1h 7m | 770 km | 6,363.1 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 462 | 10m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 460 | 24m | 225 km | 1,784.6 t |
| 6 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 354 | 8m | - | - |
| 7 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 338 | 32m | - | - |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 330 | 27m | 275 km | 1,563.7 t |
| 9 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 310 | 14m | 114 km | 608.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 305 | 1h 7m | 706 km | 3,713.4 t |
| 11 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 12 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 297 | 44m | 241 km | 1,233.7 t |
| 13 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 285 | 1h 49m | 1,423 km | 6,994.3 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 282 | 22m | 55 km | 268.0 t |
| 15 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 261 | 21m | 250 km | 1,127.4 t |
| 17 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 245 | 26m | 215 km | 907.4 t |
| 19 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 243 | 24m | 218 km | 915.5 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 243 | 13m | - | - |
| 21 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 242 | 19m | 99 km | 414.5 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 241 | 1h 15m | 961 km | 3,994.7 t |
| 23 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 238 | 12m | - | - |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 235 | 1h 38m | 1,156 km | 4,688.2 t |
| 25 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 234 | 50m | 556 km | 2,243.1 t |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 231 | 19m | 144 km | 574.6 t |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 225 | 31m | 369 km | 1,432.2 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 222 | 31m | 49 km | 187.6 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 215 | 28m | 152 km | 561.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 214 | 1h 3m | 695 km | 2,565.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CFH21 | CFH | Newcastle Airport (YWLM) | Kelvin Station Airport (YKEL) | 2026-08-15 04:52 UTC | 2026-08-15 05:24 UTC | 32m |
| JAL6777 | Japan Airlines | Narita International Airport (RJAA) | Tianjin Binhai International Airport (ZBTJ) | 2026-08-15 02:10 UTC | 2026-08-15 05:05 UTC | 2h 54m |
| FLE505 | FLE | Calgary International Airport (CYYC) | Abbotsford Airport (CYXX) | 2026-08-15 04:01 UTC | 2026-08-15 05:02 UTC | 1h 0m |
| BBC536 | BBC | Cox's Bazar Airport (VGCB) | Paro Airport (VQPR) | 2026-08-15 04:00 UTC | 2026-08-15 05:02 UTC | 1h 2m |
| WEN3569 | WEN | Kelowna Airport (CYLW) | Vancouver International Airport (CYVR) | 2026-08-15 04:09 UTC | 2026-08-15 05:00 UTC | 51m |
| SDA347 | SDA | Wellington International Airport (NZWN) | Woodbourne Airport (NZWB) | 2026-08-15 04:32 UTC | 2026-08-15 04:57 UTC | 24m |
| N23DD |  | Van Nuys Airport (KVNY) | Riverside Airport (KRAL) | 2026-08-15 04:14 UTC | 2026-08-15 04:55 UTC | 40m |
| APG225 | APG | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 2026-08-15 04:30 UTC | 2026-08-15 04:54 UTC | 23m |
| N915SH |  | Joe Foss Field (KFSD) | Clark County Airport (K8D7) | 2026-08-15 04:29 UTC | 2026-08-15 04:53 UTC | 24m |
| AIQ3923 | AIQ | Don Mueang International Airport (VTBD) | Khunan Phumipol Airport (VTPY) | 2026-08-15 04:17 UTC | 2026-08-15 04:52 UTC | 35m |
| ZSNVE | ZSN | Wonderboom Airport (FAWB) | Morningside Farm Airport (FAMS) | 2026-08-15 04:25 UTC | 2026-08-15 04:50 UTC | 24m |
| ANZ607 | ANZ | Wellington International Airport (NZWN) | Pukaki Airport (NZUK) | 2026-08-15 04:08 UTC | 2026-08-15 04:50 UTC | 42m |
| VOE9ZA | VOE | Verona / Villafranca Airport (LIPX) | Corte Airport (LFKT) | 2026-08-15 04:13 UTC | 2026-08-15 04:49 UTC | 35m |
| WMT2GJ | WMT | Henri Coanda International Airport (LROP) | Berlin Brandenburg Airport (EDDB) | 2026-08-15 02:56 UTC | 2026-08-15 04:46 UTC | 1h 50m |
| SEH1JT | SEH | Eleftherios Venizelos International Airport (LGAV) | Kalymnos Airport (LGKY) | 2026-08-15 04:23 UTC | 2026-08-15 04:43 UTC | 19m |
| MII | MII | Melbourne Moorabbin Airport (YMMB) | Melbourne Essendon Airport (YMEN) | 2026-08-15 04:26 UTC | 2026-08-15 04:40 UTC | 14m |
| VAR513 | VAR | Phoenix Goodyear Airport (KGYR) | Phoenix Goodyear Airport (KGYR) | 2026-08-15 04:15 UTC | 2026-08-15 04:35 UTC | 20m |
| EJA352 | EJA | Santa Barbara Municipal Airport (KSBA) | Oakland San Francisco Bay Airport (KOAK) | 2026-08-15 03:51 UTC | 2026-08-15 04:34 UTC | 43m |
| AZU4411 | AZU | Fazenda Flexas Airport (SNYM) | Benedito Mutran Airport (SIBD) | 2026-08-15 03:00 UTC | 2026-08-15 04:33 UTC | 1h 33m |
| N142EB |  | Mc Gregor Executive Airport (KPWG) | 81NM (81NM) | 2026-08-15 03:00 UTC | 2026-08-15 04:33 UTC | 1h 33m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
