# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_07:49:04_UTC-green)

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

**Latest saved flight:** 2026-08-08 07:49:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 07:49:04 UTC

- **177,614** saved flights
- **57,142** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **177,614** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,134,324.7 tonnes** estimated CO2 emissions
- **123,728,971 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7037 |
| 2 | SkyWest Airlines | 6496 |
| 3 | EJA | 3507 |
| 4 | IndiGo | 3115 |
| 5 | Southwest Airlines | 2804 |
| 6 | American Airlines | 2772 |
| 7 | ENY | 2213 |
| 8 | Delta Air Lines | 2100 |
| 9 | LATAM Airlines | 1646 |
| 10 | Lufthansa | 1588 |
| 11 | AZU | 1581 |
| 12 | WIF | 1482 |
| 13 | Vueling | 1461 |
| 14 | LXJ | 1395 |
| 15 | Swiss International | 1209 |
| 16 | AXM | 1203 |
| 17 | easyJet | 1200 |
| 18 | QLK | 1092 |
| 19 | EJU | 1083 |
| 20 | Alaska Airlines | 1081 |
| 21 | All Nippon Airways | 1079 |
| 22 | VIV | 979 |
| 23 | Cathay Pacific | 946 |
| 24 | CXK | 942 |
| 25 | GLO | 939 |
| 26 | AEE | 924 |
| 27 | United Airlines | 917 |
| 28 | Air France | 911 |
| 29 | MXY | 896 |
| 30 | JetBlue | 877 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 152719 |
| 2 | 🇪🇸 ES | 11345 |
| 3 | 🇧🇷 BR | 10138 |
| 4 | 🇦🇺 AU | 10060 |
| 5 | 🇮🇳 IN | 9767 |
| 6 | 🇨🇦 CA | 9723 |
| 7 | 🇮🇹 IT | 9166 |
| 8 | 🇩🇪 DE | 8756 |
| 9 | 🇬🇧 GB | 8176 |
| 10 | 🇯🇵 JP | 7161 |
| 11 | 🇫🇷 FR | 7031 |
| 12 | 🇨🇴 CO | 6526 |
| 13 | 🇬🇷 GR | 5173 |
| 14 | 🇲🇽 MX | 5096 |
| 15 | 🇨🇭 CH | 4695 |
| 16 | 🇳🇴 NO | 4610 |
| 17 | 🇹🇷 TR | 4427 |
| 18 | 🇲🇾 MY | 3136 |
| 19 | 🇵🇱 PL | 2952 |
| 20 | 🇿🇦 ZA | 2884 |
| 21 | 🇹🇭 TH | 2660 |
| 22 | 🇳🇿 NZ | 2580 |
| 23 | 🇵🇭 PH | 2346 |
| 24 | 🇬🇹 GT | 2270 |
| 25 | 🇰🇷 KR | 2223 |
| 26 | 🇲🇦 MA | 1794 |
| 27 | 🇭🇷 HR | 1749 |
| 28 | 🇲🇪 ME | 1610 |
| 29 | 🇳🇱 NL | 1598 |
| 30 | 🇲🇴 MO | 1508 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3673 |
| 2 | Denver International Airport |  | US | 2948 |
| 3 | Tokyo International Airport |  | JP | 2228 |
| 4 | Guaymaral Airport |  | CO | 2177 |
| 5 | Indira Gandhi International Airport |  | IN | 2174 |
| 6 | Harry Reid International Airport |  | US | 2113 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1918 |
| 8 | Zurich Airport |  | CH | 1881 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1854 |
| 10 | La Aurora Airport |  | GT | 1745 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1627 |
| 12 | Chicago O'Hare International Airport |  | US | 1599 |
| 13 | Salt Lake City International Airport |  | US | 1590 |
| 14 | El Dorado International Airport |  | CO | 1584 |
| 15 | Frankfurt am Main International Airport |  | DE | 1552 |
| 16 | Macau International Airport |  | MO | 1508 |
| 17 | Congonhas Airport |  | BR | 1471 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1428 |
| 19 | Capua Airport |  | IT | 1390 |
| 20 | Madrid Barajas International Airport |  | ES | 1384 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1322 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1255 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1246 |
| 24 | Malpensa International Airport |  | IT | 1215 |
| 25 | Charlotte/Douglas International Airport |  | US | 1212 |
| 26 | Charles de Gaulle International Airport |  | FR | 1202 |
| 27 | Kuala Lumpur International Airport |  | MY | 1182 |
| 28 | Bengaluru International Airport |  | IN | 1161 |
| 29 | Ninoy Aquino International Airport |  | PH | 1104 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1102 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1054 |
| 33 | Daniel K Inouye International Airport |  | US | 1025 |
| 34 | Seattle-Tacoma International Airport |  | US | 1025 |
| 35 | Viracopos International Airport |  | BR | 1016 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 989 |
| 39 | Tenerife Norte Airport |  | ES | 971 |
| 40 | Amsterdam Airport Schiphol |  | NL | 960 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 899 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 655 | 21m | 244 km | 2,758.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 418 | 24m | 225 km | 1,621.6 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 414 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 413 | 1h 8m | 770 km | 5,486.4 t |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 9 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 298 | 27m | 275 km | 1,412.1 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 292 | 1h 7m | 706 km | 3,555.1 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 269 | 44m | 241 km | 1,117.4 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 15 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 246 | 1h 48m | 1,423 km | 6,037.2 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 231 | 20m | 250 km | 997.8 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 227 | 13m | - | - |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 225 | 26m | 215 km | 833.3 t |
| 19 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 223 | 8m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 220 | 20m | 99 km | 376.8 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 212 | 1h 15m | 961 km | 3,514.0 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 211 | 19m | 144 km | 524.9 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 208 | 1h 38m | 1,156 km | 4,149.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 205 | 31m | 369 km | 1,304.9 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 202 | 24m | 218 km | 761.0 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 201 | 28m | 152 km | 525.3 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 194 | 1h 2m | 695 km | 2,325.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKASF | OKA | Hradec Kralove Airport (LKHK) | Mnichovo Hradiste Airport (LKMH) | 2026-08-08 07:13 UTC | 2026-08-08 07:49 UTC | 35m |
| FNG8 | FNG | Genbole Airport (EFGE) | Kymi Airport (EFKY) | 2026-08-08 07:08 UTC | 2026-08-08 07:47 UTC | 39m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-08 07:35 UTC | 2026-08-08 07:46 UTC | 11m |
| DLH3A | Lufthansa | Amsterdam Airport Schiphol (EHAM) | Frankfurt am Main International Airport (EDDF) | 2026-08-08 07:02 UTC | 2026-08-08 07:42 UTC | 39m |
| THA672 | Thai Airways | Suvarnabhumi Airport (VTBS) | Kansai International Airport (RJBB) | 2026-08-08 02:22 UTC | 2026-08-08 07:40 UTC | 5h 17m |
| 4XCCM |  | Haifa International Airport (LLHA) | St Catherine International Airport (HESC) | 2026-08-08 06:05 UTC | 2026-08-08 07:34 UTC | 1h 29m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-08-08 07:09 UTC | 2026-08-08 07:28 UTC | 19m |
| N951RP |  | Riverside Airport (KRAL) | Riverside Airport (KRAL) | 2026-08-08 05:57 UTC | 2026-08-08 07:28 UTC | 1h 30m |
| ECISV | ECI | Ampuriabrava Airport (LEAP) | Ampuriabrava Airport (LEAP) | 2026-08-08 07:11 UTC | 2026-08-08 07:24 UTC | 12m |
| DLH5T | Lufthansa | Munich International Airport (EDDM) | Berlin Brandenburg Airport (EDDB) | 2026-08-08 06:34 UTC | 2026-08-08 07:18 UTC | 44m |
| HBFKL | HBF | Sitterdorf Airport (LSZV) | Sitterdorf Airport (LSZV) | 2026-08-08 06:49 UTC | 2026-08-08 07:11 UTC | 21m |
| SXAEN | SXA | Amigdhaleon Airport (LGKM) | Nea Anchialos Airport (LGBL) | 2026-08-08 05:32 UTC | 2026-08-08 07:07 UTC | 1h 34m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 06:55 UTC | 2026-08-08 07:05 UTC | 10m |
| SCR137 | SCR | Cannes-Mandelieu Airport (LFMD) | Ossiacher See Airport (LOKF) | 2026-08-08 06:10 UTC | 2026-08-08 07:05 UTC | 55m |
| A7GAC |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-08 06:18 UTC | 2026-08-08 07:04 UTC | 46m |
| RYR8ZU | Ryanair | Warsaw Modlin Airport (EPMO) | Capua Airport (LIAU) | 2026-08-08 05:13 UTC | 2026-08-08 07:01 UTC | 1h 48m |
| WIF1X | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-08-08 06:46 UTC | 2026-08-08 06:57 UTC | 10m |
| ZSOKA | ZSO | O. R. Tambo International Airport (FAOR) | Walkersons Field (FADU) | 2026-08-08 06:21 UTC | 2026-08-08 06:50 UTC | 29m |
| SPNTS | SPN | Nowy Targ Airport (EPNT) | Nowy Targ Airport (EPNT) | 2026-08-08 06:33 UTC | 2026-08-08 06:47 UTC | 14m |
| GPJCD | GPJ | Norwich International Airport (EGSH) | EGYO (EGYO) | 2026-08-08 05:41 UTC | 2026-08-08 06:44 UTC | 1h 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
