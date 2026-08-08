# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_17:06:27_UTC-green)

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

**Latest saved flight:** 2026-08-08 17:06:27 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-08 17:06:27 UTC

- **178,863** saved flights
- **57,422** unique routes
- **141** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **178,863** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,149,063.7 tonnes** estimated CO2 emissions
- **124,583,404 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 7099 |
| 2 | SkyWest Airlines | 6512 |
| 3 | EJA | 3521 |
| 4 | IndiGo | 3142 |
| 5 | Southwest Airlines | 2808 |
| 6 | American Airlines | 2781 |
| 7 | ENY | 2224 |
| 8 | Delta Air Lines | 2114 |
| 9 | LATAM Airlines | 1664 |
| 10 | Lufthansa | 1600 |
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
| 22 | VIV | 983 |
| 23 | GLO | 952 |
| 24 | Cathay Pacific | 946 |
| 25 | CXK | 944 |
| 26 | AEE | 930 |
| 27 | Air France | 920 |
| 28 | United Airlines | 919 |
| 29 | MXY | 898 |
| 30 | PGT | 886 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 153323 |
| 2 | 🇪🇸 ES | 11480 |
| 3 | 🇧🇷 BR | 10241 |
| 4 | 🇦🇺 AU | 10071 |
| 5 | 🇮🇳 IN | 9848 |
| 6 | 🇨🇦 CA | 9749 |
| 7 | 🇮🇹 IT | 9253 |
| 8 | 🇩🇪 DE | 8868 |
| 9 | 🇬🇧 GB | 8262 |
| 10 | 🇯🇵 JP | 7227 |
| 11 | 🇫🇷 FR | 7130 |
| 12 | 🇨🇴 CO | 6594 |
| 13 | 🇬🇷 GR | 5217 |
| 14 | 🇲🇽 MX | 5115 |
| 15 | 🇨🇭 CH | 4774 |
| 16 | 🇳🇴 NO | 4638 |
| 17 | 🇹🇷 TR | 4519 |
| 18 | 🇲🇾 MY | 3159 |
| 19 | 🇵🇱 PL | 2985 |
| 20 | 🇿🇦 ZA | 2920 |
| 21 | 🇹🇭 TH | 2718 |
| 22 | 🇳🇿 NZ | 2582 |
| 23 | 🇵🇭 PH | 2358 |
| 24 | 🇬🇹 GT | 2286 |
| 25 | 🇰🇷 KR | 2240 |
| 26 | 🇲🇦 MA | 1811 |
| 27 | 🇭🇷 HR | 1776 |
| 28 | 🇲🇪 ME | 1630 |
| 29 | 🇳🇱 NL | 1611 |
| 30 | 🇲🇴 MO | 1510 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 3688 |
| 2 | Denver International Airport |  | US | 2957 |
| 3 | Tokyo International Airport |  | JP | 2245 |
| 4 | Guaymaral Airport |  | CO | 2193 |
| 5 | Indira Gandhi International Airport |  | IN | 2191 |
| 6 | Harry Reid International Airport |  | US | 2115 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1929 |
| 8 | Zurich Airport |  | CH | 1903 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1860 |
| 10 | La Aurora Airport |  | GT | 1757 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 1631 |
| 12 | Chicago O'Hare International Airport |  | US | 1608 |
| 13 | Salt Lake City International Airport |  | US | 1598 |
| 14 | El Dorado International Airport |  | CO | 1593 |
| 15 | Frankfurt am Main International Airport |  | DE | 1563 |
| 16 | Macau International Airport |  | MO | 1510 |
| 17 | Congonhas Airport |  | BR | 1487 |
| 18 | General Edward Lawrence Logan International Airport |  | US | 1433 |
| 19 | Capua Airport |  | IT | 1401 |
| 20 | Madrid Barajas International Airport |  | ES | 1399 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1330 |
| 22 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1271 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1248 |
| 24 | Malpensa International Airport |  | IT | 1228 |
| 25 | Charlotte/Douglas International Airport |  | US | 1216 |
| 26 | Charles de Gaulle International Airport |  | FR | 1212 |
| 27 | Kuala Lumpur International Airport |  | MY | 1190 |
| 28 | Bengaluru International Airport |  | IN | 1175 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1109 |
| 30 | Ninoy Aquino International Airport |  | PH | 1109 |
| 31 | Norman Y Mineta San Jose International Airport |  | US | 1099 |
| 32 | Barcelona International Airport |  | ES | 1062 |
| 33 | Daniel K Inouye International Airport |  | US | 1027 |
| 34 | Seattle-Tacoma International Airport |  | US | 1027 |
| 35 | Viracopos International Airport |  | BR | 1026 |
| 36 | Reno/Tahoe International Airport |  | US | 1015 |
| 37 | Calgary International Airport |  | CA | 1012 |
| 38 | Oslo Gardermoen Airport |  | NO | 994 |
| 39 | Tenerife Norte Airport |  | ES | 977 |
| 40 | Amsterdam Airport Schiphol |  | NL | 969 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 905 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 657 | 21m | 244 km | 2,766.4 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 420 | 1h 8m | 770 km | 5,579.4 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 420 | 24m | 225 km | 1,629.4 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 417 | 9m | - | - |
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
| 16 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 232 | 8m | - | - |
| 17 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 232 | 20m | 250 km | 1,002.1 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 228 | 13m | - | - |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 227 | 26m | 215 km | 840.7 t |
| 20 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 221 | 19m | 99 km | 378.6 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 218 | 31m | 49 km | 184.3 t |
| 22 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 216 | 51m | 556 km | 2,070.5 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 215 | 1h 15m | 961 km | 3,563.7 t |
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
| N330V |  | Cy Nunnally Memorial Airport (KD73) | Cy Nunnally Memorial Airport (KD73) | 2026-08-08 16:32 UTC | 2026-08-08 17:06 UTC | 34m |
| N105JF |  | North Raleigh Airport (00NC) | North Raleigh Airport (00NC) | 2026-08-08 16:42 UTC | 2026-08-08 17:02 UTC | 19m |
| CYT72 | CYT | Lovell Field (KCHA) | Southwest Georgia Regional Airport (KABY) | 2026-08-08 16:04 UTC | 2026-08-08 16:57 UTC | 52m |
| HK5007G |  | Santa Ana Airport (SKGO) | El Eden Airport (SKAR) | 2026-08-08 15:31 UTC | 2026-08-08 16:56 UTC | 1h 24m |
| N655CW |  | Massey Ranch Airpark (KX50) | Massey Ranch Airpark (KX50) | 2026-08-08 16:22 UTC | 2026-08-08 16:55 UTC | 33m |
| N567PW |  | Van Nuys Airport (KVNY) | Van Nuys Airport (KVNY) | 2026-08-08 16:13 UTC | 2026-08-08 16:54 UTC | 41m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-08-08 16:12 UTC | 2026-08-08 16:54 UTC | 42m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-08-08 16:35 UTC | 2026-08-08 16:52 UTC | 17m |
| N119RP |  | Jack Northrop Field/Hawthorne Municipal Airport (KHHR) | Ramona Airport (KRNM) | 2026-08-08 16:05 UTC | 2026-08-08 16:50 UTC | 44m |
| AOM234B | AOM | Kenitra Airport (GMMY) | Saniat Rmel Airport (GMTN) | 2026-08-08 16:26 UTC | 2026-08-08 16:49 UTC | 22m |
| N9425H |  | Dupage Airport (KDPA) | 95LL (95LL) | 2026-08-08 16:13 UTC | 2026-08-08 16:46 UTC | 33m |
| N90DT |  | Aero Country Airport (KT31) | XA65 (XA65) | 2026-08-08 16:39 UTC | 2026-08-08 16:46 UTC | 7m |
| N905JA |  | Modesto City-County-Harry Sham Field (KMOD) | Buchanan Field (KCCR) | 2026-08-08 16:13 UTC | 2026-08-08 16:46 UTC | 32m |
| BSM36 | BSM | Durant Regional/Eaker Field (KDUA) | TA22 (TA22) | 2026-08-08 16:33 UTC | 2026-08-08 16:44 UTC | 11m |
| ENY3362 | ENY | Chicago O'Hare International Airport (KORD) | Nort's Resort Airport (01PS) | 2026-08-08 15:28 UTC | 2026-08-08 16:41 UTC | 1h 12m |
| N87RM |  | Perrotti Skyranch Airfield (09ME) | Skydive New England Airport (ME64) | 2026-08-08 15:40 UTC | 2026-08-08 16:39 UTC | 59m |
| GFD50 | GFD | Boise Air Trml/Gowen Field (KBOI) | Hell Roaring Ranch Airport (ID39) | 2026-08-08 15:20 UTC | 2026-08-08 16:38 UTC | 1h 18m |
| N3040F |  | Greeneville Municipal Airport (KGCY) | Greeneville Municipal Airport (KGCY) | 2026-08-08 16:12 UTC | 2026-08-08 16:28 UTC | 15m |
| N636BE |  | Richmond Executive/Chesterfield County Airport (KFCI) | Niagara Falls International Airport (KIAG) | 2026-08-08 13:56 UTC | 2026-08-08 16:27 UTC | 2h 30m |
| N208PC |  | Hohenems-Dornbirn Airport (LOIH) | Hohenems-Dornbirn Airport (LOIH) | 2026-08-08 15:33 UTC | 2026-08-08 16:27 UTC | 54m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
