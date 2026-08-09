# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_19:51:31_UTC-green)

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

**Latest saved flight:** 2026-08-09 19:51:31 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-09 19:51:31 UTC

- **182,460** saved flights
- **58,248** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **182,460** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,193,028.6 tonnes** estimated CO2 emissions
- **127,132,095 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7245 |
| 2 | SkyWest Airlines | 6632 |
| 3 | EJA | 3599 |
| 4 | IndiGo | 3194 |
| 5 | Southwest Airlines | 2864 |
| 6 | American Airlines | 2846 |
| 7 | ENY | 2271 |
| 8 | Delta Air Lines | 2161 |
| 9 | LATAM Airlines | 1702 |
| 10 | AZU | 1635 |
| 11 | Lufthansa | 1618 |
| 12 | WIF | 1509 |
| 13 | Vueling | 1507 |
| 14 | LXJ | 1435 |
| 15 | Swiss International | 1252 |
| 16 | easyJet | 1248 |
| 17 | AXM | 1226 |
| 18 | EJU | 1123 |
| 19 | QLK | 1116 |
| 20 | All Nippon Airways | 1107 |
| 21 | Alaska Airlines | 1098 |
| 22 | VIV | 1004 |
| 23 | GLO | 979 |
| 24 | AEE | 953 |
| 25 | CXK | 951 |
| 26 | Air France | 947 |
| 27 | Cathay Pacific | 947 |
| 28 | United Airlines | 936 |
| 29 | PGT | 923 |
| 30 | MXY | 913 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 156063 |
| 2 | 🇪🇸 ES | 11740 |
| 3 | 🇧🇷 BR | 10472 |
| 4 | 🇦🇺 AU | 10203 |
| 5 | 🇮🇳 IN | 10007 |
| 6 | 🇨🇦 CA | 9930 |
| 7 | 🇮🇹 IT | 9459 |
| 8 | 🇩🇪 DE | 9050 |
| 9 | 🇬🇧 GB | 8460 |
| 10 | 🇯🇵 JP | 7379 |
| 11 | 🇫🇷 FR | 7279 |
| 12 | 🇨🇴 CO | 6794 |
| 13 | 🇬🇷 GR | 5354 |
| 14 | 🇲🇽 MX | 5205 |
| 15 | 🇨🇭 CH | 4878 |
| 16 | 🇹🇷 TR | 4736 |
| 17 | 🇳🇴 NO | 4696 |
| 18 | 🇲🇾 MY | 3195 |
| 19 | 🇵🇱 PL | 3062 |
| 20 | 🇿🇦 ZA | 3031 |
| 21 | 🇹🇭 TH | 2804 |
| 22 | 🇳🇿 NZ | 2608 |
| 23 | 🇵🇭 PH | 2410 |
| 24 | 🇬🇹 GT | 2333 |
| 25 | 🇰🇷 KR | 2263 |
| 26 | 🇲🇦 MA | 1848 |
| 27 | 🇭🇷 HR | 1822 |
| 28 | 🇲🇪 ME | 1649 |
| 29 | 🇳🇱 NL | 1641 |
| 30 | 🇲🇴 MO | 1518 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3776 |
| 2 | Denver International Airport |  | US | 3012 |
| 3 | Tokyo International Airport |  | JP | 2287 |
| 4 | Indira Gandhi International Airport |  | IN | 2237 |
| 5 | Guaymaral Airport |  | CO | 2231 |
| 6 | Harry Reid International Airport |  | US | 2138 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1961 |
| 8 | Zurich Airport |  | CH | 1952 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1897 |
| 10 | La Aurora Airport |  | GT | 1791 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1664 |
| 12 | Chicago O'Hare International Airport |  | US | 1633 |
| 13 | El Dorado International Airport |  | CO | 1630 |
| 14 | Salt Lake City International Airport |  | US | 1628 |
| 15 | Frankfurt am Main International Airport |  | DE | 1584 |
| 16 | Congonhas Airport |  | BR | 1520 |
| 17 | Macau International Airport |  | MO | 1518 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1444 |
| 19 | Madrid Barajas International Airport |  | ES | 1437 |
| 20 | Capua Airport |  | IT | 1432 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1364 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1301 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1270 |
| 24 | Malpensa International Airport |  | IT | 1262 |
| 25 | Charles de Gaulle International Airport |  | FR | 1246 |
| 26 | Charlotte/Douglas International Airport |  | US | 1237 |
| 27 | Kuala Lumpur International Airport |  | MY | 1201 |
| 28 | Bengaluru International Airport |  | IN | 1187 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1135 |
| 30 | Ninoy Aquino International Airport |  | PH | 1135 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1114 |
| 32 | Barcelona International Airport |  | ES | 1081 |
| 33 | Viracopos International Airport |  | BR | 1049 |
| 34 | Reno/Tahoe International Airport |  | US | 1048 |
| 35 | Seattle-Tacoma International Airport |  | US | 1047 |
| 36 | Daniel K Inouye International Airport |  | US | 1043 |
| 37 | Calgary International Airport |  | CA | 1037 |
| 38 | Oslo Gardermoen Airport |  | NO | 1012 |
| 39 | Tenerife Norte Airport |  | ES | 996 |
| 40 | Amsterdam Airport Schiphol |  | NL | 991 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 920 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 671 | 21m | 244 km | 2,825.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 434 | 1h 8m | 770 km | 5,765.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 428 | 24m | 225 km | 1,660.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 423 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 327 | 32m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 308 | 27m | 275 km | 1,459.5 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 298 | 1h 7m | 706 km | 3,628.2 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 271 | 44m | 241 km | 1,125.7 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 267 | 22m | 55 km | 253.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 257 | 1h 48m | 1,423 km | 6,307.2 t |
| 15 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 249 | 8m | - | - |
| 16 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 246 | 20m | 250 km | 1,062.6 t |
| 18 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 230 | 26m | 215 km | 851.8 t |
| 19 | Bodø Airport (ENBO) | ENEN (ENEN) | 229 | 13m | - | - |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 224 | 19m | 99 km | 383.7 t |
| 21 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 222 | 1h 15m | 961 km | 3,679.8 t |
| 22 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 221 | 31m | 49 km | 186.8 t |
| 23 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 220 | 50m | 556 km | 2,108.9 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 219 | 19m | 144 km | 544.8 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 219 | 12m | - | - |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 216 | 1h 38m | 1,156 km | 4,309.1 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 215 | 24m | 218 km | 810.0 t |
| 28 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 211 | 31m | 369 km | 1,343.1 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 205 | 28m | 152 km | 535.7 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 198 | 1h 1m | 695 km | 2,373.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| ASP877 | ASP | Montréal-Pierre Elliott Trudeau International Airport (CYUL) | Scottsdale Airport (KSDL) | 2026-08-09 15:06 UTC | 2026-08-09 19:51 UTC | 4h 45m |
| THY3FW | Turkish Airlines | London Gatwick Airport (EGKK) | Tekirdag Corlu Airport (LTBU) | 2026-08-09 16:53 UTC | 2026-08-09 19:46 UTC | 2h 52m |
| BAW667 | British Airways | Mikonos Airport (LGMK) | Stapleford Aerodrome (EGSG) | 2026-08-09 16:13 UTC | 2026-08-09 19:45 UTC | 3h 31m |
| EIN1LM | Aer Lingus | Dublin Airport (EIDW) | London Biggin Hill Airport (EGKB) | 2026-08-09 18:45 UTC | 2026-08-09 19:45 UTC | 59m |
| FIN7GR | Finnair | Helsinki Vantaa Airport (EFHK) | EGMT (EGMT) | 2026-08-09 17:02 UTC | 2026-08-09 19:45 UTC | 2h 42m |
| GCJAP | GCJ | Peterborough/Sibson Airport (EGSP) | Peterborough Business Airport (EGSF) | 2026-08-09 19:23 UTC | 2026-08-09 19:45 UTC | 21m |
| KLM61T | KLM Royal Dutch | Amsterdam Airport Schiphol (EHAM) | London City Airport (EGLC) | 2026-08-09 18:53 UTC | 2026-08-09 19:45 UTC | 51m |
| RYR14MJ | Ryanair | Pescara International Airport (LIBP) | Wethersfield Airport (EGVT) | 2026-08-09 17:29 UTC | 2026-08-09 19:45 UTC | 2h 15m |
| RYR16DM | Ryanair | Gdańsk Lech Wałęsa Airport (EPGD) | Wethersfield Airport (EGVT) | 2026-08-09 17:42 UTC | 2026-08-09 19:45 UTC | 2h 3m |
| RYR55CW | Ryanair | Barcelona International Airport (LEBL) | London Stansted Airport (EGSS) | 2026-08-09 17:54 UTC | 2026-08-09 19:45 UTC | 1h 50m |
| RYR889X | Ryanair | Copernicus Wrocław Airport (EPWR) | Clacton Airport (EGSQ) | 2026-08-09 18:02 UTC | 2026-08-09 19:45 UTC | 1h 43m |
| N806PH |  | John Wayne/Orange County Airport (KSNA) | Lake Tahoe Airport (KTVL) | 2026-08-09 18:50 UTC | 2026-08-09 19:41 UTC | 51m |
| EJU149U | EJU | Charles de Gaulle International Airport (LFPG) | Figari Sud-Corse Airport (LFKF) | 2026-08-09 18:12 UTC | 2026-08-09 19:41 UTC | 1h 28m |
| WIF149 | WIF | Oslo Gardermoen Airport (ENGM) | Gol Airport (ENKL) | 2026-08-09 19:04 UTC | 2026-08-09 19:40 UTC | 35m |
| N717FG |  | Trenton Mercer Airport (KTTN) | Flying W Airport (KN14) | 2026-08-09 18:31 UTC | 2026-08-09 19:39 UTC | 1h 8m |
| N350BG |  | Donald P Miller Airport (KFZI) | Wood County Regional Airport (K1G0) | 2026-08-09 19:22 UTC | 2026-08-09 19:37 UTC | 15m |
| TKR101 | TKR | Hill Afb Airport (KHIF) | Morgan County Airport (K42U) | 2026-08-09 19:35 UTC | 2026-08-09 19:37 UTC | 2m |
| N595DD |  | Scottsdale Airport (KSDL) | Glendale Regional Airport (KGEU) | 2026-08-09 19:25 UTC | 2026-08-09 19:36 UTC | 11m |
| TKR210 | TKR | Hill Afb Airport (KHIF) | Skypark Airport (KBTF) | 2026-08-09 19:32 UTC | 2026-08-09 19:35 UTC | 2m |
| N95RZ |  | Fremont Airport (K14G) | Aerodrome Les Noyers Airport (50OH) | 2026-08-09 19:24 UTC | 2026-08-09 19:34 UTC | 10m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
