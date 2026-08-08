# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_16:27:41_UTC-green)

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

**Latest saved flight:** 2026-08-08 16:27:41 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 16:27:41 UTC

- **178,746** saved flights
- **57,391** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **178,746** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,147,718.8 tonnes** estimated CO2 emissions
- **124,505,440 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7096 |
| 2 | SkyWest Airlines | 6506 |
| 3 | EJA | 3516 |
| 4 | IndiGo | 3142 |
| 5 | Southwest Airlines | 2806 |
| 6 | American Airlines | 2778 |
| 7 | ENY | 2222 |
| 8 | Delta Air Lines | 2109 |
| 9 | LATAM Airlines | 1663 |
| 10 | Lufthansa | 1597 |
| 11 | AZU | 1594 |
| 12 | WIF | 1493 |
| 13 | Vueling | 1478 |
| 14 | LXJ | 1398 |
| 15 | Swiss International | 1223 |
| 16 | easyJet | 1212 |
| 17 | AXM | 1210 |
| 18 | QLK | 1093 |
| 19 | EJU | 1090 |
| 20 | All Nippon Airways | 1088 |
| 21 | Alaska Airlines | 1081 |
| 22 | VIV | 982 |
| 23 | GLO | 950 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 944 |
| 26 | AEE | 930 |
| 27 | Air France | 920 |
| 28 | United Airlines | 919 |
| 29 | MXY | 898 |
| 30 | PGT | 884 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 153196 |
| 2 | 🇪🇸 ES | 11475 |
| 3 | 🇧🇷 BR | 10231 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9848 |
| 6 | 🇨🇦 CA | 9748 |
| 7 | 🇮🇹 IT | 9250 |
| 8 | 🇩🇪 DE | 8859 |
| 9 | 🇬🇧 GB | 8260 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7125 |
| 12 | 🇨🇴 CO | 6584 |
| 13 | 🇬🇷 GR | 5215 |
| 14 | 🇲🇽 MX | 5113 |
| 15 | 🇨🇭 CH | 4773 |
| 16 | 🇳🇴 NO | 4637 |
| 17 | 🇹🇷 TR | 4506 |
| 18 | 🇲🇾 MY | 3159 |
| 19 | 🇵🇱 PL | 2985 |
| 20 | 🇿🇦 ZA | 2918 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2284 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1808 |
| 27 | 🇭🇷 HR | 1774 |
| 28 | 🇲🇪 ME | 1630 |
| 29 | 🇳🇱 NL | 1611 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3683 |
| 2 | Denver International Airport |  | US | 2955 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Guaymaral Airport |  | CO | 2192 |
| 5 | Indira Gandhi International Airport |  | IN | 2191 |
| 6 | Harry Reid International Airport |  | US | 2114 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1929 |
| 8 | Zurich Airport |  | CH | 1903 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1859 |
| 10 | La Aurora Airport |  | GT | 1755 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1628 |
| 12 | Chicago O'Hare International Airport |  | US | 1605 |
| 13 | Salt Lake City International Airport |  | US | 1595 |
| 14 | El Dorado International Airport |  | CO | 1590 |
| 15 | Frankfurt am Main International Airport |  | DE | 1561 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1485 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1432 |
| 19 | Capua Airport |  | IT | 1401 |
| 20 | Madrid Barajas International Airport |  | ES | 1399 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1328 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1270 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1227 |
| 25 | Charlotte/Douglas International Airport |  | US | 1216 |
| 26 | Charles de Gaulle International Airport |  | FR | 1212 |
| 27 | Kuala Lumpur International Airport |  | MY | 1190 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Ninoy Aquino International Airport |  | PH | 1109 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1108 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1098 |
| 32 | Barcelona International Airport |  | ES | 1062 |
| 33 | Daniel K Inouye International Airport |  | US | 1027 |
| 34 | Viracopos International Airport |  | BR | 1026 |
| 35 | Seattle-Tacoma International Airport |  | US | 1026 |
| 36 | Reno/Tahoe International Airport |  | US | 1014 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 993 |
| 39 | Tenerife Norte Airport |  | ES | 976 |
| 40 | Amsterdam Airport Schiphol |  | NL | 969 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 905 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 657 | 21m | 244 km | 2,766.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 416 | 9m | - | - |
| 6 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 326 | 32m | - | - |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 302 | 14m | 114 km | 592.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 300 | 27m | 275 km | 1,421.6 t |
| 9 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 10 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 294 | 1h 7m | 706 km | 3,579.5 t |
| 11 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 270 | 44m | 241 km | 1,121.5 t |
| 12 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 266 | 22m | 55 km | 252.8 t |
| 13 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 264 | 29m | 304 km | 1,384.0 t |
| 14 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 250 | 1h 48m | 1,423 km | 6,135.4 t |
| 15 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 247 | 19m | 165 km | 702.6 t |
| 16 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 17 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 231 | 8m | - | - |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 215 | 51m | 556 km | 2,061.0 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 214 | 1h 15m | 961 km | 3,547.2 t |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 213 | 19m | 144 km | 529.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 209 | 1h 38m | 1,156 km | 4,169.5 t |
| 26 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 208 | 12m | - | - |
| 27 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 206 | 31m | 369 km | 1,311.2 t |
| 28 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 204 | 24m | 218 km | 768.5 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 202 | 28m | 152 km | 527.9 t |
| 30 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 195 | 1h 2m | 695 km | 2,337.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N636BE |  | Richmond Executive/Chesterfield County Airport (KFCI) | Niagara Falls International Airport (KIAG) | 2026-08-08 13:56 UTC | 2026-08-08 16:27 UTC | 2h 30m |
| N208PC |  | Hohenems-Dornbirn Airport (LOIH) | Hohenems-Dornbirn Airport (LOIH) | 2026-08-08 15:33 UTC | 2026-08-08 16:27 UTC | 54m |
| CXK235 | CXK | Cincinnati Municipal/Lunken Field (KLUK) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-08-08 15:33 UTC | 2026-08-08 16:26 UTC | 53m |
| N746BP |  | Martin State Airport (KMTN) | Martin State Airport (KMTN) | 2026-08-08 16:05 UTC | 2026-08-08 16:26 UTC | 21m |
| ARCAT75 | ARC | Gillespie Field (KSEE) | Telluride Regional Airport (KTEX) | 2026-08-08 15:07 UTC | 2026-08-08 16:25 UTC | 1h 17m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-08-08 15:59 UTC | 2026-08-08 16:21 UTC | 21m |
| N7073U |  | Bolingbrook's Clow International Airport (K1C5) | Joliet Regional Airport (KJOT) | 2026-08-08 15:57 UTC | 2026-08-08 16:21 UTC | 24m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-08 15:59 UTC | 2026-08-08 16:13 UTC | 13m |
| N49TT |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-08-08 15:50 UTC | 2026-08-08 16:10 UTC | 20m |
| LIFELN1 | LIF | 0CO8 (0CO8) | Buckley Space Force Base Airport (KBKF) | 2026-08-08 15:52 UTC | 2026-08-08 16:08 UTC | 16m |
| N3434R |  | Andersen Farms Airport (SD19) | Brookings Regional Airport (KBKX) | 2026-08-08 15:54 UTC | 2026-08-08 16:08 UTC | 14m |
| N114NS |  | Lake Creek Ranch Airport (92CO) | Ak Su Airport (CO61) | 2026-08-08 15:48 UTC | 2026-08-08 16:07 UTC | 19m |
| N929CD |  | Rocky Mountain Metro Airport (KBJC) | City Of Colorado Springs Municipal Airport (KCOS) | 2026-08-08 15:29 UTC | 2026-08-08 16:05 UTC | 36m |
| RGA01 | RGA | Birrfeld Airport (LSZF) | Dubendorf Airport (LSMD) | 2026-08-08 15:55 UTC | 2026-08-08 16:03 UTC | 8m |
| N9526G |  | Peter O Knight Airport (KTPF) | Plant City Airport (KPCM) | 2026-08-08 15:44 UTC | 2026-08-08 16:02 UTC | 18m |
| PROOS | PRO | SBMM (SBMM) | SBMM (SBMM) | 2026-08-08 15:47 UTC | 2026-08-08 16:01 UTC | 14m |
|  |  | Barrow County Airport (KWDR) | Barrow County Airport (KWDR) | 2026-08-08 15:54 UTC | 2026-08-08 15:58 UTC | 3m |
| XBMLF | XBM | Atizapan De Zaragoza Airport (MMJC) | Atizapan De Zaragoza Airport (MMJC) | 2026-08-08 15:08 UTC | 2026-08-08 15:58 UTC | 50m |
| N145SH |  | P K Airpark (K5W4) | P K Airpark (K5W4) | 2026-08-08 14:47 UTC | 2026-08-08 15:58 UTC | 1h 10m |
| N337MC |  | Albuquerque International Sunport Airport (KABQ) | Socorro Municipal Airport (KONM) | 2026-08-08 15:24 UTC | 2026-08-08 15:54 UTC | 29m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
